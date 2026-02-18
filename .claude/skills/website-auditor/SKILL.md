---
name: website-auditor
description: "Comprehensive website audit covering SEO ranking, web design quality, product/conversion optimization, and AEO readiness. Delivers 50+ actionable improvement points across technical SEO, on-page optimization, content quality, indexing health, backlink signals, Core Web Vitals, structured data, AEO/AI readiness, web design, typography, color, layout, visual hierarchy, conversion funnels, onboarding, retention, pricing, and growth mechanics. Use when the user asks to: (1) Audit a website for any combination of SEO, design, or product issues, (2) Get improvement points for ranking higher on Google, (3) Review a landing page or website design, (4) Analyze conversion funnels or product UX, (5) Evaluate pricing pages or onboarding flows, (6) Optimize for AI answer engines or featured snippets, (7) Check Core Web Vitals or page speed, (8) Review structured data, schema, sitemaps, or robots.txt, (9) Identify retention or engagement issues, (10) Get a full website health check across all dimensions. Triggers on: website audit, SEO audit, design audit, product audit, conversion audit, ranking audit, Google ranking, landing page review, UX review, funnel analysis, onboarding review, pricing review, AEO audit, web design review, site health check, typography review, color audit, responsive design check, visual hierarchy review, retention analysis, growth analysis, engagement analysis, bounce rate, churn analysis."
---

# Website Auditor

Comprehensive website audit delivering 50+ prioritized improvement points across four pillars: **SEO & Ranking**, **AEO & AI Readiness**, **Web Design & Visual Quality**, and **Product & Conversion**.

## Workflow

### 1. Collect Target Information

Ask the user for:
- **URL to audit** (homepage or specific page)
- **Target keywords** (optional — improves keyword-specific SEO checks)
- **Business type** (local, e-commerce, SaaS, news, blog, portfolio — affects which checks apply)
- **Audit scope**: Full audit (all 4 pillars) or selective (choose specific pillars)

### 2. Run the Audit

Use browser automation tools to visit the target URL and perform checks across all applicable audit domains.

**Inspection order** (each step feeds the next):

1. **Page Load & Performance** — Navigate to URL, measure load behavior, check HTTPS, Core Web Vitals
2. **HTML Head Inspection** — Read page source for title, meta, canonical, robots, schema, viewport, hreflang
3. **Content & Structure** — Analyze headings, word count, keyword placement, internal links, images
4. **Crawlability Signals** — Check robots.txt, sitemap.xml, canonical tags, noindex tags
5. **Structured Data** — Validate schema markup types and completeness
6. **AEO Readiness** — Check FAQ sections, question-based headings, direct answers, snippet formatting
7. **Desktop Screenshots** — Capture full page at 1440px width
8. **Tablet Screenshots** — Capture at 768px width
9. **Mobile Screenshots** — Capture at 375px width
10. **Visual Design Assessment** — Evaluate typography, color, layout, imagery, visual hierarchy
11. **Product & Conversion Assessment** — Evaluate value proposition, funnel, pricing, onboarding, retention signals
12. **Backlink & Authority Signals** — Assess observable link signals (internal link depth, orphan risk, outbound link quality)

For each check, record: **status** (pass/fail/warning), **current value**, **recommended fix**, **impact level** (critical/high/medium/low).

---

### Audit Pillar A: SEO & Ranking

Load [references/seo-ranking-checks.md](references/seo-ranking-checks.md) for the full checklist.

**Sub-categories:**
1. **Technical SEO** — HTTPS & security, page load performance, Core Web Vitals, crawl efficiency, structured data / schema markup, site architecture
2. **On-Page SEO** — Title tags, meta descriptions, header hierarchy & keywords, URL structure, image optimization, internal linking strategy, keyword placement & density
3. **Content Quality** — Content depth & search intent, E-E-A-T signals, freshness, multimedia, uniqueness, readability
4. **Indexing & Discovery** — Canonical tags, robots.txt configuration, XML sitemap health, indexability signals, duplicate content & soft 404s
5. **Off-Page & Authority** — Backlink signals, anchor text quality, outbound link quality, local SEO (if applicable: Google Business Profile, NAP consistency, local citations)
6. **Mobile SEO** — Responsive design, viewport meta tag, tap targets, mobile navigation, no intrusive interstitials, mobile load speed

### Audit Pillar B: AEO & AI Readiness

Load [references/seo-ranking-checks.md](references/seo-ranking-checks.md) (AEO sections: checks 22-24) for the full checklist.

**Sub-categories:**
1. **Featured Snippet Readiness** — Direct answer format (40-60 words), paragraph/list/table snippet formatting, summary/TL;DR sections, clear definitions
2. **FAQ Section & Schema** — FAQ presence on relevant pages, FAQPage JSON-LD schema, questions matching real queries, concise complete answers, natural language phrasing
3. **Voice Search Optimization** — Conversational tone, long-tail keyword targeting, natural language writing
4. **AI Answer Engine Optimization** — Structured answers for RAG systems, People Also Ask coverage, HowTo schema for step-by-step content
5. **Video Content Optimization** — Dedicated watch pages, VideoObject schema, responsive video player, one primary video per page

### Audit Pillar C: Web Design & Visual Quality

Load [references/web-design-checks.md](references/web-design-checks.md) for the full checklist.

**Sub-categories:**
1. **First Impressions & Visual Impact** — 5-second test: clarity, visual hierarchy, emotional tone, professionalism, differentiation
2. **Hero Section Effectiveness** — Headline impact, subheadline support, CTA clarity & contrast, imagery/media, layout composition, above-the-fold content
3. **Typography & Readability** — Font selection & pairing, heading hierarchy, body text readability (16px+, line-height 1.4-1.6), line length (50-75 chars), text contrast (WCAG AA: 4.5:1), consistency
4. **Color & Visual Identity** — Palette cohesion, brand alignment, accent color for CTAs, contrast & accessibility, color consistency, background variation
5. **Layout, Spacing & Visual Rhythm** — Grid consistency, section spacing (40-80px), element spacing, whitespace, content width (900-1200px), visual balance, section variety
6. **Navigation & Page Structure** — Nav clarity (5-7 items max), logo placement, page flow logic, section identification, footer completeness, breadcrumbs, scroll depth
7. **Imagery & Media** — Image quality (2x retina), relevance, style consistency, custom vs stock, icon consistency, logo presentation, alt text
8. **Interactive Elements & Microinteractions** — Button design & hierarchy, hover/focus states, form design & validation, link styling, loading states, animations
9. **Responsive Design & Cross-Device** — Breakpoint transitions (1440/768/375), mobile navigation, touch targets (44x44px), typography scaling, image handling, spacing adjustment
10. **Trust, Social Proof & Credibility** — Testimonials (real names/photos/companies), client logos, case studies, social proof placement near CTAs, team/about visibility, security indicators, contact info

Supporting references:
- [references/design-principles.md](references/design-principles.md) — Typography, color theory, visual hierarchy, imagery guidelines
- [references/layout-checklist.md](references/layout-checklist.md) — Grid, spacing, responsive design, accessibility standards
- [references/section-patterns.md](references/section-patterns.md) — Hero, CTA, testimonial, pricing, navigation, footer patterns

### Audit Pillar D: Product & Conversion

Load [references/product-conversion-checks.md](references/product-conversion-checks.md) for the full checklist.

**Sub-categories:**
1. **First Impressions & Value Proposition** — Value clarity (5-second test), headline effectiveness, CTA visibility above fold, visual hierarchy, trust signals, page load perception
2. **Conversion Funnel Analysis** — Steps to conversion (3 or fewer ideal), form friction (each field -7% conversion), progress indicators, exit points, error handling, social login/SSO, mobile funnel
3. **Onboarding & Activation** — Time to value (TTV), empty states, progressive disclosure, checklists/progress, tooltips/guides, aha moment path
4. **Retention & Engagement** — Email capture, notification systems, content freshness, community features, personalization, habit loops, feature depth
5. **Pricing & Monetization** — Tier clarity, value anchoring, free tier/trial, feature comparison table, price-to-value alignment, annual vs monthly, objection handling (FAQ, guarantees)
6. **User Experience & Navigation** — Navigation clarity (2-click rule), search functionality, mobile experience, accessibility (contrast, alt text, keyboard nav), loading states, error pages, breadcrumbs
7. **Trust & Social Proof** — Testimonials (names, photos, specific results), case studies with metrics, client logos, third-party reviews, security/privacy, team/about page
8. **Growth & Virality Mechanics** — Referral programs, social sharing, embeddable content, SEO foundations, content marketing, backlink potential

Supporting references:
- [references/metrics-reference.md](references/metrics-reference.md) — Retention, engagement, acquisition, revenue metric definitions and formulas
- [references/pricing-frameworks.md](references/pricing-frameworks.md) — Tier structure evaluation, pricing psychology, free tier/trial analysis
- [references/prioritization-guide.md](references/prioritization-guide.md) — RICE, MoSCoW, Kano, value/complexity matrix frameworks

---

### 3. Generate the Report

Output a structured report with **minimum 50 improvement points** across all audited pillars, organized by priority.

**Report format:**

```
## Website Audit Report
**URL:** [audited URL]
**Date:** [date]
**Business Type:** [type]
**Audit Scope:** [Full / Selected pillars]

---

### Executive Summary
[3-5 sentence overview of the most critical findings across all pillars]

### Overall Scores

#### SEO & Ranking Score: X/100
| Sub-category | Score | Key Issues |
|-------------|-------|------------|
| Technical SEO | X/100 | ... |
| On-Page SEO | X/100 | ... |
| Content Quality | X/100 | ... |
| Indexing & Discovery | X/100 | ... |
| Off-Page & Authority | X/100 | ... |
| Mobile SEO | X/100 | ... |

#### AEO & AI Readiness Score: X/100
| Sub-category | Score | Key Issues |
|-------------|-------|------------|
| Featured Snippet Readiness | X/100 | ... |
| FAQ & Schema | X/100 | ... |
| Voice Search | X/100 | ... |
| AI Engine Optimization | X/100 | ... |
| Video Content | X/100 | ... |

#### Web Design Score: X/5 (X/100)
| Sub-category | Score (1-5) | Key Issues |
|-------------|-------------|------------|
| First Impressions | X/5 | ... |
| Hero Section | X/5 | ... |
| Typography | X/5 | ... |
| Color & Identity | X/5 | ... |
| Layout & Spacing | X/5 | ... |
| Navigation & Structure | X/5 | ... |
| Imagery & Media | X/5 | ... |
| Interactive Elements | X/5 | ... |
| Responsive Design | X/5 | ... |
| Trust & Credibility | X/5 | ... |

#### Product & Conversion Score: X/5 (X/100)
| Sub-category | Score (1-5) | Key Issues |
|-------------|-------------|------------|
| Value Proposition | X/5 | ... |
| Conversion Funnel | X/5 | ... |
| Onboarding | X/5 | ... |
| Retention | X/5 | ... |
| Pricing | X/5 | ... |
| UX & Navigation | X/5 | ... |
| Trust & Social Proof | X/5 | ... |
| Growth Mechanics | X/5 | ... |

#### Overall Website Score: X/100
| Pillar | Weight | Score |
|--------|--------|-------|
| SEO & Ranking | 35% | X/100 |
| AEO & AI Readiness | 10% | X/100 |
| Web Design | 25% | X/100 |
| Product & Conversion | 30% | X/100 |
| **Weighted Total** | **100%** | **X/100** |

---

### Critical Issues (Fix Immediately)
1. [Issue] — [What's wrong] → [How to fix] | Pillar: X | Impact: Critical

### High-Priority Improvements
2. [Issue] — [What's wrong] → [How to fix] | Pillar: X | Impact: High
...

### Medium-Priority Improvements
...

### Quick Wins (Low Effort, Good Return)
...

---

### Detailed Findings by Pillar
[Per-pillar, per-category breakdown with screenshots and specific observations]

### Design Strengths
[What the site does well — important to acknowledge]

### Before/After Concepts
[For top design recommendations, describe what the improved version would look like]

### Metric Impact Estimates
| Recommendation | Target Metric | Estimated Impact |
|---------------|---------------|-----------------|
| ... | Conversion Rate | +X% |
| ... | Bounce Rate | -X% |
| ... | Organic Rankings | +X positions |
| ... | Retention | +X% |

### Summary
- Total issues found: X
- Critical: X | High: X | Medium: X | Low: X
- Top 5 actions for biggest overall impact:
  1. ...
  2. ...
  3. ...
  4. ...
  5. ...

### Next Steps
[Prioritized action items organized by effort level and pillar]
```

### 4. Score Calculation

#### SEO & Ranking + AEO Scores (0-100 scale)

Start from 100 and deduct per issue found:
- Critical issue: -15 points
- High impact: -8 points
- Medium impact: -4 points
- Low impact: -2 points

Minimum score is 0.

SEO & Ranking sub-category weights:
| Sub-category | Weight |
|-------------|--------|
| Technical SEO (HTTPS, speed, crawlability) | 25% |
| On-Page SEO (titles, headers, keywords, URLs) | 25% |
| Content Quality (depth, intent, E-E-A-T, freshness) | 20% |
| Indexing & Discovery (sitemap, canonical, robots.txt) | 15% |
| Off-Page & Authority (backlinks, local SEO) | 10% |
| Mobile SEO | 5% |

#### Web Design & Product Scores (1-5 per category → 0-100)

Rate each sub-category 1-5:
| Score | Meaning |
|-------|---------|
| 5 | Excellent — Professional quality, no issues |
| 4 | Good — Minor improvements possible |
| 3 | Average — Several noticeable issues |
| 2 | Below average — Significant problems |
| 1 | Poor — Major redesign needed |

Convert to 0-100: (average sub-category score / 5) × 100

#### Overall Website Score

Weighted average across all pillars:
| Pillar | Weight |
|--------|--------|
| SEO & Ranking | 35% |
| AEO & AI Readiness | 10% |
| Web Design | 25% |
| Product & Conversion | 30% |

#### Recommendation Prioritization

Use combined Impact/Effort scoring with RICE for product recommendations:

- **P1 — Quick Wins**: High impact, low effort. Implement immediately.
- **P2 — Strategic**: High impact, higher effort. Plan for next phase.
- **P3 — Polish**: Moderate impact. Address when time allows.
- **P4 — Backlog**: Low impact relative to effort. Consider for future.

RICE formula for product recommendations: `(Reach × Impact × Confidence) / Effort`

---

## Additional Workflow: Page Strategy Suggestions

Suggest new SEO pages the user's site should have.

**Process:**
1. Understand the site's domain, audience, and existing pages
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

## Additional Workflow: JSON Page Registry Management

Manage SEO pages through a structured `seo-pages.json` registry file.

For the full JSON schema, see [references/json-schema.md](references/json-schema.md).

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

**When the user asks to generate SEO pages:**
1. If no registry exists, initialize one with the script
2. Analyze the app to suggest pages (page strategy workflow)
3. For each approved suggestion, create a page entry using `create_page_entry()`
4. Add entries to the registry with `add_page()`
5. Output the updated registry JSON

**When the user asks to audit and update the registry:**
1. Run audit on the target page
2. Use `update_audit()` to write results back to the registry
3. Show the updated page entry with scores and issues

## Additional Workflow: SEO Audit (JSON Output)

When the user specifically requests JSON audit output (for programmatic use), output in this format:

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
      "aeo": { "score": 0-100, "checks": [] },
      "design": { "score": 0-100, "checks": [] },
      "product": { "score": 0-100, "checks": [] }
    },
    "topIssues": ["..."],
    "recommendations": ["..."]
  }
}
```

---

## Key Principles from Google Search Console Expertise

These principles inform the audit logic — they come from deep analysis of how Google discovers, crawls, renders, indexes, and ranks pages:

- **Discovery depends on 10+ methods**: sitemap, internal links, external links, URL guessing, server logs, Chrome usage data, domain registrar data, RSS feeds, GSC URL submission, JS rendering. A site that only relies on sitemaps is missing discovery channels.
- **Crawl budget is finite**: Google allocates crawl resources based on site quality and server speed. Response time >1000ms hurts crawl efficiency. Wasted crawl budget on 404s, redirects, or low-value pages means important pages get crawled less.
- **Indexing is not guaranteed**: Google may discover and crawl a page but still choose not to index it. Common reasons: thin content, duplicate content, soft 404, noindex tag, canonical pointing elsewhere.
- **Rendering matters**: If Googlebot can't render JS-heavy content, it treats the page as empty. Always verify pages are visible to Googlebot.
- **Canonical is a hint, not an instruction**: Google may override your canonical choice if signals (internal links, backlinks, sitemap inclusion) point to a different preferred version.
- **Backlinks are a tiebreaker**: When content quality is semantically equal between competitors, backlink authority breaks the tie. Focus on content quality first, backlinks second.
- **Anchor text relevance + link category matter**: Irrelevant anchor text pointing to wrong pages, or links from unrelated industry categories, can dilute or harm rankings.
- **AEO = SEO done well**: Answer Engine Optimization for ChatGPT, Perplexity, Google AI Mode uses the same fundamentals — semantic relevance, structured answers, authority signals. There are no separate "GEO tricks."
- **Page Experience is a ranking signal**: Core Web Vitals (LCP, CLS, INP) directly affect rankings, especially on mobile. Google uses mobile-first indexing.
- **Video needs watch pages**: Embedding a video in a blog post won't get it indexed in video search. Each video needs a dedicated page where the video is the primary content.

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

---

## Reference Files

| File | When to Load | Contents |
|------|-------------|----------|
| [references/seo-ranking-checks.md](references/seo-ranking-checks.md) | When performing SEO & AEO audit | Full 30+ point SEO/AEO checklist with checks, pass criteria, fix instructions, and scoring |
| [references/web-design-checks.md](references/web-design-checks.md) | When performing design audit | 10-category web design checklist with evaluation criteria and scoring |
| [references/product-conversion-checks.md](references/product-conversion-checks.md) | When performing product/conversion audit | 8-category product audit checklist with criteria, metric targets, and RICE scoring |
| [references/design-principles.md](references/design-principles.md) | Deep-dive on design issues | Typography, color theory, visual hierarchy, imagery, brand consistency guidelines |
| [references/layout-checklist.md](references/layout-checklist.md) | Deep-dive on layout issues | Grid & container standards, spacing system, responsive breakpoints, accessibility standards |
| [references/section-patterns.md](references/section-patterns.md) | Evaluating page sections | Navigation, hero, features, social proof, CTA, pricing, gallery, contact, footer patterns |
| [references/page-strategies.md](references/page-strategies.md) | When suggesting new pages | Page types, suggestion framework, content pillars & clusters, keyword mapping, schema recommendations |
| [references/json-schema.md](references/json-schema.md) | When working with page registry | Full JSON schemas for page entries, audit reports, and suggestions |
| [references/metrics-reference.md](references/metrics-reference.md) | When assessing product metrics | Retention, engagement, satisfaction, acquisition, traffic, revenue, virality metrics |
| [references/pricing-frameworks.md](references/pricing-frameworks.md) | When evaluating pricing pages | Tier structure evaluation, pricing psychology, free tier/trial analysis, anti-patterns |
| [references/prioritization-guide.md](references/prioritization-guide.md) | When prioritizing recommendations | RICE framework, MoSCoW method, Kano model, value vs complexity matrix |
