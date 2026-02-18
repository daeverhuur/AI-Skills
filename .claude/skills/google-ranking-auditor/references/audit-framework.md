# Google Ranking Audit Framework

25 audit checks derived from Google Search Console expertise, covering the full pipeline: Discovery → Crawling → Rendering → Indexing → Ranking.

## Table of Contents
- [1. HTTPS & Security](#1-https--security)
- [2. Page Load Performance](#2-page-load-performance)
- [3. Core Web Vitals](#3-core-web-vitals)
- [4. Mobile Responsiveness](#4-mobile-responsiveness)
- [5. Title Tag Optimization](#5-title-tag-optimization)
- [6. Meta Description Quality](#6-meta-description-quality)
- [7. Header Hierarchy & Keywords](#7-header-hierarchy--keywords)
- [8. URL Structure](#8-url-structure)
- [9. Canonical Tag Implementation](#9-canonical-tag-implementation)
- [10. Robots.txt Configuration](#10-robotstxt-configuration)
- [11. XML Sitemap Health](#11-xml-sitemap-health)
- [12. Internal Linking Strategy](#12-internal-linking-strategy)
- [13. Content Depth & Search Intent](#13-content-depth--search-intent)
- [14. Keyword Placement & Density](#14-keyword-placement--density)
- [15. Image Optimization](#15-image-optimization)
- [16. Structured Data / Schema Markup](#16-structured-data--schema-markup)
- [17. Indexability Signals](#17-indexability-signals)
- [18. Duplicate Content & Soft 404s](#18-duplicate-content--soft-404s)
- [19. Crawl Efficiency](#19-crawl-efficiency)
- [20. Backlink & Authority Signals](#20-backlink--authority-signals)
- [21. E-E-A-T Signals](#21-e-e-a-t-signals)
- [22. AEO / Featured Snippet Readiness](#22-aeo--featured-snippet-readiness)
- [23. FAQ Section & Schema](#23-faq-section--schema)
- [24. Video Content Optimization](#24-video-content-optimization)
- [25. Page Experience & UX Signals](#25-page-experience--ux-signals)

---

## 1. HTTPS & Security

**Category:** Technical SEO | **Impact:** Critical

Google confirmed HTTPS is a ranking signal. HTTP pages are flagged as "Not Secure" in Chrome, hurting trust and CTR.

**Checks:**
| Check | Pass Criteria | How to Verify |
|-------|--------------|---------------|
| HTTPS enabled | Page loads over `https://` | Check URL bar |
| Valid SSL certificate | No browser security warnings | Check for lock icon |
| HTTP→HTTPS redirect | `http://` version 301-redirects to `https://` | Navigate to HTTP version |
| No mixed content | All resources (images, scripts, CSS) load over HTTPS | Check browser console for mixed content warnings |
| HSTS header present | `Strict-Transport-Security` in response headers | Read page headers via JS |

**Fix if failing:** Install/renew SSL certificate. Set up server-side 301 redirect from HTTP to HTTPS. Fix mixed content by updating resource URLs to HTTPS.

---

## 2. Page Load Performance

**Category:** Technical SEO | **Impact:** Critical

Server response time directly affects crawl budget allocation. Google's crawler makes fewer requests to slow sites. Target: <1000ms response time (ideal <500ms).

**Checks:**
| Check | Pass Criteria |
|-------|--------------|
| Server response time | Under 1 second (visible page load, not just TTFB) |
| Time to interactive | Page usable within 4 seconds |
| Render-blocking resources | No blocking JS/CSS in `<head>` without `defer`/`async` |
| Asset minification | CSS and JS files are minified |
| Image compression | No uncompressed images over 200KB |
| CDN usage | Static assets served from CDN (check asset domains) |
| Browser caching | Cache-Control headers on static resources |

**Fix if failing:** Enable server-side caching, use a CDN, defer non-critical JS, compress images to WebP, minify CSS/JS. For response times >1000ms, consider upgrading hosting.

**Why it matters (from GSC knowledge):** There is an inverse relationship between response time and crawl requests. Slow response → fewer crawl requests → slower indexing of new/updated content. Google allocates crawl budget based on server speed.

---

## 3. Core Web Vitals

**Category:** Technical SEO | **Impact:** High

Core Web Vitals are page experience ranking signals measured on real user data.

**Checks:**
| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| Largest Contentful Paint (LCP) | < 2.5s | 2.5-4.0s | > 4.0s |
| Cumulative Layout Shift (CLS) | < 0.1 | 0.1-0.25 | > 0.25 |
| Interaction to Next Paint (INP) | < 200ms | 200-500ms | > 500ms |

**How to check:** Use browser Performance API or observe: Does content shift after load? Does the main visual element load quickly? Do clicks respond instantly?

**Fix if failing:** LCP — optimize largest image/text block, preload hero image, reduce server time. CLS — set explicit width/height on images/embeds, avoid injecting content above fold. INP — reduce JS execution time, break long tasks.

**Why it matters:** Google uses mobile-first indexing. Mobile Core Web Vitals determine ranking eligibility. Poor CWV can suppress rankings even if content is excellent.

---

## 4. Mobile Responsiveness

**Category:** Mobile | **Impact:** Critical

Google crawls and indexes the mobile version of pages first (mobile-first indexing). A site that fails on mobile fails for Google.

**Checks:**
| Check | Pass Criteria |
|-------|--------------|
| Viewport meta tag | `<meta name="viewport" content="width=device-width, initial-scale=1">` present |
| Responsive layout | Content adapts to viewport without horizontal scroll |
| Readable text | Base font size ≥ 16px without zooming |
| Tap targets | Buttons/links ≥ 48px with adequate spacing |
| No intrusive interstitials | No full-screen popups blocking content on mobile |
| Mobile navigation | Menu is usable on small screens |

**Fix if failing:** Implement responsive CSS. Use relative units (%, vw, rem). Set viewport meta tag. Increase touch target sizes. Remove or minimize interstitials.

---

## 5. Title Tag Optimization

**Category:** On-Page SEO | **Impact:** High

The title tag is the most prominent element in search results and directly influences CTR and ranking relevance.

**Checks:**
| Check | Pass Criteria |
|-------|--------------|
| Title exists | Non-empty `<title>` tag in `<head>` |
| Length | 50-60 characters (not truncated in SERPs) |
| Primary keyword present | Target keyword appears in title |
| Keyword position | Primary keyword in first half of title |
| Unique | Not duplicated on other pages of the site |
| Compelling | Includes power words, numbers, or questions for CTR |

**Fix if failing:** Rewrite title to include primary keyword near the start, keep within 60 chars, make it click-worthy. Each page must have a unique title.

---

## 6. Meta Description Quality

**Category:** On-Page SEO | **Impact:** Medium

Meta descriptions don't directly affect ranking but significantly impact CTR, which indirectly affects ranking position.

**Checks:**
| Check | Pass Criteria |
|-------|--------------|
| Description exists | Non-empty `<meta name="description">` present |
| Length | 150-160 characters |
| Contains keyword | Target keyword appears naturally |
| Call-to-action | Includes actionable language ("Learn", "Discover", "Get") |
| Unique per page | Not duplicated across site |
| Not keyword-stuffed | Keyword appears max 1-2 times |

**Fix if failing:** Write a compelling 150-160 char description that includes the primary keyword and a CTA. Ensure it's unique per page.

---

## 7. Header Hierarchy & Keywords

**Category:** On-Page SEO | **Impact:** High

Headers structure content for users and search engines. Google uses headers to understand page topic hierarchy.

**Checks:**
| Check | Pass Criteria |
|-------|--------------|
| Single H1 | Exactly one `<h1>` tag on the page |
| H1 contains keyword | Primary keyword in the H1 |
| Logical hierarchy | H1 → H2 → H3, no skipped levels (e.g., H1 → H3) |
| H2 sections | Content divided into logical sections with H2 headings |
| Keywords in H2s | Secondary/related keywords in H2 subheadings |
| Question-based H2s (AEO) | At least some H2s formatted as questions matching "People Also Ask" |

**Fix if failing:** Restructure content with single H1 containing the primary keyword. Use H2s for major sections, H3s for subsections. Include question-format headings for AEO.

---

## 8. URL Structure

**Category:** On-Page SEO | **Impact:** Medium

Semantic URLs help Google understand page content and improve CTR in search results. From GSC knowledge: always use absolute URLs (not relative) to save Google a processing step.

**Checks:**
| Check | Pass Criteria |
|-------|--------------|
| Readable URL | Human-readable slug, no IDs or random parameters |
| Contains keyword | Primary keyword in URL path |
| Hyphens as separators | Words separated by `-` (not `_` or `%20`) |
| Lowercase | All lowercase characters |
| Short length | Under 75 characters total path |
| No query parameters | Clean URL without `?key=value` |
| Absolute URLs in links | Internal links use full absolute URLs, not relative paths |

**Fix if failing:** Restructure URL to be short, descriptive, keyword-containing, lowercase with hyphens. When linking internally, use complete absolute URLs (e.g., `https://example.com/page` not `/page`).

**Why absolute URLs matter:** Google's URL Resolver must convert relative URLs to absolute URLs before processing. Using absolute URLs directly saves Google a processing step and reduces ambiguity.

---

## 9. Canonical Tag Implementation

**Category:** Indexing & Discovery | **Impact:** High

Canonical tags tell Google which version of a page is the "master" version. Google treats canonical as a **hint**, not an instruction — it may override your choice based on other signals.

**Checks:**
| Check | Pass Criteria |
|-------|--------------|
| Canonical tag exists | `<link rel="canonical" href="...">` in `<head>` |
| Self-referencing canonical | Canonical points to the page's own URL |
| Consistent protocol | Canonical uses HTTPS (matches site protocol) |
| Consistent www/non-www | Canonical uses the same domain format site-wide |
| No conflicting signals | Sitemap, internal links, and canonical all agree on preferred URL |

**Fix if failing:** Add self-referencing canonical to every page. Ensure canonical URL matches: (1) the version in your sitemap, (2) the version your internal links point to, (3) the protocol (HTTPS) and domain format (www or non-www) used site-wide.

**Why consistency matters:** If your canonical says `https://example.com` but your internal links point to `https://www.example.com`, Google receives conflicting signals and may choose a different canonical than intended. Align all three: canonical + sitemap + internal links.

---

## 10. Robots.txt Configuration

**Category:** Indexing & Discovery | **Impact:** High

Robots.txt controls what Googlebot can **crawl** (not what it can index — that's noindex). Misconfigured robots.txt can block important content or waste crawl budget.

**Checks:**
| Check | Pass Criteria |
|-------|--------------|
| Robots.txt exists | File at `domain.com/robots.txt` returns 200 |
| Not blocking important pages | Key content pages not in `Disallow` rules |
| Sitemap reference | `Sitemap: https://domain.com/sitemap.xml` line present |
| Not overly permissive | Admin, login, and private directories blocked |
| Not overly restrictive | CSS, JS, and image directories allowed (needed for rendering) |

**Fix if failing:** Ensure robots.txt exists at the root domain. Allow crawling of CSS/JS/images (Googlebot needs them to render pages). Block admin panels, login pages, and internal search results. Add sitemap URL.

**Critical warning:** Blocking CSS/JS in robots.txt means Googlebot can't render your page properly. It will treat the page as having no content, killing your rankings.

---

## 11. XML Sitemap Health

**Category:** Indexing & Discovery | **Impact:** High

The sitemap is the primary method for Google to discover your URLs. It must be accurate, complete, and error-free.

**Checks:**
| Check | Pass Criteria |
|-------|--------------|
| Sitemap exists | `sitemap.xml` accessible at root or referenced in robots.txt |
| Valid XML | Well-formed XML with proper namespace |
| Contains key pages | All important indexable pages included |
| No non-indexable URLs | No noindex, redirected, or 404 URLs in sitemap |
| Under size limits | ≤ 50,000 URLs and ≤ 50MB per file |
| Lastmod dates | `<lastmod>` present and accurate (reflects real content changes) |
| No `<priority>` tag waste | Google ignores `<priority>` — remove to reduce file size |
| Sitemap index for large sites | Uses `sitemap_index.xml` when >50K URLs |

**Fix if failing:** Generate a clean XML sitemap containing only indexable pages. Remove 404s, redirects, and noindexed URLs. Add accurate `<lastmod>` dates. Reference in robots.txt. Submit to Google Search Console. Don't repeatedly resubmit — only after major site changes.

---

## 12. Internal Linking Strategy

**Category:** On-Page SEO | **Impact:** High

Internal links are one of the 10 methods Google uses to discover URLs. They also distribute PageRank authority throughout the site. Pages without internal links (orphan pages) are hard for both users and Google to find.

**Checks:**
| Check | Pass Criteria |
|-------|--------------|
| Internal links present | Page links to ≥3 other pages on the same site |
| Descriptive anchor text | Anchor text describes the destination (not "click here" or "read more") |
| Links to related content | Internal links are contextually relevant |
| No orphan pages | All important pages reachable from at least one other page |
| Breadcrumb navigation | Breadcrumbs present for nested pages |
| Reasonable link count | 5-15 contextual internal links per page |
| Consistent URL format | All internal links use the same protocol and www/non-www |
| No broken internal links | All internal links return 200 |

**Fix if failing:** Add 5-15 contextual internal links per content page using descriptive anchor text. Link from high-authority pages (homepage, popular content) to important new content. Check for orphan pages. Implement breadcrumbs for hierarchical sites.

**Why it matters:** Internal links serve dual purpose: (1) Discovery — new URLs found via internal links enter Google's URL Server queue for crawling. (2) Authority — PageRank flows through internal links, so linking from strong pages to weaker ones boosts the weaker page.

---

## 13. Content Depth & Search Intent

**Category:** Content Quality | **Impact:** Critical

Content must match search intent and be comprehensive enough to satisfy the user's query. Google measures content semantically through vector embeddings — keyword stuffing doesn't work, but topical coverage does.

**Checks:**
| Check | Pass Criteria |
|-------|--------------|
| Content length | ≥300 words (≥1000 for competitive keywords) |
| Matches search intent | Content type matches intent: informational → guide, transactional → product page, etc. |
| Comprehensive coverage | Topic thoroughly addressed, not superficial |
| Unique content | Not duplicated from other pages on site or web |
| Updated/fresh | Content dated within last 12 months or evergreen |
| Multimedia | At least 1 image, ideally video/infographic for depth |
| Sources cited | Claims backed by credible external sources |

**Fix if failing:** Analyze top-ranking pages for the target keyword to understand expected content type and depth. Expand content to cover the full topic. Ensure the content type matches the search intent (don't put a blog post where Google expects a product page). Add supporting multimedia. Cite authoritative sources.

**Intent types to match:**
- **Informational** ("how to..."): In-depth guides, how-tos, explainers
- **Commercial** ("best X for Y"): Comparison pages, reviews, listicles
- **Transactional** ("buy X", "X near me"): Product/service pages with clear CTAs
- **Navigational** ("brand name"): Homepage or specific brand page

---

## 14. Keyword Placement & Density

**Category:** On-Page SEO | **Impact:** Medium

Keywords signal relevance. From Google's indexing process: the indexer breaks content into words (HITs), assigns word IDs, and creates a forward index that maps document IDs to word IDs. Proper keyword placement ensures your page matches the right queries.

**Checks:**
| Check | Pass Criteria |
|-------|--------------|
| Keyword in first 100 words | Primary keyword appears early in content |
| Keyword in H1 | Present in the main heading |
| Keyword in title tag | Present in the page title |
| Keyword in URL | Present in the URL slug |
| Keyword density | 1-2% natural density across content |
| LSI/semantic variants | Related terms and synonyms present throughout |
| No keyword stuffing | Reads naturally, keyword not forced or repeated excessively |
| Long-tail variations | Natural long-tail phrases included |

**Fix if failing:** Place the primary keyword in: title tag, H1, first paragraph, URL, and meta description. Use semantic variants and related terms throughout the content. Aim for natural 1-2% density.

**Why semantic variants matter:** Google's lexicon system assigns word IDs to content. Pages that use diverse related terminology create richer associations in Google's barrel/sorter system, improving relevance scoring across more queries.

---

## 15. Image Optimization

**Category:** On-Page SEO | **Impact:** Medium

Images contribute to content quality and can rank in Google Images, driving additional traffic.

**Checks:**
| Check | Pass Criteria |
|-------|--------------|
| Alt text on all images | Every `<img>` has a descriptive `alt` attribute |
| Keyword in alt text | At least one image has target keyword in alt |
| Descriptive filenames | `dental-clinic-reception.jpg` not `IMG_4523.jpg` |
| Images compressed | Each image <200KB (use WebP format where possible) |
| Responsive images | `srcset` or CSS responsive sizing used |
| Lazy loading | Images below fold use `loading="lazy"` |
| Width/height attributes | `width` and `height` set to prevent layout shift (CLS) |

**Fix if failing:** Add descriptive alt text to all images. Compress images (TinyPNG, WebP conversion). Use `loading="lazy"` for below-fold images. Set explicit dimensions to prevent CLS.

---

## 16. Structured Data / Schema Markup

**Category:** Technical SEO | **Impact:** High

Structured data tells Google more about page content in a machine-readable format, enabling rich results (star ratings, FAQs, breadcrumbs, video thumbnails). Google's enhancements section in GSC only appears when structured data is detected.

**Checks:**
| Check | Pass Criteria |
|-------|--------------|
| Schema markup present | At least one structured data type implemented |
| Valid JSON-LD | No syntax errors in structured data |
| Appropriate type | Schema type matches content (Article, Product, LocalBusiness, FAQ, etc.) |
| Required properties filled | All required fields per schema.org specification populated |
| BreadcrumbList | Breadcrumb schema implemented for navigation |
| Organization/LocalBusiness | Site-wide entity schema present |
| Schema hierarchy correct | Follows schema.org hierarchy (e.g., EducationalOrganization is a type of Organization) |

**Fix if failing:** Add JSON-LD structured data matching the page content type. Start with BreadcrumbList site-wide + page-type specific schema. Validate with Google Rich Results Test. Follow schema.org hierarchy — don't use flat/disconnected schemas.

**Common schema types by page:**
- Homepage → Organization / LocalBusiness / WebSite with SearchAction
- Blog post → Article + BreadcrumbList
- Product page → Product with Offer + BreadcrumbList
- FAQ page → FAQPage + BreadcrumbList
- How-to guide → HowTo + BreadcrumbList
- Local business → LocalBusiness with address, hours, reviews

---

## 17. Indexability Signals

**Category:** Indexing & Discovery | **Impact:** Critical

A page can be discovered and crawled but still not indexed. Google's indexing decision depends on content quality, uniqueness, and explicit signals.

**Checks:**
| Check | Pass Criteria |
|-------|--------------|
| No accidental noindex | `<meta name="robots" content="noindex">` not present on pages meant for indexing |
| No X-Robots-Tag noindex | HTTP header doesn't contain `X-Robots-Tag: noindex` |
| Not blocked by robots.txt + noindex combo | Page isn't simultaneously blocked from crawling AND noindexed (Googlebot can't see the noindex if it can't crawl) |
| Canonical points to self | Canonical tag doesn't send index credit elsewhere |
| Page in sitemap | Important pages included in sitemap.xml |
| Page has internal links | Page reachable via internal link structure |
| Content is substantial | Not thin/empty content that Google would classify as soft 404 |

**Fix if failing:** Remove accidental noindex tags. Ensure canonical is self-referencing (or intentionally points to the correct master page). Include the page in the sitemap. Link to it from related pages. Add substantial, unique content.

**"Discovered Currently Not Indexed" fixes:** Wait 7-10 days (queue may be backed up). Improve URL to be more semantic. Update title and meta description. Improve content quality. Add internal links from authoritative pages.

**"Crawled Currently Not Indexed" fixes:** Improve content quality and uniqueness. Change URL if needed (resets Google's perception). Add external backlinks. Improve overall site quality (Google judges new pages based on site-wide quality).

---

## 18. Duplicate Content & Soft 404s

**Category:** Indexing & Discovery | **Impact:** High

Duplicate content confuses Google about which version to index. Soft 404s waste crawl budget on pages Google considers empty.

**Checks:**
| Check | Pass Criteria |
|-------|--------------|
| No duplicate page content | Page content doesn't substantially match another page on the site |
| No www/non-www duplicates | Site consistently uses one version; other 301-redirects |
| No HTTP/HTTPS duplicates | HTTP version redirects to HTTPS |
| No trailing-slash duplicates | `/page` and `/page/` resolve to same URL (one redirects to other) |
| No soft 404 pages | Pages with headers/footers but no main content don't return 200 (should be 404 or have content added) |
| Proper redirect chains | No long redirect chains (A→B→C→D); redirect directly to final destination |

**Fix if failing:** Implement canonical tags pointing to the preferred version. Set up 301 redirects for all URL variants. For soft 404s: either add real content or return actual 404 status. Break redirect chains by pointing directly to final destination.

---

## 19. Crawl Efficiency

**Category:** Technical SEO | **Impact:** Medium

For small sites (<100 pages), crawl budget rarely matters. For larger sites, inefficient crawling delays indexing of new and updated content.

**Checks:**
| Check | Pass Criteria |
|-------|--------------|
| Server response <1s | Fast server response for crawlers |
| Low 404 rate | Most crawled URLs return 200, minimal 404s |
| No crawl traps | No infinite URL patterns (e.g., calendar pagination, faceted navigation generating endless URLs) |
| Important pages shallow | Key pages within 3 clicks from homepage |
| No unnecessary redirects | Minimal redirect processing for crawler |
| Clean URL parameters | No crawlable URLs with sort/filter parameters that create duplicate content |
| Crawl budget not wasted | Robots.txt blocks low-value URLs (admin, search results, tag pages with no content) |

**Fix if failing:** Block low-value URL patterns in robots.txt. Fix or redirect 404 pages. Flatten site architecture so important pages are within 3 clicks. Eliminate infinite pagination and faceted navigation traps. Improve server speed.

**Key insight:** Google's URL Server schedules crawls based on priority. URLs from Search Console submissions get high priority. URLs discovered via random guessing get low priority. Make your important pages easily discoverable via sitemap and internal links.

---

## 20. Backlink & Authority Signals

**Category:** Off-Page | **Impact:** High

Backlinks remain a ranking factor but act as a tiebreaker when content quality is semantically equal. Quality and relevance matter far more than quantity.

**Observable checks (without third-party tools):**
| Check | What to Look For |
|-------|-----------------|
| Outbound link quality | Does the page link to authoritative, relevant external sources? |
| Link relevance | Are internal and external links topically related? |
| Anchor text quality | Are link anchors descriptive and relevant (not "click here")? |
| No excessive outbound links | Page doesn't have 200+ outbound links diluting value |
| Follow vs nofollow | Authoritative outbound links should be dofollow (signals trust) |
| No paid link indicators | No obvious sponsored links without `rel="sponsored"` |

**Backlink quality factors (from GSC expertise):**
1. **Referring domain uniqueness** — 1 link from 100 domains > 100 links from 1 domain
2. **Link category/industry relevance** — Links from your industry's category carry more weight (Topic-Sensitive PageRank)
3. **Anchor text relevance** — Anchor text must match the target page's topic. Wrong anchor text to wrong pages dilutes authority
4. **External link count on linking page** — A page with 225 outbound links passes minimal value per link
5. **Link position** — Links in main content > links in footer/sidebar (Reasonable Surfer Model)

**Fix if failing:** Improve outbound link quality by linking to authoritative sources. Use descriptive anchor text on all links. For backlink building: focus on getting links from industry-relevant, authoritative sites. Monitor for toxic/spam backlinks and disavow if necessary.

---

## 21. E-E-A-T Signals

**Category:** Content Quality | **Impact:** High

Experience, Expertise, Authoritativeness, Trustworthiness — Google's quality framework. Critical for YMYL (Your Money Your Life) topics.

**Checks:**
| Check | Pass Criteria |
|-------|--------------|
| Author identified | Content has named author with credentials |
| Author bio/page | Author has a bio or dedicated page with expertise details |
| About page | Site has an informative About Us page |
| Contact information | Clear contact details available |
| Trust signals | Privacy policy, terms of service present |
| External citations | Claims backed by cited authoritative sources |
| Original research/experience | Content shows first-hand experience or original data |
| Professional design | Site looks professional and trustworthy |

**Fix if failing:** Add author names and bios to content pages. Create About and Contact pages. Link to authoritative sources when making claims. Show first-hand experience through case studies, original photos, or personal insights.

---

## 22. AEO / Featured Snippet Readiness

**Category:** AEO | **Impact:** High

Optimize content to be selected as the direct answer by Google's featured snippets, AI Mode, AI Overviews, and LLM-based search (ChatGPT, Perplexity). AEO is not a separate discipline — it is SEO done with structure and clarity.

**Checks:**
| Check | Pass Criteria |
|-------|--------------|
| Direct answer format | Questions answered concisely in the first sentence after each heading (40-60 words) |
| Paragraph snippet format | Key definitions/answers in standalone paragraphs |
| List snippet format | Step-by-step content uses ordered/unordered lists |
| Table snippet format | Comparison data in HTML tables |
| Conversational tone | Content written naturally, as if answering a question |
| People Also Ask coverage | Content addresses related questions from PAA |
| Summary/TL;DR | Page includes a brief summary near the top for quick extraction |
| Clear definitions | Key terms defined explicitly ("X is...") for AI extraction |

**Fix if failing:** Restructure content so every question heading is followed by a direct 40-60 word answer in the first sentence. Use lists for processes, tables for comparisons. Add a summary section near the top. Write in a conversational, clear tone. Cover related PAA questions.

**Why this works for AI engines:** RAG systems (like Perplexity) chunk your content, create vector embeddings, and retrieve the most semantically relevant chunks. Well-structured content with clear answers creates better chunks and better embeddings, making your content more likely to be selected.

---

## 23. FAQ Section & Schema

**Category:** AEO | **Impact:** High

FAQ sections serve double duty: they capture long-tail traffic AND make content eligible for FAQ rich results in Google Search.

**Checks:**
| Check | Pass Criteria |
|-------|--------------|
| FAQ section present | Dedicated Q&A section on relevant pages |
| FAQPage schema | `@type: FAQPage` JSON-LD markup on FAQ content |
| Questions match real queries | Questions reflect actual search queries (not made up) |
| Answers are concise | 40-60 words per answer for snippet eligibility |
| Answers are complete | Each answer fully addresses the question |
| Questions use natural language | Phrased how users actually search ("How do I..." not "How does one...") |

**Fix if failing:** Add an FAQ section to key pages with 5-8 questions based on real search queries (check People Also Ask, Google autocomplete). Implement FAQPage schema in JSON-LD. Keep answers concise but complete.

---

## 24. Video Content Optimization

**Category:** Content Quality | **Impact:** Medium

Video content can appear in Google Video Search and as rich results with thumbnails, but only if properly implemented.

**Checks:**
| Check | Pass Criteria |
|-------|--------------|
| Video has a watch page | Each important video has a dedicated page where the video is the **primary** content element |
| Video schema markup | `VideoObject` schema with title, description, thumbnailUrl, uploadDate, duration |
| Responsive video | Video player adapts to viewport size |
| Video in main content | Video is positioned within main content area, not just sidebar |
| One primary video per page | Only one video targeted for indexing per page (Google only indexes one) |

**Fix if failing:** Create dedicated watch pages for each important video — pages where the video is the main purpose, not a side element in a blog post. Add VideoObject schema. The same video can be embedded on multiple pages, but only the watch page will get the video rich result.

**Why watch pages matter:** Embedding a video in a multipurpose page (blog + testimonials + text) won't get it indexed in video search. Google needs a page where the primary purpose is watching the video. This is the #1 cause (90-95%) of video indexing failures.

---

## 25. Page Experience & UX Signals

**Category:** Mobile + Content | **Impact:** Medium

Aggregate check covering user experience signals that influence both ranking and user behavior metrics.

**Checks:**
| Check | Pass Criteria |
|-------|--------------|
| No intrusive popups | No full-screen interstitials on page load (especially mobile) |
| Easy navigation | Clear menu, breadcrumbs, logical site structure |
| Readable formatting | Short paragraphs, bullet points, bold key phrases |
| Clear CTA | Each page has a clear next step for the user |
| No deceptive patterns | No dark patterns, fake buttons, or misleading ads |
| Accessible content | Adequate color contrast, screen-reader friendly structure |
| No layout shift on interaction | Clicking buttons/links doesn't cause unexpected page movement |

**Fix if failing:** Remove or minimize popups/interstitials. Improve content formatting with short paragraphs, bullet points, and visual hierarchy. Add clear navigation and CTAs. Ensure adequate color contrast and accessible HTML structure.

---

## Scoring Summary

Each of the 25 checks above contains multiple sub-checks. Evaluate every sub-check and classify issues as:

| Severity | Points Deducted | Examples |
|----------|----------------|----------|
| Critical | -15 per issue | No HTTPS, accidental noindex on key pages, page returns 5xx |
| High | -8 per issue | Missing H1, no sitemap, no schema, thin content |
| Medium | -4 per issue | Meta description too long, missing alt text, slow LCP |
| Low | -2 per issue | URL contains underscores, missing author bio |

**The 20+ improvement points in the final report should be sorted by:**
1. Critical issues first (blocking ranking entirely)
2. High-impact quick wins (easy fixes with big ranking impact)
3. High-impact efforts (significant work but significant reward)
4. Medium-impact items
5. Low-impact polish items
