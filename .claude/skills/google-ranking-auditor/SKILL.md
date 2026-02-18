---
name: google-ranking-auditor
description: "Audit a live website for Google ranking improvements, delivering 20+ actionable improvement points across technical SEO, on-page optimization, indexing health, backlink quality, Core Web Vitals, structured data, AEO readiness, and crawl efficiency. Use when the user asks to: (1) Audit a website for SEO/ranking issues, (2) Get improvement points for ranking higher on Google, (3) Analyze why a site isn't ranking well, (4) Check a site's SEO health or Google readiness, (5) Identify SEO problems on a live URL, (6) Improve organic search visibility, (7) Optimize for AI answer engines (AEO/GEO), (8) Fix indexing or crawling issues, (9) Audit Core Web Vitals or page speed, (10) Review structured data, schema, sitemaps, or robots.txt. Triggers on: SEO audit, ranking audit, Google ranking, website audit for SEO, why isn't my site ranking, improve Google rankings, site health check, AEO audit, search visibility."
---

# Google Ranking Auditor

Audit a live website and deliver 20+ prioritized improvement points to rank higher on Google.

## Workflow

### 1. Collect Target Information

Ask the user for:
- **URL to audit** (homepage or specific page)
- **Target keywords** (optional — improves keyword-specific checks)
- **Business type** (local, e-commerce, SaaS, news, blog — affects which checks apply)

### 2. Run the Audit

Use browser automation tools to visit the target URL and perform the checks documented in [references/audit-framework.md](references/audit-framework.md).

**Inspection order** (each step feeds the next):

1. **Page Load & Performance** — Navigate to URL, measure load behavior, check HTTPS
2. **HTML Head Inspection** — Read page source for title, meta, canonical, robots, schema, viewport, hreflang
3. **Content & Structure** — Analyze headings, word count, keyword placement, internal links, images
4. **Crawlability Signals** — Check robots.txt, sitemap.xml, canonical tags, noindex tags
5. **Structured Data** — Validate schema markup types and completeness
6. **AEO Readiness** — Check FAQ sections, question-based headings, direct answers, snippet formatting
7. **Mobile Experience** — Responsive layout, tap targets, viewport, font sizes
8. **Backlink & Authority Signals** — Assess observable link signals (internal link depth, orphan risk, outbound link quality)

For each check, record: **status** (pass/fail/warning), **current value**, **recommended fix**, **impact level** (critical/high/medium/low).

### 3. Generate the Report

Output a structured report with **minimum 20 improvement points**, organized by priority.

**Report format:**

```
## Google Ranking Audit Report
**URL:** [audited URL]
**Date:** [date]
**Overall Score:** [X/100]

### Critical Issues (Fix Immediately)
1. [Issue] — [What's wrong] → [How to fix] | Impact: Critical

### High-Priority Improvements
2. [Issue] — [What's wrong] → [How to fix] | Impact: High
...

### Medium-Priority Improvements
...

### Quick Wins (Low Effort, Good Return)
...

### Summary
- Total issues found: X
- Critical: X | High: X | Medium: X | Low: X
- Top 3 actions for biggest ranking impact:
  1. ...
  2. ...
  3. ...
```

### 4. Score Calculation

Start from 100 and deduct per issue found:
- Critical issue: -15 points
- High impact: -8 points
- Medium impact: -4 points
- Low impact: -2 points

Minimum score is 0. Categories and weights:
| Category | Weight |
|----------|--------|
| Technical SEO (HTTPS, speed, crawlability) | 25% |
| On-Page SEO (titles, headers, keywords, URLs) | 25% |
| Content Quality (depth, intent, E-E-A-T, freshness) | 20% |
| AEO Readiness (FAQ, schema, snippets, AI answers) | 15% |
| Indexing & Discovery (sitemap, canonical, robots.txt) | 10% |
| Mobile Experience | 5% |

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

## Reference Files

| File | When to Load | Contents |
|------|-------------|----------|
| [references/audit-framework.md](references/audit-framework.md) | When performing the audit | Full 25-point audit checklist with specific checks, pass criteria, fix instructions, and scoring |
