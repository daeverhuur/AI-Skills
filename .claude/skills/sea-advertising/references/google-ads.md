# Google Ads Complete Reference

> Compiled from: Darren Taylor 2025/2026, Beginners Tutorial 2026, Ultimate Tutorial 2025, Free Course 2026, Alex/Darlington Media

> **Coverage**: Video 1 (Darren Taylor 5hr course), Video 2 (Alex/Darlington Media), Video 5 (Darren Taylor 2026 update)

---

## 1. What is PPC / Google Ads

- **Pay-per-click**: you only pay when someone clicks your ad
- Sits at the **bottom of the marketing funnel** (conversion stage)
- Highly targeted, measurable, high ROAS compared to awareness channels
- **Limitation**: can only target people actively searching — cannot create latent demand
- Requires a good website to convert traffic; ads alone won't save a bad landing page

---

## 2. The Auction System & Ad Rank

Every search triggers a real-time auction between advertisers.

```
Ad Rank = Max CPC Bid × Quality Score
```

- Higher ad rank = better position, potentially **lower** cost per click
- Example: £3 bid × QS 10 = rank 30 **beats** £4 bid × QS 5 = rank 20
- Up to 4 ads at top, 4 at bottom for competitive searches
- You never pay your max bid — you pay just enough to beat the rank below you

---

## 3. Quality Score (1–10)

Three factors determine Quality Score:

| Factor | What it Measures |
|--------|-----------------|
| **Expected CTR** | How likely users will click vs. competitors (based on historical data) |
| **Ad Relevance** | How relevant your ads are to the keywords being bid on |
| **Landing Page Experience** | Mobile-friendly, fast loading, clear navigation, relevant content |

- Higher QS = cheaper clicks (it's a multiplier on your bid)
- One of the most important optimization levers in the entire system
- Target: 7+ (6 is average, 8–10 is excellent)

---

## 4. Setting Objectives & Business Metrics

Before starting any campaign, establish baseline metrics:

- Current website traffic per month
- Number of leads/sales per month
- **Website conversion rate** = conversions ÷ clicks × 100
- Lead-to-sale conversion rate
- Average order value (AOV)
- Current cost per sale (CPA)
- Break-even point for profitability

Use these to calculate your **maximum viable cost per lead** — the absolute ceiling before a campaign becomes unprofitable.

---

## 5. Conversion Rate Optimization (CRO)

**Fix your website before spending on ads.** Common improvements:

- Strong call-to-action buttons (Get a Quote, Book Now, Call Us)
- Visible contact information — phone number at top of page, click-to-call on mobile
- **Segmented service pages** — separate page per service, not one page for everything
- Bullet points and lists instead of block text paragraphs
- Contact forms on service pages (not just on a dedicated contact page)
- Clear, relevant images and visual appeal
- Easy navigation with services listed in the main menu

---

## 6. Account Setup

- Use a **Manager Account (MCC)** to avoid being forced into a Smart Campaign immediately
- Path: Google Ads Manager Account → Create new Google Ads account under it
- **NEVER** use the "Smart Campaign" account option — always choose full Google Ads account
- Manager account lets you manage multiple client accounts (essential for agencies/freelancers)
- Add billing details later, after research phase is complete

---

## 7. Campaign Structure

```
Account
  └── Campaign          ← budget level, geo/device targeting settings
        └── Ad Group    ← themed keyword groupings
              ├── Keywords    ← what triggers your ads
              └── Ads         ← what users see
```

- **One campaign per service area or business objective**
- **Multiple ad groups per campaign** — each themed by keyword intent
- Each ad group: tightly themed keywords + ad copy relevant to those keywords
- 8–12 ad groups per campaign is considered highly segmented and effective

---

## 8. Keyword Research

### Using Keyword Planner

1. Start with "Discover new keywords"
2. Enter seed keywords (your core service terms)
3. Use Google's filters: brand vs. non-brand, services, locations, etc.
4. Download full keyword list as CSV for offline refinement

### Refinement Process

```
Keyword Planner output:  ~1,000+ keywords
After Google filters:    ~700 keywords
After manual review:     ~150 keywords (remove irrelevant, competitor names, wrong services)
After grouping:          8–12 themed ad groups
```

### Grouping Keywords into Ad Groups

Group by theme and intent:

| Theme Examples | Description |
|----------------|-------------|
| Generic service | Core terms (e.g. "boiler repair") |
| Brand names | Branded searches for your business |
| Emergency | Urgent intent (e.g. "24 hour boiler repair") |
| Cost / price | Commercial intent (e.g. "boiler repair cost") |
| Local / near me | Geo-intent (e.g. "boiler repair London") |
| Service plans | Subscription/recurring intent |

- Don't over-segment — single keyword ad groups are no longer effective due to close variants
- If a keyword fits multiple groups, choose based on conversion potential
- Each ad group's copy must be relevant to its keywords

---

## 9. Keyword Match Types

### Broad Match *(no special characters)*

- Default setting — shows for any search Google deems "relevant"
- **HIGHEST volume, LOWEST quality**
- Can match to completely irrelevant searches
- Google pushes broad match for automation reasons — treat with skepticism
- **Expert consensus: DO NOT start campaigns with broad match**
- Only test after campaign is already performing well with other match types

### Exact Match *[square brackets]*

```
Keyword: [boiler repair]
```

- Most restrictive and targeted
- Since 2015: includes "close variants" (plurals, slight spelling variations)
- **LOWEST volume, HIGHEST quality traffic**
- Always include exact match variants in every campaign

### Phrase Match *"double quotes"*

```
Keyword: "boiler repair"
```

- **Best balance of volume and accuracy** — recommended starting point
- User's search must contain the keyword phrase in similar order
- Also includes close variants since 2015
- Word order no longer strictly enforced

### Negative Match

- Blocks your ads from showing for specific searches
- Can apply broad, phrase, or exact match logic to negatives
- Use **exact match negatives** for competitor names (avoids blocking positive related terms)
- Use **broad match negatives** for completely irrelevant categories (e.g. "oil" if you do gas boilers)

### Expert Recommendation

> **Start with Phrase Match + Exact Match only. Never start with Broad Match.**
> Build your negative keyword list before launch. Ignore Google reps who push broad match.

---

## 10. Negative Keywords

### Finding Negatives Before Launch

- Review all keywords in Keyword Planner results
- Look for: competitor names, irrelevant services, wrong product types, DIY intent
- Download the full list and manually comb through for exclusion candidates
- Use Google's refinement filters to surface categories to exclude in bulk

### Ongoing Negative Keyword Management

- Check **Search Terms Report** weekly
- Block irrelevant searches that triggered your ads
- Add as exact/phrase/broad negatives as appropriate
- Create **Negative Keyword Lists** — these can be shared across multiple campaigns

---

## 11. Text Ads (Responsive Search Ads)

### Components

| Element | Limit | Notes |
|---------|-------|-------|
| Headlines | 15 max | 30 characters each |
| Descriptions | 4 max | 90 characters each |
| Display URL paths | 2 | 15 characters each |
| Final URL | 1 | Actual landing page URL |

Google tests combinations and automatically serves best-performing variants.

### Writing Effective Ads

- Include a strong **call-to-action** (Get a Quote, Book Now, Call Today)
- Include keywords in headlines for relevance
- Highlight USPs clearly
- Include numbers/stats (20+ years experience, 5-star rated, 500+ jobs completed)
- Use emotional triggers and urgency where appropriate
- Include pricing if competitive
- Write headlines across different themes:
  - Keyword-matching headlines
  - Benefit-focused headlines
  - CTA-focused headlines
- **Pin** important headlines to specific positions when sequence matters

### Ad Strength

- Google rates: Poor → Average → Good → Excellent
- Target "Good" or "Excellent"
- Add diverse headlines covering different angles to improve score
- More unique, non-overlapping headlines = better ad strength rating

---

## 12. Ad Extensions / Assets

Always set up ALL relevant extensions. They improve CTR, occupy more screen real estate, and improve Quality Score.

| Extension Type | Use For |
|----------------|---------|
| **Sitelinks** | Additional links below ad (add 4–6) |
| **Callouts** | Short highlights (Free quotes, 24/7 service, 10-year guarantee) |
| **Structured Snippets** | Predefined categories (Services: Boiler Repair, Installation...) |
| **Call Extension** | Phone number directly in the ad |
| **Location Extension** | Business address and map pin |
| **Price Extension** | Show pricing for specific services or products |
| **Promotion Extension** | Special offers with date ranges |
| **Image Extension** | Visual additions to text ads |

---

## 13. Bidding Strategies

### Manual Bidding

| Strategy | Description |
|----------|-------------|
| **Manual CPC** | Set your own bids per keyword — full control |
| **Enhanced CPC** | You set base bids, Google adjusts ±30% for likely converters |

Good for the learning phase when you don't yet have conversion data.

### Smart Bidding (Automated)

| Strategy | Optimizes For |
|----------|---------------|
| **Maximize Clicks** | Most clicks within budget (good for starting) |
| **Maximize Conversions** | Most conversions within budget |
| **Maximize Conversion Value** | Revenue, not just conversion count |
| **Target CPA** | Set target cost per acquisition |
| **Target ROAS** | Set target return on ad spend |
| **Target Impression Share** | Visibility (best for brand campaigns) |

### Bidding Strategy Progression

```
Phase 1 (0–30 conversions):  Manual CPC or Maximize Clicks
Phase 2 (30+ conversions):   Switch to Target CPA or Maximize Conversions
Phase 3 (consistent data):   Test Target ROAS for revenue optimization
```

**Minimum threshold**: 30–50 conversions per month before smart bidding strategies work reliably. Below this, automation doesn't have enough signal.

---

## 14. Conversion Tracking

### Setup Options

- Google Ads conversion tag (via Google Tag Manager — recommended)
- Import from Google Analytics 4
- Enhanced conversions (first-party data matching)
- Offline conversion import (for lead-to-sale tracking)

### Key Conversions to Track

- Form submissions
- Phone calls (call tracking via forwarding number)
- Purchases / transactions (eCommerce)
- Key page views (e.g., Thank You page after form submit)
- Click-to-call on mobile

### Attribution Models

| Model | Description |
|-------|-------------|
| **Data-driven** | Recommended — uses ML to assign credit across touchpoints |
| **Last-click** | Default, simple, but incomplete picture |
| First-click, linear, time-decay | Being deprecated by Google |

> **Never launch a campaign without verified conversion tracking.**

---

## 15. Campaign Types

### Search Campaigns

- Text ads on search results pages
- **Highest intent** — people actively searching for your service
- Best for direct response and lead generation
- **Start here first** before any other campaign type

### Display Campaigns

- Banner/image ads across Google Display Network (GDN)
- 2M+ websites, apps, YouTube
- Good for brand awareness and remarketing
- Lower intent than search, lower CPC
- Best use: retargeting website visitors

### Shopping Campaigns

- Product listings with image, price, and store name
- Requires Google Merchant Center + product feed
- Great for eCommerce
- Product feed quality is critical to performance

### Performance Max (PMax)

- Runs across ALL Google channels simultaneously (Search, Display, YouTube, Gmail, Discover, Maps)
- Uses AI to optimize across channels
- Requires **asset groups**: headlines, descriptions, images, videos
- Uses **audience signals** (not targeting) as hints for the algorithm
- Good complement to existing Search campaigns
- Can cannibalize existing campaigns — monitor carefully
- Give it **4–6 weeks** to complete the learning period before evaluating

### YouTube / Video Campaigns

- Video ads on YouTube and video partner sites
- Formats: skippable in-stream, non-skippable, bumper ads, in-feed
- Good for awareness and remarketing
- Targeting options: keywords, topics, placements, audiences, demographics

### Discovery / Demand Gen Campaigns

- Visual ads in Google Discover, YouTube, Gmail
- More awareness-focused than direct response
- Uses audience targeting over keyword targeting
- Good for upper-funnel marketing and reaching new audiences

---

## 16. Remarketing / Retargeting

- Show ads to people who previously visited your website
- Requires remarketing pixel/tag on website
- **Audience list types**:
  - All website visitors
  - Visitors to specific pages
  - Cart abandoners
  - Converters (to exclude or cross-sell)
- **RLSA** (Remarketing Lists for Search Ads): adjust bids for returning searchers
- **Dynamic remarketing**: show specific products/services a user viewed
- Membership duration: 30–540 days (typically 30–90 days for most businesses)

Remarketing typically delivers **higher conversion rates and lower CPA** than cold traffic.

---

## 17. Audiences

| Audience Type | Description |
|---------------|-------------|
| **In-Market** | Actively researching/comparing — highest purchase intent |
| **Affinity** | Specific interests or lifestyles — good for awareness |
| **Custom Segments** | Your own audiences based on URLs/keywords/apps |
| **Customer Match** | Upload customer email lists for targeting |
| **Demographics** | Age, gender, household income, parental status |

**Best practice**: Add audiences in **observation mode** first to gather data, then switch to **targeting** if performance data warrants it.

---

## 18. Budget Management

- Set **daily budgets** at campaign level
- Google may spend up to **2× daily budget** on high-opportunity days
- Monthly spend won't exceed daily budget × 30.4
- Start conservative, scale based on performance data
- **Shared budgets** available for campaigns with similar priorities
- Google spreads spend throughout the day by default (standard delivery)

**Starting point for most local service industries**: £20–50/day for testing

---

## 19. Optimization Tactics

### Weekly Tasks

- Review **Search Terms Report** → add new negative keywords
- Check **Quality Scores** → investigate and improve keywords below 6
- Review **ad performance** → pause consistently underperforming ad variants
- Monitor **budget pacing** — are you hitting daily limits? Is spend too low?

### Monthly Tasks

- A/B test new ad copy variants
- Review conversion data → adjust bids and budget allocation
- Review **audience performance** data
- Assess competitor landscape
- Adjust **geographic** and **device bid modifiers** based on performance data

### Ongoing

- Add new negative keywords as search terms reveal new patterns
- Test new keyword variations
- Improve landing pages based on Quality Score feedback
- Monitor **cost per conversion** trends — flag deterioration early

---

## 20. Common Mistakes

1. **Starting with broad match keywords** — wastes budget on irrelevant traffic
2. **Not setting up conversion tracking before launch** — flying blind from day one
3. **Not doing negative keyword research** — irrelevant clicks burn budget
4. **Sending all traffic to the homepage** — use specific landing pages per service
5. **Not optimizing the website first** — ads can't fix a low-converting website
6. **Ignoring Quality Score** — leaving cheaper clicks on the table
7. **Setting and forgetting** — campaigns require ongoing weekly/monthly optimization
8. **Following Google Ads rep recommendations blindly** — they optimize for Google's revenue
9. **Using Smart Campaigns instead of full Google Ads** — loss of control and visibility
10. **Not segmenting keywords into themed ad groups** — poor ad relevance, lower CTR
11. **Budget too small relative to CPC costs** — can't gather meaningful data
12. **Not understanding business metrics** — can't calculate profitability without CPA, AOV, conversion rate

---

## 21. Account Audit Checklist

### Tracking & Measurement
- [ ] Conversion tracking set up and verified working?
- [ ] Attribution model appropriate (data-driven recommended)?
- [ ] Call tracking configured?

### Keywords & Targeting
- [ ] Quality Scores above 6 for main keywords?
- [ ] Search Terms Report reviewed — irrelevant queries blocked?
- [ ] Negative keyword list comprehensive?
- [ ] No broad match keywords (especially in early campaigns)?
- [ ] Geographic targeting correct and precise?

### Ads & Assets
- [ ] Ad copy relevant to keywords in each ad group?
- [ ] Ad strength "Good" or "Excellent"?
- [ ] All relevant ad extensions set up (sitelinks, callouts, structured snippets, call)?

### Landing Pages
- [ ] Landing pages relevant to ad copy and keywords?
- [ ] Mobile experience tested and functional?
- [ ] CTA buttons visible and compelling?
- [ ] Contact forms accessible (not just on contact page)?

### Bidding & Budget
- [ ] Bidding strategy appropriate for current data volume?
- [ ] Budget allocation aligned with performance data?
- [ ] Device bid adjustments reviewed?
- [ ] Ad schedule/dayparting considered?

### Campaign Structure
- [ ] Campaign structure logical — not too broad, not too granular?
- [ ] Audience lists active and properly segmented?
- [ ] Remarketing audiences configured?

---

## 22. Dynamic Keyword Insertion & Ad Customizers

### Dynamic Keyword Insertion (DKI)

```
Syntax: {KeyWord:Default Text}
```

- Automatically inserts the user's search query into your ad headline/description
- Capitalizes based on the `KeyWord` vs `keyword` vs `KEYWORD` syntax variant
- `{KeyWord:Boiler Repair}` → shows search term with title case; fallback = "Boiler Repair"
- Makes ads feel hyper-relevant to searchers
- **Risk**: can insert inappropriate or irrelevant terms — monitor search terms closely when using DKI

### Dynamic Location Insertion

```
Syntax: {LOCATION(City):Default City}
```

- Automatically inserts the user's detected city into the ad
- Great for service businesses covering multiple locations without separate campaigns
- Fallback text shown when location cannot be detected

### IF Functions

```
Syntax: {=IF(device=mobile,"Call Now","Get a Quote")}
```

- Show different ad text based on device type or audience membership
- Useful for mobile-specific CTAs (call vs. form)

---

## 23. Ad Rotation & Testing

- Google tests RSA headline/description combinations automatically
- **Optimized rotation** (default): Google serves best-performing combinations more often
- **Even rotation**: For A/B testing when you want equal distribution
- Pin headlines to specific positions (1, 2, 3) when order matters — but pinning reduces Google's optimization ability
- Pinned positions reduce ad strength rating — only pin when absolutely necessary (legal disclaimers, brand names)
- **A/B ad testing best practice** (Alex/Darlington): Create 2–3 RSA variations per ad group; pause the weakest after 30+ days

---

## 24. Search Terms Report (Deep Dive)

The Search Terms Report is the most important optimization tool in Google Ads.

### How to Access

- Reports → Search terms (or Keywords → Search terms tab)
- Shows every actual query that triggered your ads

### What to Look For

| Signal | Action |
|--------|--------|
| High impressions, 0 clicks | Low relevance — add as negative or improve ad copy |
| Clicks but no conversions | Poor landing page fit — investigate or exclude |
| Good conversions, not a keyword yet | Add as explicit keyword to bid on |
| Irrelevant intent | Add as negative keyword immediately |
| Competitor brand name | Decide: bid on competitor terms or exclude? |

### Workflow

```
Weekly: Export → Sort by cost → Negative any irrelevant → Add new positives
Monthly: Full review for patterns → Update match types → Refresh ad groups
```

### Close Variant Problem

- Google shows "close variants" even for exact match keywords
- You may appear for plurals, synonyms, related searches you didn't target
- Search Terms Report catches these — essential for controlling who you reach

---

## 25. Ad Extensions — Extended Detail

### Sitelinks
- **Minimum**: 4 sitelinks recommended
- Add description lines (2 × 35 chars) for expanded sitelinks
- Examples: "About Us", "Our Services", "Customer Reviews", "Emergency Callout"
- Link to relevant subpages, not just the homepage
- Enable at account, campaign, or ad group level

### Callout Extensions
- Short snippets (25 chars each), not clickable
- Minimum 4, aim for 8–10
- Examples: "Free Quotes", "Same Day Service", "10-Year Guarantee", "5-Star Rated", "No Call-Out Charges"
- Focus on USPs that aren't in the ad copy itself

### Structured Snippets
- Pick a category header (Services, Types, Brands, Models, etc.)
- List items below the header
- Example: Services: Boiler Repair, Boiler Installation, Annual Servicing, Power Flushing
- Minimum 3 values, aim for 6+

### Call Extension
- Adds a clickable phone number to the ad
- On mobile: tapping the number counts as a phone call conversion
- Enable call reporting for tracking
- Set business hours to only show when you can answer

### Location Extension
- Requires Google Business Profile linked to Google Ads
- Shows address, map, distance from searcher
- Especially important for local businesses
- Boosts quality score through geographic relevance signals

### Price Extensions
- Show prices for specific services or products
- Good for businesses with defined service packages
- Format: Service name + brief description + starting price
- Disqualifies users who can't afford your pricing (filters out low-quality leads)

### Promotion Extensions
- Highlight sales and offers with start/end dates
- Automatically stops showing after end date
- Include promo code option

### Lead Form Extensions
- Collect leads directly from the SERP without sending users to your website
- Useful for high-volume, competitive markets
- Lower intent than website form completions — treat as top-of-funnel leads
- Download leads via CSV or integrate with CRM

### Image Extensions
- Add lifestyle/product images to text ads
- Makes ads visually richer on desktop
- Use high-quality, relevant images (minimum 300×300px, recommended 1200×628px)

### Extension Strategy by Business Type

| Business Type | Priority Extensions |
|---------------|---------------------|
| Local service | Call, Location, Sitelinks, Callouts |
| eCommerce | Price, Promotion, Image, Sitelinks |
| Lead gen B2B | Sitelinks, Callouts, Structured Snippets, Lead Form |
| SaaS/software | Sitelinks, Callouts, Structured Snippets |

---

## 26. Smart Bidding — In-Depth Analysis

### Manual CPC (Darren Taylor 2026 perspective)

- Full control: you set every keyword bid individually
- Start by matching bids to Quality Score — high QS keywords can bid lower for same position
- Historical note: Marin Software (major bid management SaaS) effectively went bankrupt when Google released Smart Bidding — automated bidding has become genuinely very good
- Manual CPC still valuable when:
  - Campaign is new and lacks conversion data
  - Very low conversion volume (< 30/month)
  - You have unique insights about your market that automation doesn't have

### Enhanced CPC (ECPC)
- Base: your manual bids
- Google adjusts ±30% when it predicts a conversion is more/less likely
- Bridge between manual and fully automated
- Good transitional strategy when moving from manual to smart bidding

### Target CPA
- You set a target cost per acquisition
- Google spends more on searches it predicts will convert at or below your CPA target
- Requires minimum 30 conversions in past 30 days to function reliably
- Set initial target 20–30% higher than your actual target — gives algorithm room to learn
- Reduce target gradually (10–15% increments) as performance stabilizes

### Target ROAS
- You set a target return on ad spend (e.g., 400% = £4 revenue per £1 spent)
- Best for eCommerce where conversion values vary
- Requires minimum 50 conversions/month with value data
- More restrictive than Target CPA — only suitable for mature campaigns

### Maximize Conversions
- Spends full budget to maximize conversion count
- No CPA target — algorithm prioritizes volume over efficiency
- Best when: you want to spend a fixed budget, don't care about CPA yet
- Risk: can spend budget on low-quality conversions to hit volume

### Maximize Conversion Value
- Prioritizes high-value conversions over conversion count
- Best for eCommerce with varying order values
- May get fewer conversions but higher total revenue

### Maximize Clicks
- Optimizes for click volume within budget
- Good for brand campaigns where you want presence
- Not for direct response — no connection to conversions

### Target Impression Share
- Sets a target percentage of auctions where your ad should appear
- Use for brand campaigns (aim for 90%+ impression share on brand terms)
- Not for generic terms — too expensive and irrelevant

### Smart Bidding Learning Period

```
Changes that reset learning period:
- Switching bidding strategy
- Significant budget changes (±20%)
- Major keyword additions/removals
- Significant ad copy changes

Duration:
- Standard: 2 weeks
- Performance Max: 4–6 weeks
- Target ROAS: up to 6 weeks for complex accounts
```

- **Observation window**: Monitor cost per conversion trend over 30 days before judging smart bidding performance
- Never make major changes during learning period — disrupts the algorithm

---

## 27. AI-Assisted Ad Copywriting (ChatGPT Project Method)

*From Darren Taylor's 2026 updated course*

### The ChatGPT Project Approach

Instead of one-off prompts, create a dedicated **ChatGPT Project** for each client or campaign. This preserves context across all copywriting sessions.

**What to include in the project system prompt:**

```
Business name: [Name]
Industry: [Industry]
Location: [City/Region]
Target audience: [Demographics + psychographics]
USPs: [3–5 key differentiators]
Tone of voice: [Formal/casual/friendly/etc.]
Competitor context: [What competitors claim]
Price position: [Budget/mid-market/premium]
Brand guidelines: [Any restrictions]
```

### Prompt Templates for RSA Copy

**Full ad set generation:**
```
Write 15 Google Ads headlines (max 30 chars each) and 4 descriptions
(max 90 chars each) for [business] targeting [service keyword].

USPs: [list]
CTA: [desired action]
Tone: [tone]

Group headlines into themes:
- Keyword-matching (3–5)
- Benefit-focused (3–5)
- CTA-focused (3–5)
- Social proof (2–3)
- Urgency (1–2)
```

**Refinement prompt:**
```
Improve these headlines: [paste headlines]
Issues: [too generic / no urgency / doesn't highlight USP X]
Constraints: max 30 chars, include [keyword]
```

### Character Count Verification

Always verify headline/description lengths before uploading. ChatGPT sometimes miscounts — especially with special characters.

Use this verification prompt:
```
Count the exact character length of each headline and flag any
that exceed 30 characters. List each headline with its character count.
```

### Competitor-Informed Copywriting

```
Here are 5 competitor ads in [industry]: [paste ad text]
Write 15 headlines that differentiate from these competitors
and address gaps they're not addressing.
```

---

## 28. Campaign Setup Walkthrough — Step by Step

### Pre-Campaign Checklist

```
□ Google Ads account created (via Manager Account)
□ Billing set up
□ Conversion tracking verified (green checkmark in Google Ads)
□ GA4 linked to Google Ads
□ Google Business Profile linked (for Location extension)
□ Keyword research completed (phrase + exact match identified)
□ Negative keyword list prepared
□ Landing pages reviewed/optimized for CRO
□ Ad copy written (15 headlines, 4 descriptions per ad group)
□ Extensions prepared (sitelinks, callouts, structured snippets, call, location)
```

### Campaign Settings — Critical Choices

| Setting | Recommended Option | Why |
|---------|-------------------|-----|
| Campaign goal | Leads / Sales | Not "Brand awareness" unless that's genuinely your goal |
| Campaign type | Search | Start here; avoid PMax for first campaign |
| Bidding | Manual CPC or Maximize Clicks | For campaigns without conversion history |
| Networks | Search Network ONLY | Uncheck "Display Network" and "Search Partners" initially |
| Locations | Specific city/region | NOT entire country unless you operate nationally |
| Language | Target language + English | Users often search in English even in non-English countries |
| Ad schedule | Business hours initially | Refine with dayparting data after 30+ days |
| Dynamic search ads | OFF | Not recommended for new accounts |
| Auto-apply recommendations | OFF | Google's recommendations optimize for spend, not your ROI |

### Search Partners — The Decision

- Search Partners = Bing, Yahoo, other search sites that use Google's ad network
- Often cheaper than Google Search but typically lower intent/conversion rate
- **Best practice**: Start with Search Network only. After 90 days, run a Search Partners segment report. If CPA is comparable, turn on Search Partners for incremental volume.

### Location Targeting — Advanced

```
Targeting options:
1. People IN your location (recommended for local businesses)
2. People searching for your location (for tourism/e-commerce)
3. Both (default — often too broad for local businesses)
```

- Use option 1 for local service businesses
- Layer with location bid adjustments once you have 30+ days of data

---

## 29. Google Shopping Campaigns

*For eCommerce businesses only*

### Requirements

1. Google Merchant Center account
2. Product feed (uploaded to Merchant Center)
3. Website verified in Merchant Center
4. Feed linked to Google Ads account

### Product Feed Essentials

| Attribute | Description | Optimization Tip |
|-----------|-------------|------------------|
| `id` | Unique product identifier | Keep consistent with website SKU |
| `title` | Product name | Include key search terms naturally |
| `description` | Product description | Rich with relevant keywords |
| `google_product_category` | Google taxonomy category | Be as specific as possible |
| `image_link` | Product image URL | High quality, white background |
| `price` | Current price | Must match website exactly |
| `availability` | in_stock / out_of_stock | Update in real-time |

### Shopping Campaign Structure

```
Campaign: Shopping [Product Category]
  Ad Group: All Products (or by category)
    Product Groups: Subdivide by brand → product type → item
```

- Start with one campaign, all products
- Subdivide into campaigns by margin/product category as you scale
- **Use negative keywords** — Shopping campaigns can trigger for unrelated searches

### Product Listing Optimization

- Product **title** is the most important ranking factor in Shopping
- Include: Brand + Product type + Key attribute + Size/Color if relevant
- Images with clean white backgrounds outperform lifestyle shots for CTR
- Price competitiveness directly impacts impression share

---

## 30. Performance Max (PMax) — Advanced Guide

### What PMax Is

- Runs across: Search, Display, Shopping, YouTube, Gmail, Discover, Maps
- Single campaign replaces multiple channel-specific campaigns
- Uses AI to decide when/where/how to show ads

### Asset Groups

Each PMax campaign uses Asset Groups:

```
Asset Group = themed collection of:
- 3–5 images
- 1–5 logos
- 1–5 videos (or Google generates one)
- Up to 15 headlines
- Up to 5 long headlines (90 chars)
- Up to 5 descriptions
- Final URL
```

Create separate asset groups for different product/service themes.

### Audience Signals

- NOT targeting (PMax targets broadly regardless)
- "Signals" are hints to help the algorithm start learning faster
- Use: Custom intent audiences, Customer Match lists, In-market segments
- The algorithm may completely ignore signals if it finds better-performing audiences

### PMax Cannibalization Risk

- PMax can steal traffic from existing Search campaigns
- Search campaigns get priority when the same query matches both
- Monitor Search campaign performance closely after adding PMax

### When to Use PMax

- After existing Search campaigns are profitable and stable
- When you want to expand reach beyond search
- For eCommerce where Shopping + Search + Display all matter
- NOT as a replacement for a well-structured Search campaign

### PMax Limitations

- Very limited visibility into what's working (opaque reporting)
- Minimal control compared to Search campaigns
- Cannot exclude specific placements easily
- Videos are auto-generated if you don't provide them — often low quality

---

## 31. RLSA — Remarketing Lists for Search Ads

### What It Is

- Apply audience lists to Search campaigns
- When a user on your remarketing list searches, you can:
  - Bid higher (bid adjustment %)
  - Show different ad copy
  - Lower bids (if poor conversion history)

### Setup

```
Audience Manager → Remarketing → Create new list → Website visitors
Apply to campaign → Observation mode first → Analyze → Adjust bids
```

### Common RLSA Strategies

| Audience | Strategy |
|----------|----------|
| Homepage visitors | +20% bid adjustment (showed interest) |
| Product page visitors | +50% bid adjustment (high intent) |
| Cart abandoners | +100% bid adjustment (very high intent, different ad copy) |
| Past converters | -100% (exclude from lead gen) OR +50% (include for repeat purchase) |
| Existing customers | Separate campaign with loyalty messaging |

### Observation vs. Targeting Mode

- **Observation**: Audience data collected, bids adjusted, but non-audience users still see ads
- **Targeting**: ONLY audience members see your ads (highly restrictive)
- Always start with Observation; switch to Targeting only for dedicated remarketing campaigns

---

## 32. Reporting & Key Metrics

### Core Metrics

| Metric | Formula | Good Range |
|--------|---------|-----------|
| CTR | Clicks ÷ Impressions × 100 | 3–5% (search), 0.3–0.5% (display) |
| CPC | Cost ÷ Clicks | Varies by industry |
| Conversion Rate | Conversions ÷ Clicks × 100 | 2–5% typical |
| Cost per Conversion | Cost ÷ Conversions | Must be below your max CPA |
| ROAS | Revenue ÷ Ad Spend × 100 | Target varies (200–500% common) |
| Quality Score | 1–10 (per keyword) | Aim for 7+ |
| Impression Share | Impressions ÷ Eligible Impressions | 60–80% is healthy |

### Impression Share Insights

```
Impression Share Lost (Budget): Lost due to insufficient budget
Impression Share Lost (Rank):   Lost due to low Ad Rank (QS or bid)
```

- High budget loss → increase daily budget
- High rank loss → improve Quality Score or increase bids

### Segment Reports

Always segment data to find performance patterns:

```
Segment by → Device:    Compare mobile vs. desktop vs. tablet CPA
Segment by → Day of week: Identify best/worst days for conversions
Segment by → Hour of day: Find peak conversion hours for dayparting
Segment by → Location:  Find best-performing cities or regions
```

### Dashboard Setup Best Practice

Create a custom column set for daily monitoring:
```
Impressions | Clicks | CTR | Avg. CPC | Conversions | Conv. Rate | Cost/Conv | ROAS
```

---

## 33. Account Structure Philosophies

### Themed Ad Groups (Darren Taylor — Recommended 2025+)

```
Campaign: Boiler Services London
  Ad Group: Boiler Repair          ← generic repair searches
  Ad Group: Emergency Boiler Repair ← urgent/immediate intent
  Ad Group: Boiler Installation     ← replacement intent
  Ad Group: Boiler Servicing        ← maintenance intent
  Ad Group: Boiler Repair Cost      ← price-research intent
  Ad Group: Boiler Repair Near Me   ← local/geo intent
```

- 8–12 ad groups per campaign for high segmentation
- Each ad group: 5–15 themed keywords + 2–3 RSAs
- Modern Google close variants mean ultra-granular segmentation is less beneficial

### SKAGs — Single Keyword Ad Groups (Alex/Darlington — Historical)

```
Campaign: Boiler Repair
  Ad Group: [boiler repair]         ← exact match
  Ad Group: "boiler repair"         ← phrase match
  Ad Group: boiler repair           ← broad match (optional, separate)
```

**SKAG Pros**: Maximum relevance, precise bid control, easy to track performance per keyword
**SKAG Cons**: Extremely high maintenance, less effective since close variants (2019+), not scalable for large accounts

**Current consensus (2025)**: Themed ad groups outperform SKAGs due to close variant matching — Google now treats similar keywords identically anyway. The extra segmentation work provides diminishing returns.

### Frankenstein Ad Groups (Anti-Pattern)

Named by Alex/Darlington to describe what NOT to do:

```
Ad Group: ALL SERVICES (terrible structure)
  Keywords: boiler repair, plumber, bathroom fitting,
            emergency plumber, heating engineer...
  Ads: Generic copy that can't be relevant to all keywords
```

- Result: Low Quality Scores across all keywords
- Result: Irrelevant ad copy → low CTR → expensive clicks
- **Always avoid: never put unrelated keywords in the same ad group**

---

## 34. Geographic Targeting Strategy

### Radius Targeting

- Target by radius around a specific postcode/address
- Better than city targeting for local service businesses
- Common radii: 10, 20, 30 miles depending on service area

### Location Bid Adjustments

After 30+ days of data:
```
Find: Which cities/boroughs convert best?
Apply: +20–50% bid adjustment to high-converting locations
Apply: -20–50% bid adjustment to poor-converting locations
Exclude: Locations with no conversions after 30+ clicks
```

### Postcode Exclusions

- Exclude postal codes/areas you don't serve
- More precise than negative radius targeting
- Important for businesses with specific service boundaries

---

## 35. Device Bid Adjustments

```
Find: Reports → Segment by device
Compare: CPA on mobile vs. desktop vs. tablet
Apply: Bid adjustments based on relative performance

Example:
Desktop CPA: £40 (benchmark)
Mobile CPA:  £70 → Apply -30% mobile bid adjustment
Tablet CPA:  £90 → Apply -50% tablet bid adjustment
```

- Mobile typically has lower conversion rates for complex B2B/service purchases
- Mobile typically converts better for emergency/immediate-need services
- Always check your data — don't assume mobile is worse

---

## 36. Ad Schedule / Dayparting

### Default

- Ads run 24/7 unless restricted

### When to Restrict

- Service businesses: Restrict to business hours if you can't take enquiries overnight
- Risk: Overnight leads from a competitor's form could still win — consider keeping ads on with lower bids

### Hour-of-Day Segmentation

After 90 days of data:
```
Reports → Time → Hour of day
Find: Which hours produce lowest CPA?
Apply: +bid adjustment for peak hours
Apply: -bid adjustment or pause for low-conversion hours
```

---

## 37. Patterns & Recurring Themes

### Universal Advice Across All Sources

| Principle | Detail |
|-----------|--------|
| **Research first** | Never launch without keyword research, negative planning, and understanding your business metrics |
| **Quality over quantity** | Fewer, highly relevant keywords outperform thousands of broad keywords |
| **Website first** | Fix CRO before spending on ads — ads amplify what's already there |
| **Phrase + Exact only** | Every experienced instructor advises against starting with broad match |
| **Ignore Google reps** | Their recommendations typically increase spend without improving performance |
| **Test and iterate** | Never set and forget — weekly and monthly optimization is non-negotiable |
| **Track everything** | Without conversion tracking, optimization is impossible |
| **Relevance chain** | Keyword → Ad Copy → Landing Page must be aligned at every step |
| **Automation is good** | Smart bidding has matured — embrace it when you have sufficient data |
| **AI for copywriting** | Use ChatGPT Projects (persistent context) for efficient, consistent ad copy generation |

### Key Benchmarks

| Metric | Benchmark |
|--------|-----------|
| Quality Score | Aim for 7+ (6 = average, 8–10 = excellent) |
| CTR (search) | 3–5% average, 8%+ is excellent |
| Conversion rate | 2–5% typical (varies by industry) |
| Smart bidding minimum | 30 conversions/month (50+ for Target ROAS) |
| Learning period | 2–4 weeks before major changes (PMax: 4–6 weeks) |
| Starting budget | £20–50/day for most local industries |
| Impression share | 60–80% healthy for non-brand; 90%+ for brand terms |
| Ad strength | Target "Good" or "Excellent" on all RSAs |

### Evolution of Best Practices (2019–2026)

| Practice | Old Advice | Current Advice |
|----------|-----------|----------------|
| Keyword match types | SKAGs with exact match | Themed groups with phrase + exact |
| Bidding | Manual CPC preferred | Smart bidding after 30+ conversions |
| Ad format | ETAs (3 headlines, 2 desc) | RSAs only (15 headlines, 4 desc) |
| Broad match | Never use | Test carefully only in mature accounts |
| Attribution | Last-click | Data-driven (DDA) |
| Extensions | Optional | Mandatory — all relevant types |

### The Relevance Chain (Core Principle)

```
Search Query
    ↓ (match)
Keyword → Ad Group
    ↓ (match)
Ad Copy (headline + description)
    ↓ (click)
Landing Page (relevant, fast, CTA-optimized)
    ↓ (convert)
Conversion Tracking → Google Ads signal → Better automation
```

Every link in this chain must be tightly aligned. A weak link degrades the whole chain.

### The Automation Transition Mindset

- Pre-2019: Manual management was the competitive advantage
- 2019–2022: Smart bidding emerged as genuinely superior for high-volume accounts
- 2023–2026: Automation is the default; human expertise is in setup, structure, and strategy
- **Your edge now**: Better keyword research, better copy, better landing pages, better structure — not manual bid adjustments
- Historical note (Darren Taylor): Marin Software — major bid management SaaS — effectively went bankrupt when Smart Bidding launched; automated bidding is that good now

### Agency/Freelancer Notes (from Alex/Darlington Media)

- Structure campaigns to be auditable — clients need to understand what you're doing
- Keep campaign names descriptive: `[Location] [Service] [Match Type] [Date]`
- Document optimization decisions — clients ask "why did you do this?"
- Charge based on percentage of ad spend (10–20%) OR flat management fee, not results
- Set realistic expectations: most campaigns need 90 days to mature and optimize

### The Golden Rule

> **Relevance is everything.**
>
> The entire Google Ads system rewards relevance at every level: relevant keywords earn better Quality Scores, relevant ads earn higher CTRs, relevant landing pages earn better conversion rates. Every optimization decision should start with the question: *"Is this relevant to what the user is searching for?"*
