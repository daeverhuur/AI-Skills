# SEO & Ranking Audit Checks

Comprehensive merged reference combining the Google Ranking Audit Framework (25 checks) with the SEO/AEO Audit Checklist. Each check includes detailed pass criteria, impact levels, verification methods, and fix instructions.

---

## Table of Contents

1. [HTTPS & Security](#1-https--security)
2. [Page Load Performance](#2-page-load-performance)
3. [Core Web Vitals](#3-core-web-vitals)
4. [Mobile Responsiveness](#4-mobile-responsiveness)
5. [Title Tag Optimization](#5-title-tag-optimization)
6. [Meta Description Quality](#6-meta-description-quality)
7. [Header Hierarchy & Keywords](#7-header-hierarchy--keywords)
8. [URL Structure](#8-url-structure)
9. [Canonical Tag Implementation](#9-canonical-tag-implementation)
10. [Robots.txt Configuration](#10-robotstxt-configuration)
11. [XML Sitemap Health](#11-xml-sitemap-health)
12. [Internal Linking Strategy](#12-internal-linking-strategy)
13. [Content Depth & Search Intent](#13-content-depth--search-intent)
14. [Keyword Placement & Density](#14-keyword-placement--density)
15. [Image Optimization](#15-image-optimization)
16. [Structured Data / Schema Markup](#16-structured-data--schema-markup)
17. [Indexability Signals](#17-indexability-signals)
18. [Duplicate Content & Soft 404s](#18-duplicate-content--soft-404s)
19. [Crawl Efficiency](#19-crawl-efficiency)
20. [Backlink & Authority Signals](#20-backlink--authority-signals)
21. [E-E-A-T Signals](#21-e-e-a-t-signals)
22. [AEO / Featured Snippet Readiness](#22-aeo--featured-snippet-readiness)
23. [FAQ Section & Schema](#23-faq-section--schema)
24. [Video Content Optimization](#24-video-content-optimization)
25. [Page Experience & UX Signals](#25-page-experience--ux-signals)
26. [Local SEO (If Applicable)](#26-local-seo-if-applicable)
27. [Scoring Summary](#scoring-summary)

---

## 1. HTTPS & Security

**Category:** Technical SEO | **Impact:** Critical

Google confirmed HTTPS is a ranking signal. HTTP pages are flagged as "Not Secure" in Chrome and other modern browsers. Sites without HTTPS face trust erosion and ranking penalties.

### Checks

| # | Check | Pass Criteria | How to Verify |
|---|-------|--------------|---------------|
| 1.1 | HTTPS enabled | Page loads over `https://` | Load page in browser, check URL bar shows padlock |
| 1.2 | Valid SSL certificate | No browser security warnings, certificate not expired | Browser padlock icon shows "Connection is secure"; check expiry date |
| 1.3 | HTTP→HTTPS redirect | `http://` version 301-redirects to `https://` | Curl `http://domain.com` and verify 301 redirect to HTTPS |
| 1.4 | No mixed content | All resources (images, scripts, stylesheets) load over HTTPS | Open DevTools Console, check for mixed content warnings |
| 1.5 | HSTS header present | `Strict-Transport-Security` header in response headers | Check response headers in DevTools Network tab or via curl |

### Fix Instructions

1. **Install/renew SSL certificate** — Use Let's Encrypt (free) or purchase from a CA. Most hosting providers offer one-click SSL.
2. **Set up 301 redirect** — In `.htaccess` (Apache) or server config (Nginx), redirect all HTTP traffic to HTTPS permanently.
3. **Fix mixed content** — Update all resource URLs from `http://` to `https://` or use protocol-relative `//` URLs. Search HTML, CSS, and JS for hardcoded `http://` references.
4. **Enable HSTS** — Add `Strict-Transport-Security: max-age=31536000; includeSubDomains` to response headers.

---

## 2. Page Load Performance

**Category:** Technical SEO | **Impact:** Critical

Server response time directly affects crawl budget and user experience. There is an inverse relationship between response time and crawl requests — slower sites get crawled less frequently. Target: <1000ms (ideal <500ms).

### Checks

| # | Check | Pass Criteria | How to Verify |
|---|-------|--------------|---------------|
| 2.1 | Server response time | Under 1 second (ideal under 500ms) | DevTools Network tab — check TTFB; or use WebPageTest |
| 2.2 | Time to interactive | Page usable within 4 seconds | Lighthouse audit or WebPageTest |
| 2.3 | Render-blocking resources | No blocking JS/CSS without `defer`/`async` | Lighthouse "Eliminate render-blocking resources" audit |
| 2.4 | Asset minification | CSS and JS files minified (no unnecessary whitespace/comments) | Check file sizes; compare minified vs. source |
| 2.5 | Image compression | No uncompressed images over 200KB | DevTools Network tab — filter by Img, check sizes |
| 2.6 | CDN usage | Static assets served from CDN | Check response headers for CDN indicators (e.g., `cf-ray` for Cloudflare) |
| 2.7 | Browser caching | `Cache-Control` headers present on static resources | DevTools Network tab — check response headers on CSS/JS/image files |

### Fix Instructions

1. **Enable server-side caching** — Use Redis, Memcached, or application-level caching to reduce database queries.
2. **Use a CDN** — Cloudflare, Fastly, or CloudFront for static asset delivery.
3. **Defer non-critical JS** — Add `defer` or `async` attributes to script tags that are not needed for initial render.
4. **Compress images to WebP** — Use tools like Squoosh, ImageOptim, or build-time plugins. Target <200KB per image.
5. **Minify CSS/JS** — Use build tools (Webpack, Vite, esbuild) or online minifiers. Remove unused CSS with PurgeCSS.
6. **Set Cache-Control headers** — `Cache-Control: public, max-age=31536000` for static assets with fingerprinted filenames.

### Why It Matters

Google's crawl budget is finite. Slow response times mean Googlebot makes fewer requests, leaving pages undiscovered or stale. Studies show a direct inverse relationship between server response time and crawl frequency.

---

## 3. Core Web Vitals

**Category:** Technical SEO | **Impact:** High

Core Web Vitals (CWV) are page experience ranking signals measured on real user data (CrUX). They assess loading, visual stability, and interactivity.

### Metrics & Thresholds

| # | Metric | Good | Needs Improvement | Poor |
|---|--------|------|-------------------|------|
| 3.1 | LCP (Largest Contentful Paint) | < 2.5s | 2.5–4.0s | > 4.0s |
| 3.2 | CLS (Cumulative Layout Shift) | < 0.1 | 0.1–0.25 | > 0.25 |
| 3.3 | INP (Interaction to Next Paint) | < 200ms | 200–500ms | > 500ms |
| 3.4 | FCP (First Contentful Paint) | < 2.0s | 2.0–4.0s | > 4.0s |

### Checks

| # | Check | Pass Criteria | How to Verify |
|---|-------|--------------|---------------|
| 3.1 | LCP within threshold | < 2.5 seconds | PageSpeed Insights, Lighthouse, CrUX Dashboard |
| 3.2 | CLS within threshold | < 0.1 | PageSpeed Insights, Lighthouse, Web Vitals JS library |
| 3.3 | INP within threshold | < 200ms | PageSpeed Insights (field data), Chrome DevTools Performance tab |
| 3.4 | FCP within threshold | < 2.0 seconds | Lighthouse, PageSpeed Insights |

### Fix Instructions

1. **LCP optimization** — Optimize the largest image (compress, use WebP, preload hero image with `<link rel="preload">`). Use `fetchpriority="high"` on the LCP element. Minimize server response time.
2. **CLS optimization** — Set explicit `width` and `height` attributes on all images and videos. Reserve space for ads/embeds. Avoid inserting content above existing content dynamically.
3. **INP optimization** — Reduce JavaScript execution time. Break long tasks (>50ms) into smaller chunks using `requestIdleCallback` or `scheduler.yield()`. Minimize main-thread work.
4. **FCP optimization** — Inline critical CSS, defer non-critical CSS, reduce server response time, preconnect to required origins.

---

## 4. Mobile Responsiveness

**Category:** Mobile | **Impact:** Critical

Google uses mobile-first indexing — the mobile version of your page is the primary version Google evaluates for ranking. A poor mobile experience directly harms rankings.

### Checks

| # | Check | Pass Criteria | How to Verify |
|---|-------|--------------|---------------|
| 4.1 | Viewport meta tag present | `<meta name="viewport" content="width=device-width, initial-scale=1">` exists | View page source, search for viewport tag |
| 4.2 | Responsive layout | No horizontal scroll on mobile viewports | Test at 375px, 390px, 414px widths in DevTools |
| 4.3 | Readable text | Base font size ≥ 16px, sufficient contrast | DevTools computed styles; Lighthouse accessibility audit |
| 4.4 | Tap targets | ≥ 48px × 48px with adequate spacing between targets | Lighthouse "Tap targets" audit |
| 4.5 | No intrusive interstitials | No full-screen popups blocking content on mobile | Manually test on mobile; check for popups on page load |
| 4.6 | Mobile navigation usable | Hamburger menu works, navigation items reachable | Manual testing on mobile device or emulator |
| 4.7 | Fast mobile load | Page loads under 3 seconds on 4G connection | Lighthouse with mobile throttling; WebPageTest 4G profile |
| 4.8 | Passes Google Mobile-Friendly Test | Google's test reports "Page is mobile-friendly" | Run Google Mobile-Friendly Test or check Search Console |

### Fix Instructions

1. **Add viewport meta tag** — Place `<meta name="viewport" content="width=device-width, initial-scale=1">` in `<head>`.
2. **Use responsive CSS** — Use relative units (`%`, `rem`, `vw`), flexbox, CSS Grid. Avoid fixed pixel widths on containers.
3. **Increase font size** — Set `body { font-size: 16px; }` minimum. Use `rem` for scaling.
4. **Fix tap targets** — Ensure buttons/links are at least 48×48px with 8px+ spacing between interactive elements.
5. **Remove intrusive interstitials** — Replace full-screen popups with banners or inline CTAs. Defer popups until after user engagement.

---

## 5. Title Tag Optimization

**Category:** On-Page SEO | **Impact:** High

The title tag is one of the strongest on-page ranking signals and the primary element users see in search results. It directly impacts both rankings and click-through rate.

### Checks

| # | Check | Pass Criteria | How to Verify |
|---|-------|--------------|---------------|
| 5.1 | Title exists | Non-empty `<title>` tag present in `<head>` | View page source, check for `<title>` |
| 5.2 | Length | 50–60 characters (displays fully in SERP) | Count characters; use SERP preview tool |
| 5.3 | Primary keyword present | Target keyword appears in title | Read the title; confirm keyword presence |
| 5.4 | Keyword in first half | Keyword appears within the first 30 characters | Check keyword position in the title string |
| 5.5 | Unique per page | No other page on the site has the same title | Crawl site with Screaming Frog or similar; check for duplicates |
| 5.6 | Compelling for CTR | Uses power words, numbers, or questions to encourage clicks | Manual review for engagement factors |
| 5.7 | Brand name included | Brand/site name appended where appropriate (e.g., "Title — Brand") | Check title format for brand inclusion |

### Fix Instructions

1. **Write unique titles** — Every indexable page needs its own distinct title tag. Never duplicate.
2. **Front-load keywords** — Place the primary keyword as close to the beginning as possible.
3. **Keep within length** — 50–60 characters to avoid truncation in SERPs. Google measures in pixels (~600px), so avoid wide characters.
4. **Make it compelling** — Use numbers ("7 Ways to..."), power words ("Ultimate", "Complete"), or questions to boost CTR.
5. **Include brand** — Append brand name at the end separated by ` | ` or ` — ` for brand recognition.

---

## 6. Meta Description Quality

**Category:** On-Page SEO | **Impact:** Medium

Meta descriptions don't directly affect rankings but strongly influence click-through rate (CTR), which is a user engagement signal. Google may rewrite descriptions that don't match the page content.

### Checks

| # | Check | Pass Criteria | How to Verify |
|---|-------|--------------|---------------|
| 6.1 | Description exists | Non-empty `<meta name="description">` tag present | View page source, check for meta description |
| 6.2 | Length | 150–160 characters | Count characters; SERP preview tool |
| 6.3 | Contains primary keyword | Keyword appears naturally in description | Read description, confirm keyword presence |
| 6.4 | Call-to-action included | Description contains an action phrase ("Learn how...", "Discover...", "Get started...") | Manual review |
| 6.5 | Unique per page | No other page has the same description | Crawl site for duplicate meta descriptions |
| 6.6 | Not keyword-stuffed | Keyword appears 1–2 times maximum, reads naturally | Manual review for readability |

### Fix Instructions

1. **Write unique descriptions** — One per page, summarizing the page's value proposition in 150–160 characters.
2. **Include primary keyword** — Google bolds matching search terms in descriptions, increasing CTR.
3. **Add a CTA** — End with an action phrase: "Learn more", "Get your free guide", "Compare options today".
4. **Avoid stuffing** — Use the keyword once or twice naturally. Google may ignore stuffed descriptions and auto-generate one.

---

## 7. Header Hierarchy & Keywords

**Category:** On-Page SEO | **Impact:** High

Header tags (H1–H6) define content structure for both users and search engines. Proper hierarchy helps Google understand topic relevance and content organization.

### Checks

| # | Check | Pass Criteria | How to Verify |
|---|-------|--------------|---------------|
| 7.1 | Single H1 | Exactly one `<h1>` tag per page | DevTools: `document.querySelectorAll('h1').length === 1` |
| 7.2 | H1 contains primary keyword | Target keyword appears in the H1 text | Read the H1; confirm keyword presence |
| 7.3 | H1 matches title intent | H1 and title tag convey the same topic/intent | Compare H1 and title side by side |
| 7.4 | Logical hierarchy | H1 > H2 > H3, no skipped levels (e.g., no H1 → H3) | Inspect heading outline; use a heading checker tool |
| 7.5 | H2s for major sections | Each major content section has an H2 heading | Review page structure |
| 7.6 | Keywords in H2s | Secondary/related keywords appear in H2 headings | Read H2s, check for keyword relevance |
| 7.7 | Question-based H2s for AEO | At least some H2s phrased as questions ("How to...", "What is...") | Review H2s for question format |
| 7.8 | Header length | Headings between 20–70 characters | Measure character count of each heading |

### Fix Instructions

1. **Ensure single H1** — Remove duplicate H1 tags. Use H2 for section headings. The H1 should be the page's main topic.
2. **Add keywords to headings** — Place primary keyword in H1, secondary keywords in H2s. Keep it natural.
3. **Fix hierarchy** — Never skip levels. If content goes from H1 to H3, add an H2 in between.
4. **Use question headings** — Format some H2s as questions users actually ask. This targets PAA (People Also Ask) boxes and AI answer extraction.
5. **Keep headings concise** — 20–70 characters is the sweet spot. Too short lacks context; too long loses impact.

---

## 8. URL Structure

**Category:** On-Page SEO | **Impact:** Medium

Clean, descriptive URLs help search engines understand page content and improve user trust. Google's URL Resolver converts relative URLs to absolute, so using absolute URLs saves a processing step.

### Checks

| # | Check | Pass Criteria | How to Verify |
|---|-------|--------------|---------------|
| 8.1 | Readable URL | No random IDs, session tokens, or meaningless parameters | Inspect URL in browser address bar |
| 8.2 | Contains keyword | URL slug includes the target keyword | Check URL path for keyword presence |
| 8.3 | Hyphens as separators | Words separated by hyphens, not underscores or spaces | Inspect URL for `-` usage |
| 8.4 | Lowercase | Entire URL path is lowercase | Check for uppercase characters in URL |
| 8.5 | Short path | Total URL path under 75 characters | Count characters in the path portion |
| 8.6 | No query parameters | URL does not rely on query strings for content delivery | Check for `?` in URL |
| 8.7 | Absolute URLs in internal links | Internal links use full `https://domain.com/path` format | Inspect internal link `href` attributes in source |
| 8.8 | Canonical tag present | `<link rel="canonical">` pointing to self or preferred URL | View source, check for canonical tag |

### Why Absolute URLs Matter

Google's URL Resolver converts relative URLs to absolute during processing. Using absolute URLs in internal links saves this processing step and eliminates ambiguity, especially in complex site architectures.

### Fix Instructions

1. **Restructure URLs** — Use lowercase, hyphenated, keyword-rich slugs: `/seo-audit-checklist` not `/page?id=123`.
2. **Set up redirects** — 301-redirect old URLs to new clean URLs to preserve link equity.
3. **Use absolute URLs** — Update internal links to use full absolute URLs.
4. **Add canonical tags** — Every indexable page should have a self-referencing canonical tag.

---

## 9. Canonical Tag Implementation

**Category:** Indexing & Discovery | **Impact:** High

Canonical tags tell search engines which version of a page is the "preferred" one, consolidating ranking signals and preventing duplicate content issues.

### Checks

| # | Check | Pass Criteria | How to Verify |
|---|-------|--------------|---------------|
| 9.1 | Canonical tag exists | `<link rel="canonical" href="...">` present in `<head>` | View page source, search for `rel="canonical"` |
| 9.2 | Self-referencing canonical | Canonical URL matches the current page URL | Compare canonical href with the actual URL |
| 9.3 | Consistent protocol | Canonical uses HTTPS (not HTTP) | Check canonical href starts with `https://` |
| 9.4 | Consistent www/non-www | Canonical matches the preferred domain variant | Check canonical matches site's www preference |
| 9.5 | No conflicting signals | Sitemap URL, internal links, and canonical all agree on the preferred URL | Cross-reference sitemap, internal links, and canonical tag |

### Fix Instructions

1. **Add canonical tags** — Every indexable page needs `<link rel="canonical" href="https://domain.com/exact-page-url">`.
2. **Use HTTPS in canonical** — Always point to the HTTPS version.
3. **Pick www or non-www** — Choose one and be consistent across canonical tags, sitemap, and internal links.
4. **Avoid conflicts** — If the sitemap lists URL-A but the canonical points to URL-B, search engines receive mixed signals. Align them.

---

## 10. Robots.txt Configuration

**Category:** Indexing & Discovery | **Impact:** High

Robots.txt controls which parts of the site search engine crawlers can access. Misconfiguration can block critical pages or waste crawl budget on low-value URLs.

### Checks

| # | Check | Pass Criteria | How to Verify |
|---|-------|--------------|---------------|
| 10.1 | Robots.txt exists | `domain.com/robots.txt` returns HTTP 200 | Navigate to `/robots.txt` in browser |
| 10.2 | Not blocking important pages | Key content pages are not disallowed | Review `Disallow` directives against important URLs |
| 10.3 | Sitemap reference present | `Sitemap: https://domain.com/sitemap.xml` directive included | Check robots.txt for `Sitemap:` line |
| 10.4 | Not overly permissive | Admin, login, and internal tool paths are blocked | Verify `Disallow` covers `/admin/`, `/login/`, `/wp-admin/`, etc. |
| 10.5 | Not overly restrictive | CSS, JS, and images are NOT blocked (allowed for rendering) | Verify no `Disallow` rules for `/css/`, `/js/`, `/images/` or `*.css` |

### Critical Warning

Blocking CSS, JS, or image files in robots.txt means Googlebot cannot render your pages properly. Google needs these resources to understand page layout, content, and user experience. Always allow access to render-critical resources.

### Fix Instructions

1. **Create robots.txt** — Place at domain root. Start with `User-agent: *` and add specific `Disallow` rules.
2. **Add sitemap reference** — Include `Sitemap: https://domain.com/sitemap.xml` at the end.
3. **Block low-value paths** — Disallow admin panels, search result pages, faceted navigation, and login pages.
4. **Allow rendering resources** — Never block CSS, JS, or image directories that Googlebot needs to render pages.

---

## 11. XML Sitemap Health

**Category:** Indexing & Discovery | **Impact:** High

The XML sitemap helps search engines discover and prioritize pages. A well-maintained sitemap accelerates indexing and signals which pages matter most.

### Checks

| # | Check | Pass Criteria | How to Verify |
|---|-------|--------------|---------------|
| 11.1 | Sitemap exists and accessible | Sitemap URL returns HTTP 200 with valid XML | Navigate to `/sitemap.xml`; check HTTP status |
| 11.2 | Valid XML | Proper XML syntax with correct namespace (`xmlns`) | Validate with XML validator or Screaming Frog |
| 11.3 | Contains key indexable pages | All important pages are listed | Cross-reference sitemap URLs with key page list |
| 11.4 | No non-indexable URLs | No noindex pages, redirected URLs, or 404 pages in sitemap | Crawl sitemap URLs, check status codes and meta robots |
| 11.5 | Under size limits | ≤ 50,000 URLs per file, ≤ 50MB per file | Check URL count and file size |
| 11.6 | Lastmod dates present and accurate | `<lastmod>` reflects actual content modification date | Compare lastmod with page content update dates |
| 11.7 | No priority tag waste | Priority tag absent or unused (Google ignores `<priority>`) | Review sitemap for `<priority>` tags — remove if present |
| 11.8 | Sitemap index for large sites | Sites with >50K URLs use a sitemap index file | Check if main sitemap references sub-sitemaps |
| 11.9 | Submitted to Google Search Console | Sitemap registered in GSC | Verify in Search Console → Sitemaps |

### Fix Instructions

1. **Generate sitemap** — Use CMS plugins (Yoast, Next.js sitemap) or tools like Screaming Frog to generate.
2. **Remove bad URLs** — Strip out noindexed, redirected, and 404 pages. Only include canonical, indexable URLs.
3. **Update lastmod** — Only update `<lastmod>` when page content actually changes. Google uses this to prioritize recrawling.
4. **Drop priority tags** — Google has confirmed it ignores `<priority>`. Remove to reduce file size.
5. **Submit to GSC** — Go to Search Console → Sitemaps → Add sitemap URL.

---

## 12. Internal Linking Strategy

**Category:** On-Page SEO | **Impact:** High

Internal links serve two critical functions: helping search engines discover pages and distributing PageRank (link equity) across the site. Orphan pages with no internal links are unlikely to rank.

### Checks

| # | Check | Pass Criteria | How to Verify |
|---|-------|--------------|---------------|
| 12.1 | Internal links present | Page links to ≥ 3 other pages on the site | Count internal links in page source |
| 12.2 | Descriptive anchor text | No "click here" or "read more" — anchors describe the target | Review anchor text of internal links |
| 12.3 | Links to related content | Internal links point to contextually relevant pages | Evaluate link targets for topical relevance |
| 12.4 | No orphan pages | Every page receives at least one internal link | Crawl site, check for pages with zero inlinks |
| 12.5 | Breadcrumb navigation | Nested pages have breadcrumb navigation | Check for breadcrumb markup on subpages |
| 12.6 | Reasonable link count | 5–15 contextual internal links per page (not excessive) | Count in-content internal links |
| 12.7 | Consistent URL format | Internal links use the same URL format (www vs non-www, trailing slash) | Inspect href values for consistency |
| 12.8 | No broken internal links | All internal links return HTTP 200 | Crawl site, check for 404s on internal links |

### Why It Matters

Internal links are the primary mechanism for page discovery and PageRank distribution. A well-linked page has a significantly higher chance of being crawled, indexed, and ranked than an orphan page.

### Fix Instructions

1. **Audit for orphan pages** — Use a crawler to find pages with zero internal links. Add contextual links from relevant pages.
2. **Improve anchor text** — Replace generic anchors with descriptive text that includes target keywords naturally.
3. **Add contextual links** — Within body content, link to related articles, services, or product pages.
4. **Implement breadcrumbs** — Use BreadcrumbList schema with visible breadcrumb navigation for nested page structures.
5. **Fix broken links** — Regularly crawl for 404s and update or redirect broken internal links.

---

## 13. Content Depth & Search Intent

**Category:** Content Quality | **Impact:** Critical

Content quality and search intent alignment are among the strongest ranking factors. Google's Helpful Content System rewards content created for users, not search engines.

### Checks

| # | Check | Pass Criteria | How to Verify |
|---|-------|--------------|---------------|
| 13.1 | Content length | ≥ 300 words minimum; ≥ 1000 words for competitive keywords | Word count tool or `document.body.innerText.split(' ').length` |
| 13.2 | Matches search intent | Content type matches the intent behind the target keyword | Search the keyword on Google, compare SERP results with page type |
| 13.3 | Comprehensive coverage | Topic covered in depth, not superficially | Compare with top-ranking competitors for completeness |
| 13.4 | Unique content | Not duplicated from other pages on the site or other sites | Use Copyscape or site-level duplicate check |
| 13.5 | Updated/fresh | Content updated within last 12 months, or clearly evergreen | Check publish/update dates; look for outdated information |
| 13.6 | Multimedia present | Includes images, video, infographics, or other media | Check for non-text content elements |
| 13.7 | Sources cited | Credible external sources referenced where appropriate | Look for outbound links to authoritative references |
| 13.8 | Readability | Written at grade 8–10 reading level | Hemingway Editor or Flesch-Kincaid readability test |
| 13.9 | Formatting | Short paragraphs (2–3 sentences), bullet points, bold key phrases | Visual review of content structure |
| 13.10 | No thin pages | No pages with minimal or stub content | Crawl site for pages with <100 words of content |

### Search Intent Types

| Intent | User Goal | Content Type |
|--------|-----------|-------------|
| Informational | Learn something | Guide, tutorial, explainer, wiki |
| Commercial | Compare options | Comparison page, review, "best of" list |
| Transactional | Complete an action | Product page, pricing page, signup form |
| Navigational | Find a specific site/page | Brand page, homepage, specific feature page |

### Fix Instructions

1. **Align with intent** — Search the target keyword, analyze the top 10 results, and match the content type Google is already ranking.
2. **Expand thin content** — Add depth, examples, data, and multimedia. Target comprehensiveness over word count.
3. **Update stale content** — Refresh statistics, update examples, fix broken links, add new sections.
4. **Improve formatting** — Break up walls of text with subheadings, bullets, numbered lists, and bold key takeaways.
5. **Cite sources** — Link to authoritative external sources to build credibility and demonstrate research depth.

---

## 14. Keyword Placement & Density

**Category:** On-Page SEO | **Impact:** Medium

Strategic keyword placement signals relevance to search engines without over-optimization. The goal is natural integration at key positions throughout the content.

### Checks

| # | Check | Pass Criteria | How to Verify |
|---|-------|--------------|---------------|
| 14.1 | Keyword in first 100 words | Primary keyword appears within the opening paragraph | Read the first 100 words |
| 14.2 | Keyword in H1, title, URL | Keyword present in all three primary elements | Check H1, title tag, and URL slug |
| 14.3 | Keyword density | 1–2% density (natural, not forced) | Count keyword occurrences / total words × 100 |
| 14.4 | LSI/semantic variants | Related terms and synonyms used throughout | Check for semantically related terms |
| 14.5 | No keyword stuffing | Keyword does not appear unnaturally or excessively | Read content aloud; check for awkward repetition |
| 14.6 | Secondary keywords | 2–3 additional relevant keywords targeted | Identify and verify secondary keyword presence |
| 14.7 | Long-tail variations | Long-tail keyword phrases included naturally | Check for question-based and conversational variants |

### Fix Instructions

1. **Place keyword early** — Mention the primary keyword in the first 100 words of the content body.
2. **Use semantic variations** — Don't repeat the exact keyword; use synonyms, related terms, and natural variations.
3. **Target 1–2% density** — For a 1000-word article, the primary keyword should appear 10–20 times naturally.
4. **Include long-tail phrases** — Add conversational, question-based keyword variations for voice search and AI engines.
5. **Avoid stuffing** — If the keyword feels forced when read aloud, rephrase. Google penalizes over-optimization.

---

## 15. Image Optimization

**Category:** On-Page SEO | **Impact:** Medium

Images impact page speed, accessibility, visual stability (CLS), and can rank in Google Image Search. Proper optimization covers all four aspects.

### Checks

| # | Check | Pass Criteria | How to Verify |
|---|-------|--------------|---------------|
| 15.1 | Alt text on all images | Every `<img>` has a descriptive `alt` attribute (not "image1") | Inspect images in DevTools or use Lighthouse |
| 15.2 | Keyword in alt text | At least one image has the target keyword in its alt text | Review alt attributes for keyword presence |
| 15.3 | Descriptive filenames | Image files named descriptively (not `IMG_4523.jpg`) | Check image `src` attributes for meaningful names |
| 15.4 | Images compressed | All images under 200KB; WebP format used where possible | DevTools Network tab — filter by images, check sizes |
| 15.5 | Responsive images | `srcset` attribute or CSS-based responsive images used | Check `<img>` tags for `srcset` or `<picture>` elements |
| 15.6 | Lazy loading | `loading="lazy"` on below-fold images | Inspect image tags for `loading` attribute |
| 15.7 | Width/height attributes | `width` and `height` set on images to prevent CLS | Check `<img>` tags for dimension attributes |

### Fix Instructions

1. **Add descriptive alt text** — Describe the image content: "Red Toyota Corolla parked in front of dealership" not "car" or "image1".
2. **Rename files** — Use descriptive, hyphenated filenames: `seo-audit-checklist-overview.webp`.
3. **Compress and convert** — Use WebP format for 25–50% savings. Compress with tools like Squoosh or Sharp.
4. **Add dimensions** — Set `width` and `height` on all `<img>` tags to reserve space and prevent layout shift.
5. **Lazy load** — Add `loading="lazy"` to all images below the fold. Do NOT lazy load the LCP image.
6. **Use responsive images** — Serve appropriate sizes for different viewports using `srcset` and `sizes` attributes.

---

## 16. Structured Data / Schema Markup

**Category:** Technical SEO | **Impact:** High

Structured data helps search engines understand page content and enables rich results (star ratings, FAQ dropdowns, recipe cards, etc.). Rich results significantly improve CTR.

### Checks

| # | Check | Pass Criteria | How to Verify |
|---|-------|--------------|---------------|
| 16.1 | Schema markup present | At least one schema type implemented | Check page source for `application/ld+json` scripts |
| 16.2 | Valid JSON-LD | No syntax errors in structured data | Google Rich Results Test or Schema Markup Validator |
| 16.3 | Appropriate type | Schema type matches page content | Verify schema type aligns with page purpose |
| 16.4 | Required properties filled | All required properties per schema.org spec are present | Rich Results Test shows no errors |
| 16.5 | BreadcrumbList implemented | Breadcrumb navigation has corresponding schema | Check for BreadcrumbList JSON-LD |
| 16.6 | Organization/LocalBusiness entity | Site-wide entity schema on homepage | Check homepage for Organization or LocalBusiness schema |
| 16.7 | Schema hierarchy correct | Nested schemas properly reference each other | Validate schema structure in testing tool |

### Common Schema Types by Page

| Page Type | Recommended Schema |
|-----------|--------------------|
| Homepage | Organization / LocalBusiness / WebSite with SearchAction |
| Blog post | Article + BreadcrumbList |
| Product page | Product with Offer + BreadcrumbList |
| FAQ page | FAQPage + BreadcrumbList |
| How-to guide | HowTo + BreadcrumbList |
| Local business | LocalBusiness with address, hours, reviews |
| Service page | Service + BreadcrumbList |
| Event page | Event + BreadcrumbList |

### Fix Instructions

1. **Implement JSON-LD** — Use `<script type="application/ld+json">` in the `<head>`. JSON-LD is Google's preferred format over Microdata or RDFa.
2. **Match schema to content** — Use Article for articles, Product for products, FAQPage for FAQs. Never misrepresent content type.
3. **Fill required fields** — Check schema.org documentation for required properties. Google's Rich Results Test shows what's missing.
4. **Add BreadcrumbList** — Implement on all pages with navigation hierarchy. Enables breadcrumb display in SERPs.
5. **Validate** — Test every page's schema using Google's Rich Results Test before deploying.

---

## 17. Indexability Signals

**Category:** Indexing & Discovery | **Impact:** Critical

If a page isn't indexed, it can't rank. Indexability issues are among the most damaging SEO problems because they completely prevent visibility.

### Checks

| # | Check | Pass Criteria | How to Verify |
|---|-------|--------------|---------------|
| 17.1 | No accidental noindex | `<meta name="robots" content="noindex">` is NOT present on pages that should be indexed | View source, search for "noindex" |
| 17.2 | No X-Robots-Tag noindex | HTTP header `X-Robots-Tag: noindex` is NOT present | Check response headers in DevTools Network tab |
| 17.3 | No contradictory signals | Page is not simultaneously blocked by robots.txt AND noindexed | Cross-reference robots.txt and meta robots |
| 17.4 | Canonical points to self | Canonical tag URL matches the page's own URL | Compare canonical href with current URL |
| 17.5 | Page in sitemap | Page URL is listed in the XML sitemap | Search sitemap file for the page URL |
| 17.6 | Page has internal links | At least one other page links to this page | Crawl site, check inbound internal link count |
| 17.7 | Content is substantial | Page is not a soft 404 (renders but has no real content) | Check word count, verify meaningful content exists |

### Fixes for "Discovered — Currently Not Indexed"

Google discovered the URL but hasn't crawled it yet. This means the page isn't interesting enough to prioritize.

1. Wait 7–10 days (new pages need time)
2. Improve the URL structure to be more descriptive
3. Update the title tag and meta description to be more compelling
4. Improve the page's content quality and depth
5. Add internal links from high-authority pages on the site

### Fixes for "Crawled — Currently Not Indexed"

Google crawled the page but decided not to index it. This is a quality signal.

1. Improve content quality and uniqueness — make it the best resource on the topic
2. Change the URL if current one is too generic
3. Add external backlinks from relevant sites
4. Improve overall site quality (rising tide lifts all boats)
5. Consolidate thin or duplicate pages into one comprehensive resource

---

## 18. Duplicate Content & Soft 404s

**Category:** Indexing & Discovery | **Impact:** High

Duplicate content dilutes ranking signals across multiple URLs. Soft 404s waste crawl budget on pages that appear to exist but have no useful content.

### Checks

| # | Check | Pass Criteria | How to Verify |
|---|-------|--------------|---------------|
| 18.1 | No duplicate page content | No two pages have substantially the same content | Crawl site, compare content similarity |
| 18.2 | No www/non-www duplicates | Only one variant accessible (other redirects) | Test both `www` and non-`www` URLs |
| 18.3 | No HTTP/HTTPS duplicates | Only HTTPS accessible (HTTP redirects) | Test both `http://` and `https://` URLs |
| 18.4 | No trailing-slash duplicates | Consistent trailing slash handling (one variant redirects to the other) | Test URLs with and without trailing slash |
| 18.5 | No soft 404 pages | Pages that return 200 but display error or empty content are properly 404ing | Check Search Console for soft 404 reports |
| 18.6 | Proper redirect chains | No redirect chains (A→B→C→D); maximum one redirect hop | Crawl site, check for chain redirects |
| 18.7 | Proper redirect types | 301 for permanently moved content, not 302 | Check redirect status codes with curl or crawler |

### Fix Instructions

1. **Canonicalize duplicates** — Choose one URL as canonical, redirect others with 301s, and set canonical tag.
2. **Enforce one domain variant** — Redirect www to non-www (or vice versa) with 301 at server level.
3. **Fix trailing slashes** — Pick one convention and redirect the other variant with 301.
4. **Fix soft 404s** — Return proper 404 status code for pages with no content. Or add real content.
5. **Flatten redirect chains** — Update all redirects to point directly to the final destination URL.
6. **Use 301 for permanent moves** — Only use 302 for genuinely temporary redirects.

---

## 19. Crawl Efficiency

**Category:** Technical SEO | **Impact:** Medium

Crawl efficiency determines how effectively Googlebot can discover and process your site's pages. Wasted crawl budget means important pages get crawled less frequently.

### Checks

| # | Check | Pass Criteria | How to Verify |
|---|-------|--------------|---------------|
| 19.1 | Server response under 1 second | TTFB < 1000ms for all important pages | WebPageTest, Lighthouse, or curl timing |
| 19.2 | Low 404 rate | Less than 5% of crawled URLs return 404 | Google Search Console coverage report |
| 19.3 | No crawl traps | No infinite URL patterns (e.g., calendar pages generating infinite future dates) | Review URL patterns in crawl stats |
| 19.4 | Important pages within 3 clicks | Key pages reachable within 3 clicks from homepage | Map site navigation depth |
| 19.5 | No unnecessary redirects | Internal links point to final URLs, not redirect chains | Crawl site for internal links that redirect |
| 19.6 | Clean URL parameters | No excessive URL parameters generating duplicate content | Review URL parameter handling in GSC |
| 19.7 | Crawl budget not wasted | robots.txt blocks low-value URLs (search results, filters, admin) | Review robots.txt disallow rules |
| 19.8 | Logical site hierarchy | Category > Subcategory > Page structure | Map information architecture |
| 19.9 | Flat architecture | Key pages within 3 levels of depth from homepage | Check crawl depth metrics |
| 19.10 | Custom 404 page | 404 page includes navigation and search to help users recover | Navigate to a non-existent URL, check 404 page |
| 19.11 | Proper pagination | Paginated content uses prev/next or load-more patterns | Check paginated sections for proper implementation |

### Fix Instructions

1. **Improve server response** — Optimize database queries, enable caching, use CDN, upgrade hosting if needed.
2. **Fix 404s** — Redirect broken URLs to relevant pages or return proper 404 with a helpful error page.
3. **Block crawl traps** — Use robots.txt to block infinite URL patterns (calendars, session IDs, faceted navigation).
4. **Flatten architecture** — Restructure navigation so key pages are within 3 clicks of the homepage.
5. **Create custom 404** — Design a 404 page with site navigation, search, and links to popular pages.
6. **Update internal links** — Point all internal links to final destination URLs, not URLs that redirect.
7. **Handle pagination** — Use `rel="next"` and `rel="prev"` for paginated series, or implement infinite scroll with proper URL handling.

---

## 20. Backlink & Authority Signals

**Category:** Off-Page | **Impact:** High

Backlinks remain one of Google's strongest ranking signals. Quality matters far more than quantity — one link from an authoritative, topically relevant site outweighs hundreds of low-quality links.

### Observable On-Page Checks

| # | Check | Pass Criteria | How to Verify |
|---|-------|--------------|---------------|
| 20.1 | Outbound link quality | Links to authoritative, reputable sources | Review outbound links for domain authority |
| 20.2 | Link relevance | Outbound links are topically related to the content | Check if linked pages are on-topic |
| 20.3 | Anchor text quality | Descriptive anchor text, not "click here" or naked URLs | Review anchor text of outbound links |
| 20.4 | No excessive outbound links | Page does not have 200+ outbound links (dilutes value) | Count outbound links |
| 20.5 | Follow vs nofollow appropriate | Authoritative outbound links are dofollow; untrusted/paid are nofollowed | Check `rel` attributes on outbound links |
| 20.6 | No paid link indicators | Paid/sponsored links use `rel="sponsored"` | Check for undisclosed paid links |

### Backlink Quality Factors

| Factor | Why It Matters |
|--------|----------------|
| Referring domain uniqueness | 1 link from 100 domains > 100 links from 1 domain |
| Link category/industry relevance | Topic-Sensitive PageRank weights relevant links more heavily |
| Anchor text relevance | Anchor text must match or relate to the target page topic |
| External link count on linking page | A page with 225 outbound links passes minimal value per link |
| Link position | Main content links > footer/sidebar links (Reasonable Surfer Model) |

### Additional Off-Page Checks

| # | Check | Pass Criteria | How to Verify |
|---|-------|--------------|---------------|
| 20.7 | Backlink diversity | Links from varied domains, not concentrated | Ahrefs, Moz, or Semrush backlink report |
| 20.8 | Anchor text variety | Natural mix of branded, exact-match, and generic anchors | Backlink tool anchor text report |
| 20.9 | No toxic backlinks | No links from spam, PBN, or penalized sites | Backlink audit tool; Google Disavow if needed |
| 20.10 | Social presence | Active social media profiles linked from/to the site | Check for social profile links and activity |
| 20.11 | Brand mentions | Site/brand mentioned across the web (linked or unlinked) | Google Alerts, brand mention monitoring tools |

### Fix Instructions

1. **Improve outbound links** — Link to authoritative sources (.edu, .gov, industry leaders) to demonstrate credibility.
2. **Earn quality backlinks** — Create linkable assets (original research, tools, comprehensive guides). Pursue relevant guest posts, digital PR, and resource page links.
3. **Diversify backlink profile** — Build links from varied domains, not just one type of source.
4. **Disavow toxic links** — Use Google's Disavow Tool for clearly spammy backlinks you can't get removed.
5. **Monitor anchor text** — Ensure a natural mix: ~40% branded, ~20% naked URL, ~20% generic, ~20% keyword-rich.

---

## 21. E-E-A-T Signals

**Category:** Content Quality | **Impact:** High

E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) is central to Google's Search Quality Evaluator Guidelines. While not a direct ranking factor, E-E-A-T signals influence how Google's algorithms assess content quality, especially for YMYL (Your Money, Your Life) topics.

### Checks

| # | Check | Pass Criteria | How to Verify |
|---|-------|--------------|---------------|
| 21.1 | Author identified | Content has a named author with visible credentials | Check for author byline on the page |
| 21.2 | Author bio/page | Author has a bio or dedicated page detailing expertise | Check for author bio section or link to author page |
| 21.3 | About page | Informative About Us/About page exists | Navigate to /about or About link in navigation |
| 21.4 | Contact information | Contact details clearly available (email, phone, address) | Check footer, contact page, or header for contact info |
| 21.5 | Trust signals | Privacy policy and terms of service pages exist and are linked | Check footer for privacy/terms links |
| 21.6 | External citations | Authoritative sources referenced and linked | Review content for outbound citations |
| 21.7 | Original research/experience | Case studies, original photos, personal insights, proprietary data | Look for first-hand experience indicators |
| 21.8 | Professional design | Site looks professional, not spammy or outdated | Visual assessment of design quality and polish |

### Fix Instructions

1. **Add author bylines** — Include author name, photo, and credentials on all content pages.
2. **Create author pages** — Dedicated pages for each author with bio, expertise, credentials, and links to their content.
3. **Build About page** — Explain who you are, your mission, team credentials, and why users should trust you.
4. **Display contact info** — Make contact details easily findable. Physical address adds trust for local businesses.
5. **Add trust pages** — Create and link to privacy policy, terms of service, and (if applicable) editorial guidelines.
6. **Cite sources** — Reference authoritative external sources to demonstrate research depth.
7. **Show experience** — Include case studies, original photography, personal anecdotes, and proprietary data that demonstrate first-hand experience.

---

## 22. AEO / Featured Snippet Readiness

**Category:** AEO | **Impact:** High

Answer Engine Optimization (AEO) prepares content for AI-powered search engines (Google AI Overview, Bing Chat, Perplexity, ChatGPT) and featured snippets. Well-structured content is more likely to be extracted and cited by AI systems.

### Checks

| # | Check | Pass Criteria | How to Verify |
|---|-------|--------------|---------------|
| 22.1 | Direct answer format | 40–60 word concise answers immediately following question headings | Check content structure after H2/H3 question headings |
| 22.2 | Paragraph snippet format | Standalone answer paragraphs that can be extracted independently | Test extracting paragraphs — do they make sense alone? |
| 22.3 | List snippet format | Ordered/unordered lists for step-by-step or enumerated content | Check for HTML list elements for procedural content |
| 22.4 | Table snippet format | Comparison data presented in HTML tables | Check for `<table>` elements with structured comparison data |
| 22.5 | Conversational tone | Natural language that sounds like how people actually speak/ask | Read content aloud to check for natural flow |
| 22.6 | People Also Ask coverage | Content addresses related questions users commonly ask | Search target keyword, compare PAA questions with content |
| 22.7 | Summary/TL;DR near top | Brief summary or key takeaways near the beginning of the content | Check for summary section in the first few paragraphs |
| 22.8 | Clear definitions | "X is..." format for key terms, enabling easy AI extraction | Check for definitional statements for key concepts |
| 22.9 | Structured answers | Answers formatted as paragraph, list, or table (not buried in prose) | Review answer formatting and extractability |

### Why This Works for AI Engines

RAG (Retrieval Augmented Generation) systems — used by AI search engines — chunk content, create vector embeddings, and retrieve semantically relevant chunks. Well-structured content with clear headings, concise answers, and logical organization creates better chunks and more accurate embeddings. This means your content is more likely to be retrieved and cited.

### Fix Instructions

1. **Use question headings** — Format H2s as questions: "What is SEO?", "How do I improve page speed?"
2. **Answer immediately** — Place a concise 40–60 word answer directly after each question heading.
3. **Use lists for steps** — Convert procedural content into ordered lists. Convert feature comparisons into unordered lists.
4. **Use tables for data** — Present comparisons, specifications, and multi-attribute data in HTML tables.
5. **Add a TL;DR** — Place a summary box or key takeaways section near the top of long-form content.
6. **Write definitions** — For key terms, use the format: "Term is [definition]." This is the most extractable format for AI.
7. **Cover PAA questions** — Search your target keyword, note the People Also Ask questions, and address them in your content.

---

## 23. FAQ Section & Schema

**Category:** AEO | **Impact:** High

FAQ sections target People Also Ask boxes, voice search queries, and AI answer extraction. Combined with FAQPage schema, they can earn rich results in SERPs.

### Checks

| # | Check | Pass Criteria | How to Verify |
|---|-------|--------------|---------------|
| 23.1 | FAQ section present | Relevant pages include a dedicated FAQ section | Scroll to bottom of page or check for FAQ section |
| 23.2 | FAQPage schema | JSON-LD FAQPage markup matches visible FAQ content | Check source for FAQPage JSON-LD; validate with Rich Results Test |
| 23.3 | Questions match real queries | Questions reflect actual user search queries, not fabricated | Compare questions with Google Autocomplete, PAA, and keyword tools |
| 23.4 | Answers concise | Each answer is 40–60 words | Measure answer length |
| 23.5 | Answers complete | Answers fully address the question (no "contact us for more info") | Read each answer — does it satisfy the question? |
| 23.6 | Natural language questions | Questions use conversational phrasing users would actually type/speak | Read questions aloud — do they sound natural? |
| 23.7 | HowTo schema for steps | Step-by-step content uses HowTo schema markup | Check for HowTo JSON-LD on how-to/tutorial pages |

### Fix Instructions

1. **Add FAQ sections** — Include 5–10 FAQs on key landing pages. Source questions from Google's PAA, Autocomplete, and customer support data.
2. **Implement FAQPage schema** — Add JSON-LD markup with `@type: FAQPage` containing `Question` and `Answer` pairs matching the visible content exactly.
3. **Use real questions** — Research what users actually ask. Use Google Autocomplete, AnswerThePublic, and your site's search logs.
4. **Keep answers concise but complete** — 40–60 words per answer. Answer the question fully without unnecessary filler.
5. **Add HowTo schema** — For tutorial/how-to content, use HowTo schema with step-by-step `HowToStep` items.

---

## 24. Video Content Optimization

**Category:** Content Quality | **Impact:** Medium

Video content can appear in Google Search, Google Video, and Discover. However, 90–95% of video indexing failures stem from improper page structure — specifically, embedding video on multipurpose pages instead of dedicated watch pages.

### Checks

| # | Check | Pass Criteria | How to Verify |
|---|-------|--------------|---------------|
| 24.1 | Video has a watch page | Video is the primary content on a dedicated page (not buried in a text article) | Check if the page is focused on the video or if video is secondary |
| 24.2 | VideoObject schema | JSON-LD with title, description, thumbnailUrl, uploadDate, duration | Check source for VideoObject JSON-LD; validate with Rich Results Test |
| 24.3 | Responsive video player | Video player scales to viewport width without overflow | Test video player at mobile widths |
| 24.4 | Video in main content area | Video is in the main content, not sidebar or footer | Check video position in page layout |
| 24.5 | One primary video per page | Google only indexes one video per page — the primary one should be first | Check if multiple videos exist; ensure the important one is first |

### Why Watch Pages Matter

90–95% of video indexing failures occur because the video is embedded in a multipurpose page (e.g., a blog post with text, images, AND a video). Google needs a dedicated watch page where the video is the primary content to properly index and rank the video in Video Search results.

### Fix Instructions

1. **Create watch pages** — For important videos, create a dedicated page where the video is the hero/primary content.
2. **Add VideoObject schema** — Include title, description, thumbnailUrl, uploadDate, duration, and contentUrl in JSON-LD.
3. **Make video responsive** — Use responsive embed techniques (`aspect-ratio` CSS or padding-bottom hack).
4. **Place video prominently** — The video should be above the fold, in the main content area, not buried below.
5. **One video per page** — If a page has multiple videos, ensure the most important one appears first in the DOM.

---

## 25. Page Experience & UX Signals

**Category:** Mobile + Content | **Impact:** Medium

Page experience encompasses Core Web Vitals, mobile-friendliness, HTTPS, and user interaction quality. Google uses page experience as a tiebreaker between similarly relevant results.

### Checks

| # | Check | Pass Criteria | How to Verify |
|---|-------|--------------|---------------|
| 25.1 | No intrusive popups | No full-screen popups on mobile, especially before content is visible | Test on mobile; check for popups on load |
| 25.2 | Easy navigation | Menu, breadcrumbs, and logical structure present | Manually navigate the site; check for clear pathways |
| 25.3 | Readable formatting | Short paragraphs (2–3 sentences), bullets, bold key phrases | Visual review of content formatting |
| 25.4 | Clear CTA on each page | Every page has a clear next action for the user | Identify the primary CTA on each page |
| 25.5 | No deceptive patterns | No dark patterns, fake buttons, misleading UI elements | Manual review for deceptive design |
| 25.6 | Accessible content | Sufficient color contrast, screen-reader friendly, keyboard navigable | Lighthouse accessibility audit; manual keyboard navigation test |
| 25.7 | No layout shift on interaction | Clicking buttons/links doesn't cause unexpected page jumps | Interact with page elements and observe for layout shifts |

### Fix Instructions

1. **Remove intrusive interstitials** — Replace full-screen popups with small banners or inline CTAs. Defer popups until after user scrolls or spends 30+ seconds.
2. **Improve navigation** — Add breadcrumbs, clear menu labels, and logical site hierarchy.
3. **Format for scanning** — Use subheadings every 200–300 words, bullet points for lists, bold for key phrases.
4. **Add clear CTAs** — Every page should have an obvious next step (buy, sign up, read more, contact).
5. **Eliminate dark patterns** — Remove fake urgency timers, misleading close buttons, pre-checked options, and hidden costs.
6. **Improve accessibility** — Ensure 4.5:1 color contrast ratio, add ARIA labels, test keyboard navigation.

---

## 26. Local SEO (If Applicable)

**Category:** Off-Page | **Impact:** High (for local businesses)

Only applicable for businesses with physical locations or defined service areas. Local SEO drives visibility in Google Maps, local pack results, and location-based searches.

### Checks

| # | Check | Pass Criteria | How to Verify |
|---|-------|--------------|---------------|
| 26.1 | Google Business Profile claimed | GBP listing is claimed and verified by the business owner | Search business name on Google Maps; check for "Claim this business" |
| 26.2 | GBP completeness | Hours, description, categories, photos, attributes all filled | Review GBP listing for completeness |
| 26.3 | NAP consistency | Name, Address, Phone identical across all online listings | Compare NAP on website, GBP, Yelp, BBB, social profiles |
| 26.4 | Local keywords in content | Location-based keywords used naturally in page content | Check for city, neighborhood, and region keywords |
| 26.5 | LocalBusiness schema | JSON-LD LocalBusiness schema with address, hours, phone | Check source for LocalBusiness JSON-LD |
| 26.6 | Active reviews with responses | Business has recent reviews and responds to them | Check GBP reviews section for recency and responses |
| 26.7 | Local citations | Business listed on Yelp, BBB, industry directories | Search for business on major directories |
| 26.8 | Unique location pages | Each service area/location has a dedicated page with unique content | Check for location-specific pages in site structure |
| 26.9 | Correct Google Maps pin | Map pin is at the correct physical location | Verify pin placement on Google Maps |
| 26.10 | Local content | Blog or content about local topics, events, or community | Check blog/content for local relevance |

### Fix Instructions

1. **Claim and verify GBP** — Go to business.google.com, claim the listing, and complete verification.
2. **Complete GBP profile** — Fill in all fields: hours, description, primary and secondary categories, photos (interior, exterior, team), attributes.
3. **Standardize NAP** — Use the exact same business name, address, and phone number everywhere online. No abbreviations on some and full words on others.
4. **Add local keywords** — Include city and neighborhood names naturally in titles, headings, and content.
5. **Implement LocalBusiness schema** — Add JSON-LD with address, geo coordinates, hours, phone, and business type.
6. **Manage reviews** — Encourage reviews from customers. Respond to all reviews (positive and negative) within 24–48 hours.
7. **Build citations** — List on Yelp, BBB, industry directories, local chambers of commerce, and data aggregators.
8. **Create location pages** — For multi-location businesses, create unique pages per location with location-specific content.

---

## Scoring Summary

Each check category contains multiple sub-checks. When auditing, classify each issue found by severity level.

### Severity Levels

| Severity | Points Deducted | Examples |
|----------|----------------|----------|
| Critical | -15 per issue | No HTTPS, accidental noindex on key pages, page returns 5xx, site not mobile-friendly |
| High | -8 per issue | Missing H1, no sitemap, no schema, thin content, broken canonical |
| Medium | -4 per issue | Meta description too long, missing alt text, slow LCP, missing author bio |
| Low | -2 per issue | URL contains underscores, missing HSTS header, no favicon |

### Issue Prioritization

Improvement points in the final audit report should be sorted by:

1. **Critical issues first** — Blocking ranking entirely (noindex, HTTPS, server errors)
2. **High-impact quick wins** — Easy fixes with big ranking impact (title tags, H1, canonical)
3. **High-impact efforts** — Significant work but significant reward (content depth, schema, backlinks)
4. **Medium-impact items** — Noticeable improvements (image optimization, meta descriptions, CWV)
5. **Low-impact polish items** — Minor refinements (URL formatting, HSTS, author bios)

### Score Interpretation

| Score Range | Rating | Meaning |
|-------------|--------|---------|
| 90–100 | Excellent | Well-optimized, minor tweaks only |
| 75–89 | Good | Strong foundation, some improvements needed |
| 60–74 | Fair | Significant gaps, prioritize fixes |
| 40–59 | Poor | Major issues blocking performance |
| 0–39 | Critical | Fundamental SEO problems, complete overhaul needed |

### Priority Matrix

|  | Quick Win | Moderate Effort | Major Effort |
|---|-----------|----------------|--------------|
| **High Impact** | P1 — Do first | P2 — Plan next | P3 — Roadmap |
| **Medium Impact** | P2 — Plan next | P3 — Roadmap | P4 — Backlog |
| **Low Impact** | P3 — Roadmap | P4 — Backlog | P5 — Skip |

Use this matrix to advise clients on implementation order. P1 items should be addressed immediately, P2 within the current sprint/month, P3 within the quarter, P4 when resources allow, and P5 only if all higher priorities are complete.
