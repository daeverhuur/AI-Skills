---
name: seo-aeo-auditor
description: "SEO and AEO (Answer Engine Optimization) auditing, page strategy, and content generation toolkit. Use when the user asks to: (1) Audit a page, section, or site for SEO performance, (2) Improve SEO scores or fix SEO issues, (3) Suggest new SEO pages or content areas for their app/site, (4) Generate or manage SEO pages via JSON, (5) Optimize content for AI answer engines, voice search, or featured snippets, (6) Create FAQ pages, schema markup, or structured data, (7) Plan content pillars, topic clusters, or keyword strategies, (8) Anything related to search engine optimization, search rankings, organic traffic, meta tags, keywords, backlinks, or AEO."
---

# SEO/AEO Auditor

Audit pages for SEO performance, suggest content strategies, and manage SEO pages through a JSON registry.

## Three Core Workflows

### 1. SEO Audit (Section/Page Analysis)

Audit a user-specified page or section for SEO performance and propose improvements.

**Process:**
1. Read the target page/section content (HTML, component code, or URL)
2. Load [references/audit-checklist.md](references/audit-checklist.md) for the full checklist
3. Evaluate against all applicable checks in these categories:
   - On-Page SEO (titles, meta, headers, URLs, images, links, keywords)
   - Technical SEO (HTTPS, performance, crawlability, schema, architecture)
   - Content Quality (length, intent match, freshness, E-E-A-T, readability)
   - Off-Page signals (where observable)
   - AEO Readiness (FAQ sections, schema, snippet formatting, conversational tone)
   - Mobile (responsive, viewport, touch targets, speed)
4. Score each category and compute overall score using the weighting:
   - Technical: 25%, On-Page: 25%, Content: 20%, AEO: 15%, Off-Page: 10%, Mobile: 5%
5. Output a structured audit report as JSON (see JSON schema below)
6. Present a human-readable summary with prioritized recommendations

**Audit output format:**
```json
{
  "auditReport": {
    "date": "ISO-8601",
    "pageId": "URL or identifier",
    "overallScore": 0-100,
    "categories": {
      "onPage": { "score": 0-100, "checks": [{"name":"...","status":"pass|fail|warning","current":"...","recommended":"...","impact":"high|medium|low"}] },
      "technical": { "score": 0-100, "checks": [] },
      "content": { "score": 0-100, "checks": [] },
      "offPage": { "score": 0-100, "checks": [] },
      "aeo": { "score": 0-100, "checks": [] }
    },
    "topIssues": ["..."],
    "recommendations": ["..."]
  }
}
```

**Scoring rules:**
- Critical issues: -15 points from 100 baseline
- High impact: -8 points
- Medium impact: -4 points
- Low impact: -2 points

### 2. Page Strategy Suggestions

Suggest new SEO pages the user's app or site should have.

**Process:**
1. Understand the app/site's domain, audience, and existing pages
2. Load [references/page-strategies.md](references/page-strategies.md) for page types and suggestion framework
3. Analyze across these dimensions:
   - **Search intent coverage**: informational, navigational, commercial, transactional
   - **Funnel stages**: awareness, consideration, decision, retention
   - **Content cluster gaps**: missing pillars, orphaned content, incomplete clusters
   - **Page type gaps**: blog, FAQ, comparison, glossary, how-to, location, hub
   - **AEO opportunities**: FAQ pages, featured snippet targets, voice search pages
4. Output suggestions as JSON with rationale, each containing a full page entry ready for the registry

**Suggestion output format:**
```json
{
  "suggestions": [
    {
      "rationale": "Why this page should exist",
      "searchIntent": "informational|transactional|navigational|commercial",
      "estimatedVolume": "high|medium|low",
      "competitionLevel": "high|medium|low",
      "page": { "...full page registry entry..." }
    }
  ]
}
```

### 3. JSON Page Registry Management

Manage SEO pages through a structured `seo-pages.json` registry file.

**Registry operations:**

**Initialize a new registry:**
```bash
python scripts/seo_page_generator.py init <path/to/seo-pages.json> <https://domain.com>
```

**List pages in registry:**
```bash
python scripts/seo_page_generator.py list <path/to/seo-pages.json>
```

**Generate sitemap data:**
```bash
python scripts/seo_page_generator.py sitemap <path/to/seo-pages.json>
```

**Add/update pages programmatically:** Import and use `create_page_entry()`, `add_page()`, `update_audit()` from `scripts/seo_page_generator.py`.

For the full JSON schema covering page entries, audit reports, and suggestions, see [references/json-schema.md](references/json-schema.md).

**When the user asks to generate SEO pages:**
1. If no registry exists, initialize one with the script
2. Analyze the app to suggest pages (workflow 2)
3. For each approved suggestion, create a page entry using `create_page_entry()`
4. Add entries to the registry with `add_page()`
5. Output the updated registry JSON

**When the user asks to audit and update the registry:**
1. Run audit (workflow 1) on the target page
2. Use `update_audit()` to write results back to the registry
3. Show the updated page entry with scores and issues

## Key SEO Concepts Quick Reference

### On-Page Essentials
- **Title tags**: 50-60 chars, primary keyword near start, unique per page
- **Meta descriptions**: 150-160 chars, include keyword, CTA, unique per page
- **H1**: Exactly one per page, contains primary keyword
- **Headers**: Logical H1>H2>H3 hierarchy, keywords in H2s
- **URLs**: Short, hyphenated, lowercase, keyword-containing
- **Images**: Alt text on all images, compressed, descriptive filenames
- **Internal links**: 5-10 contextual links per page, descriptive anchors
- **Keywords**: Primary in first 100 words, 1-2% density, LSI variants

### AEO Essentials
- Add FAQ sections with FAQPage schema to relevant pages
- Structure answers in 40-60 word paragraphs for featured snippets
- Use question-based H2/H3 headings matching "People Also Ask" queries
- Implement HowTo schema for step-by-step content
- Write conversationally for voice search compatibility
- Provide direct, concise answers in the first sentence after each question heading

### Technical Essentials
- HTTPS with valid SSL certificate
- Core Web Vitals: LCP < 2.5s, CLS < 0.1, INP < 200ms
- XML sitemap submitted to Search Console
- Valid robots.txt not blocking important pages
- Canonical tags on all pages
- Mobile-responsive with viewport meta tag
- Schema markup (at minimum: BreadcrumbList site-wide + page-type schema)

### Content Quality Signals
- Minimum 300 words (1000+ for competitive keywords)
- Matches search intent (informational/commercial/transactional)
- E-E-A-T: Experience, Expertise, Authoritativeness, Trustworthiness
- Updated within last 12 months
- Unique, not duplicated across site
- Multimedia (images, video, infographics)
- Cited sources for claims

## Reference Files

| File | When to Load | Contents |
|------|-------------|----------|
| [references/audit-checklist.md](references/audit-checklist.md) | When auditing a page | Full audit checklist with checks, criteria, and scoring |
| [references/page-strategies.md](references/page-strategies.md) | When suggesting pages | Page types, suggestion framework, cluster patterns, schema mapping |
| [references/json-schema.md](references/json-schema.md) | When working with JSON registry | Full JSON schemas for pages, audits, and suggestions |
| [scripts/seo_page_generator.py](scripts/seo_page_generator.py) | When creating/managing registry | Python script for registry CRUD operations |
