---
name: oauth-saas-setup
description: >
  SaaS-style OAuth integration pattern: one-click login, zero manual input, full auto-discovery.
  Use when building any third-party platform integration (Meta, Google, LinkedIn, etc.) that requires
  OAuth authentication, API asset discovery, or setup wizards. Triggers on: OAuth setup, connect platform,
  API integration, auto-discovery, token exchange, third-party login, platform onboarding, CAPI setup,
  pixel setup, ad account setup, social account connection, analytics connection.
---

# OAuth SaaS Setup Pattern

## Core Philosophy

**The user clicks ONE button and never opens the third-party platform's dashboard.**

Everything that CAN be discovered via API MUST be discovered via API. Manual input fields are a last resort, not a default. The user should never need to copy-paste IDs, tokens, or secrets.

```
USER EXPERIENCE:
Click "Connect {Platform}" → OAuth popup → Allow → Auto-discovery → Pick from lists → Done
Connection stays active FOREVER. User never reconnects manually.

NEVER:
- Show token/secret input fields
- Ask for Pixel IDs, Account IDs, Property IDs
- Link to external dashboards for "copy this value"
- Require the user to understand API concepts
- Show "token expired" errors to the user
- Ask the user to reconnect because a token expired
```

## Connect Once, Stay Connected Forever

**The user connects ONCE and the system stays connected indefinitely.** Token renewal is the system's job, not the user's. Users should never see token expiry warnings, reconnect buttons, or "session expired" messages under normal operation.

### Token Lifecycle Strategy

Every platform has different token mechanics. The system MUST handle all of them transparently:

| Platform | Token Type | Lifetime | Renewal Strategy |
|---|---|---|---|
| **Google** (GA4, GSC) | Refresh token | Indefinite | Use `refresh_token` to get new `access_token` before every API call |
| **Meta** (Pixel, Ads, Pages) | Long-lived token | ~60 days | Cron job exchanges current token for a new one before expiry |
| **LinkedIn** | Access token | 60 days (refresh: 365 days) | Use `refresh_token`, re-request refresh token annually |

### Implementation Rules

1. **Always request `offline_access` / refresh token scopes** — This is what gives indefinite access
2. **Always store the `refresh_token`** — This is the key to permanent connections
3. **Auto-refresh before expiry, not after** — A cron job should refresh tokens days before they expire
4. **Never surface token state to the user** — The connection is either "working" or "disconnected"
5. **Only show reconnect if the refresh token itself is revoked** — This only happens if the user manually revokes access in the platform's settings

### Token Refresh Patterns

#### Google (Refresh Token Pattern)
Google gives a `refresh_token` during OAuth that never expires (unless revoked). Use it to silently get fresh `access_token`s:

```typescript
// Before any Google API call:
async function getValidGoogleToken(conn: GoogleConnection): Promise<string> {
  // Access token still valid? Use it.
  if (conn.token_expires_at > Date.now() + 5 * 60 * 1000) {
    return conn.access_token;
  }

  // Silently refresh using refresh_token
  const resp = await fetch("https://oauth2.googleapis.com/token", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      client_id: process.env.GOOGLE_CLIENT_ID!,
      client_secret: process.env.GOOGLE_CLIENT_SECRET!,
      refresh_token: conn.refresh_token!,
      grant_type: "refresh_token",
    }),
  });

  const data = await resp.json();
  // Save new access_token + expires_at to database
  await updateTokens(conn.user_id, data.access_token, Date.now() + data.expires_in * 1000);
  return data.access_token;
}
```

**Critical:** Request `access_type=offline` and `prompt=consent` in the OAuth URL to guarantee a refresh token.

#### Meta (Long-Lived Token Exchange Pattern)
Meta doesn't give refresh tokens. Instead, exchange the current long-lived token for a new one before it expires:

```typescript
// Cron job: runs daily, refreshes tokens expiring within 7 days
export const refreshMetaTokens = cronAction({
  schedule: "0 3 * * *", // 3 AM daily
  handler: async (ctx) => {
    const expiringSoon = await ctx.runQuery(
      internal.metaConnections.getExpiringSoon,
      { withinMs: 7 * 24 * 60 * 60 * 1000 } // 7 days
    );

    for (const conn of expiringSoon) {
      const resp = await fetch(
        `https://graph.facebook.com/v21.0/oauth/access_token?` +
        `grant_type=fb_exchange_token&` +
        `client_id=${process.env.META_APP_ID}&` +
        `client_secret=${process.env.META_APP_SECRET}&` +
        `fb_exchange_token=${conn.access_token}`
      );

      if (resp.ok) {
        const data = await resp.json();
        await ctx.runMutation(internal.metaConnections.updateToken, {
          user_id: conn.user_id,
          access_token: data.access_token,
          token_expires_at: Date.now() + (data.expires_in ?? 5184000) * 1000,
        });
      }
      // If refresh fails → token was revoked by user → mark as disconnected
    }
  },
});
```

#### LinkedIn (Refresh Token Pattern)
LinkedIn provides a `refresh_token` (valid ~365 days). Use it like Google's pattern. Set up a cron to refresh the refresh token itself before its annual expiry.

### What the User Sees

| Actual State | User Sees | System Does |
|---|---|---|
| Token valid | Green "Verbonden" | Nothing |
| Token expiring in 7 days | Green "Verbonden" (unchanged!) | Cron silently refreshes |
| Token expired but refresh works | Green "Verbonden" (unchanged!) | Auto-refresh on next API call |
| Refresh token revoked by user | "Verbinding verbroken — opnieuw verbinden" | Only case where reconnect is needed |

### Schema: Always Include Refresh Token

```typescript
// REQUIRED fields for permanent connections:
{platform}_connections: defineTable({
  // ...
  access_token: v.string(),
  refresh_token: v.optional(v.string()),  // CRITICAL for permanent connections
  token_expires_at: v.number(),
  refresh_token_expires_at: v.optional(v.number()), // For platforms with expiring refresh tokens
  last_token_refresh_at: v.optional(v.number()),    // Track when last refreshed
  // ...
})
```

### OAuth URL: Always Request Offline/Permanent Scopes

```typescript
// Google: MUST include access_type=offline
authUrl.searchParams.set("access_type", "offline");
authUrl.searchParams.set("prompt", "consent"); // Forces refresh_token even on re-auth

// LinkedIn: MUST request refresh token scope
scopes.push("r_basicprofile"); // refresh tokens auto-granted with certain scopes

// Meta: Request long-lived token exchange in callback (already in pattern)
```

## Architecture Pattern

### 1. Data Model: Per-User Connection Table

Every integration gets its own structured Convex table with user isolation.

```typescript
// convex/schema.ts
{platform}_connections: defineTable({
  // === Identity ===
  user_id: v.string(),                    // Clerk user ID — multi-tenant isolation

  // === OAuth Tokens ===
  access_token: v.string(),
  refresh_token: v.optional(v.string()),   // For platforms that support token refresh
  token_expires_at: v.number(),            // Epoch ms
  token_scope: v.optional(v.string()),     // Granted scopes for reference
  connected_user_name: v.string(),         // Display name from /me endpoint
  account_email: v.optional(v.string()),   // Email if available
  connected_at: v.number(),

  // === Selected Assets (user's final choices) ===
  // One pair per discoverable entity type:
  {entity}_id: v.optional(v.string()),
  {entity}_name: v.optional(v.string()),

  // === Discovered Assets (raw API results as JSON strings) ===
  discovered_{entities}: v.optional(v.string()),  // JSON.stringify(array)

  // === Configuration ===
  // Platform-specific toggles (e.g., capi_enabled, auto_publish)
  {feature}_enabled: v.boolean(),

  // === Setup Progress ===
  setup_status: v.string(),     // "connected" | "discovered" | "configured" | "error"
  setup_error: v.optional(v.string()),

  // === Validation ===
  validation_status: v.optional(v.string()),
  validation_message: v.optional(v.string()),
  validated_at: v.optional(v.number()),

  updated_at: v.number(),
}).index("by_user_id", ["user_id"])
```

**Rules:**
- NEVER scatter config across a generic KV store (like `ad_settings`)
- One structured table per integration = queryable, type-safe, debuggable
- `user_id` index on every table — multi-tenant from day one
- Store discovered assets as JSON strings (flexible schema for varying API responses)

### 2. OAuth Flow: Route Pattern

```
app/api/auth/{platform}/route.ts          → Initiate OAuth
app/api/auth/{platform}/callback/route.ts → Handle callback
```

#### Initiation Route

```typescript
// app/api/auth/{platform}/route.ts
export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url);
  const userId = searchParams.get("userId");
  if (!userId) return NextResponse.json({ error: "Missing userId" }, { status: 400 });

  // 1. Check env vars — NEVER ask user for app credentials
  const clientId = process.env.{PLATFORM}_CLIENT_ID;
  if (!clientId) return NextResponse.json({ error: "Not configured" }, { status: 500 });

  // 2. Build state with CSRF protection
  const state = Buffer.from(JSON.stringify({
    userId,
    platform: "{platform}",
    timestamp: Date.now(),
  })).toString("base64url");

  // 3. Set state cookie (httpOnly, 10-min expiry)
  const response = NextResponse.redirect(authUrl);
  response.cookies.set("{platform}_oauth_state", state, {
    httpOnly: true,
    secure: true,
    sameSite: "lax",
    maxAge: 600,
    path: "/",
  });

  return response;
}
```

#### Callback Route

```typescript
// app/api/auth/{platform}/callback/route.ts
export async function GET(request: NextRequest) {
  // 1. Validate state cookie matches
  // 2. Exchange code for access token
  // 3. Exchange short-lived → long-lived token (if platform supports it)
  // 4. Fetch /me for display name
  // 5. Write to {platform}_connections via Convex mutation
  // 6. Redirect to admin page with ?{platform}=connected&discovery=pending

  // CRITICAL: Also write to connection table, not just legacy KV stores
  await convex.mutation(api.{platform}Connections.upsertConnection, {
    user_id: stateData.userId,
    access_token: longLivedToken,
    token_expires_at: Date.now() + tokenExpiresIn * 1000,
    connected_user_name: userName,
  });
}
```

### 3. Auto-Discovery: Action Pattern

After OAuth completes, the system AUTOMATICALLY discovers all available assets.

```typescript
// convex/{platform}Connections.ts

export const discoverAssets = action({
  args: { user_id: v.string() },
  handler: async (ctx, args) => {
    const conn = await ctx.runQuery(internal.{...}.getByUserInternal, { user_id: args.user_id });
    if (!conn) return;

    // Check token expiry FIRST
    if (conn.token_expires_at < Date.now()) {
      await ctx.runMutation(internal.{...}.updateSetupStatus, {
        user_id: args.user_id,
        status: "error",
        error: "Token expired — reconnect required",
      });
      return;
    }

    try {
      // Discover all entity types via API
      const entities = await discoverEntitiesFromAPI(conn.access_token);

      // Save discovered assets
      await ctx.runMutation(internal.{...}.saveDiscoveredAssets, {
        user_id: args.user_id,
        // Pass all discovered data as JSON strings
        ...entities,
        // AUTO-SELECT single options (zero clicks needed)
        ...(entities.items.length === 1 && {
          auto_selected_id: entities.items[0].id,
          auto_selected_name: entities.items[0].name,
        }),
      });
    } catch (error) {
      await ctx.runMutation(internal.{...}.updateSetupStatus, {
        user_id: args.user_id,
        status: "error",
        error: error.message,
      });
    }
  },
});
```

**Auto-Selection Rules:**
- If exactly 1 option exists for an entity type → auto-select it (no user interaction needed)
- If multiple options → show as clickable list
- If zero options → show helpful message + link to create one in the platform

### 4. Discovery Hierarchy: Always Try Multiple Endpoints

APIs often have scoped endpoints (business-owned) and personal endpoints. Always cascade:

```typescript
// Example: Ad Account discovery
// 1. Try business-owned first
const bizAccounts = await fetch(`/${businessId}/owned_ad_accounts`);

// 2. If none found, fall back to personal accounts
if (bizAccounts.length === 0) {
  const personalAccounts = await fetch(`/me/adaccounts`);
  // Label them so user knows the difference
  personalAccounts.forEach(a => a.name += " (persoonlijk)");
}

// 3. Never show an empty state without trying all endpoints
```

### 5. Finalize & Sync: Backward Compatibility

When the user confirms their selections, sync to any legacy stores that existing code reads from.

```typescript
export const finalizeSetup = action({
  args: { user_id: v.string(), /* feature toggles */ },
  handler: async (ctx, args) => {
    const conn = await ctx.runQuery(/* get connection */);

    // 1. Update connection status
    await ctx.runMutation(internal.{...}.finalizeInternal, { /* ... */ });

    // 2. Sync to legacy stores (backward compat)
    // e.g., marketing_scripts for ScriptInjector, ad_settings for CAPI route
    await ctx.runMutation(internal.marketingScripts.upsertByTypeInternal, { /* ... */ });

    // 3. Trigger validation
    await ctx.runAction(internal.{...}.validate);
  },
});
```

### 6. UI Pattern: State Machine

The UI renders based on `setup_status` from the connection table.

```tsx
// React component pattern
const connection = useQuery(api.{platform}Connections.getByUser,
  user?.id ? { user_id: user.id } : "skip"
);

// State machine:
// null (loading)     → Spinner
// null (loaded)      → "Connect {Platform}" CTA button
// "connected"        → Scanning animation ("Account wordt gescand...")
// "discovered"       → Asset selectors (clickable lists) + "Activeren" button
// "configured"       → Green status cards + test button + disconnect option
// "error"            → Error message + "Opnieuw proberen" button
```

**UI Rules:**
- NEVER show manual ID input fields for things that can be discovered
- Auto-trigger discovery on OAuth redirect (detect `?platform=connected` in URL)
- Auto-migrate legacy data if old store has tokens but new table is empty
- Show connection banner with: user name, token expiry, reconnect/disconnect buttons
- Each discovered asset shows as a green card when selected, clickable list when not

### 7. Migration Pattern: Legacy Data

When replacing a data store, ALWAYS add auto-migration for existing users.

```typescript
export const migrateFromLegacy = mutation({
  args: { user_id: v.string() },
  handler: async (ctx, args) => {
    // 1. Check if already migrated
    const existing = await ctx.db.query("{platform}_connections")
      .withIndex("by_user_id", q => q.eq("user_id", args.user_id)).first();
    if (existing) return existing._id;

    // 2. Read legacy data
    const token = await readLegacyStore("access_token_key");
    if (!token) return null; // No legacy data

    // 3. Create new structured row from legacy data
    return await ctx.db.insert("{platform}_connections", { /* ... */ });
  },
});
```

**In the UI:**
```tsx
useEffect(() => {
  if (connection === null && legacyTokenExists && !migrating) {
    setMigrating(true);
    migrateFromLegacy({ user_id }).then((id) => {
      if (id) discoverAssets({ user_id }); // Re-discover after migration
    });
  }
}, [connection, legacyTokenExists]);
```

## Checklist for New Integrations

When adding a new platform integration, verify:

- [ ] OAuth route checks env vars — never asks user for app credentials
- [ ] Callback exchanges for long-lived token (if platform supports it)
- [ ] Callback writes to structured `{platform}_connections` table (not just KV store)
- [ ] Callback redirects with `?{platform}=connected` for UI to detect
- [ ] Discovery action runs automatically after OAuth
- [ ] Single options are auto-selected (zero clicks)
- [ ] Multiple options shown as clickable lists (not text input fields)
- [ ] Empty results show helpful message + link to create in platform
- [ ] Discovery cascades: business-owned → personal → manual fallback with deep link
- [ ] Finalize syncs to any legacy stores other code depends on
- [ ] Validation runs after finalize
- [ ] UI shows connection banner (green "Verbonden") — NO expiry countdown visible
- [ ] Auto-migration exists if replacing an older data store
- [ ] Error states show retry button, not just error text
- [ ] Token auto-refreshes before expiry (cron for Meta, refresh_token for Google/LinkedIn)
- [ ] `refresh_token` is stored in the connection table
- [ ] OAuth URL requests offline/permanent access (`access_type=offline`, `prompt=consent`)
- [ ] Cron job refreshes tokens days before expiry — user never sees "expired"
- [ ] Only show "reconnect" if refresh token is revoked (user action in platform settings)
- [ ] All text is in Dutch for public-facing UI (admin can be English)

## Anti-Patterns (NEVER Do These)

| Anti-Pattern | Why It's Wrong | Do This Instead |
|---|---|---|
| Manual token input field | Users don't know what tokens are | OAuth button → auto-fetch |
| Manual ID input (Pixel ID, Account ID) | Users have to find it in another dashboard | Auto-discover via API |
| "Optional" fields that skip validation | Defeats the purpose of validation | Require or auto-fill, never skip |
| Scattered KV store for config | Unqueryable, no types, no user isolation | Structured per-user table |
| Raw API error messages | Users don't understand API errors | Dutch error messages with retry action |
| Empty states with no guidance | User is stuck | Message + deep link to create the missing thing |
| Single discovery endpoint | Misses personal/shared assets | Cascade: business → personal → manual |
| No migration path | Existing users see nothing | Auto-migrate legacy data on first load |
| Showing token expiry to user | Users don't care about tokens | Auto-refresh silently, show only "Verbonden" |
| "Reconnect" button for expired tokens | Makes it the user's problem | Cron/refresh_token handles renewal automatically |
| Not requesting offline access | Short-lived tokens = broken connections | Always request `offline_access` / `access_type=offline` |
| Not storing refresh_token | Can't renew without user interaction | Always store and use refresh_token |

## Reference Implementations in This Project

| Platform | Connection Table | Discovery Action | OAuth Routes |
|---|---|---|---|
| **Meta Pixel/CAPI** | `meta_connections` | `metaConnections.discoverAssets` | `app/api/auth/meta-ads/` |
| **Google Analytics 4** | `ga_connections` | Auto-select in `saveOAuthTokens` | `app/api/auth/ga4/` |
| **Google Search Console** | `gsc_connections` | Auto-select in callback | `app/api/auth/gsc/` |
| **LinkedIn** | `social_accounts` | Direct save (no discovery needed) | `app/api/auth/linkedin/` |
| **Facebook/Instagram** | `social_accounts` | Page discovery in callback | `app/api/auth/meta/` |
