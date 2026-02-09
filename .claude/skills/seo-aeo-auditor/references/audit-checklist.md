# SEO/AEO Audit Checklist

## Table of Contents
- [On-Page SEO Checks](#on-page-seo-checks)
- [Technical SEO Checks](#technical-seo-checks)
- [Content Quality Checks](#content-quality-checks)
- [Off-Page SEO Checks](#off-page-seo-checks)
- [AEO Checks](#aeo-checks)
- [Local SEO Checks](#local-seo-checks)
- [Mobile SEO Checks](#mobile-seo-checks)
- [Scoring Framework](#scoring-framework)

---

## On-Page SEO Checks

### Title Tags
| Check | Pass Criteria | Impact |
|-------|--------------|--------|
| Title exists | Non-empty `<title>` tag present | critical |
| Title length | 50-60 characters | high |
| Primary keyword in title | Target keyword within first 60 chars | high |
| Keyword near beginning | Primary keyword in first half of title | medium |
| Unique per page | No duplicate titles across site | high |
| Compelling/clickable | Action-oriented, includes numbers or questions | medium |
| Brand name included | Brand appended where appropriate | low |

### Meta Descriptions
| Check | Pass Criteria | Impact |
|-------|--------------|--------|
| Description exists | Non-empty meta description tag | high |
| Description length | 150-160 characters | medium |
| Contains primary keyword | Target keyword included naturally | medium |
| Unique per page | No duplicate descriptions across site | medium |
| Call-to-action | Includes actionable language | low |
| Not keyword-stuffed | Keyword appears max 1-2 times | medium |

### Header Tags
| Check | Pass Criteria | Impact |
|-------|--------------|--------|
| Single H1 | Exactly one H1 per page | critical |
| H1 contains keyword | Primary keyword in H1 | high |
| H1 matches title intent | H1 aligns with page title topic | medium |
| Logical hierarchy | H1 > H2 > H3, no skipped levels | medium |
| H2s for sections | Content divided with H2 subheadings | medium |
| Keywords in H2s | Secondary keywords in subheadings | low |
| Header length | 20-70 characters per header | low |

### URL Structure
| Check | Pass Criteria | Impact |
|-------|--------------|--------|
| Readable URL | Human-readable slug, no IDs/params | medium |
| Contains keyword | Primary keyword in URL path | medium |
| Hyphens as separators | Words separated by hyphens (not underscores) | medium |
| Lowercase | All lowercase characters | low |
| Short length | Under 75 characters total | low |
| No parameters | Clean URL without ?key=value strings | low |
| Canonical tag | `<link rel="canonical">` pointing to self or preferred | high |

### Images
| Check | Pass Criteria | Impact |
|-------|--------------|--------|
| Alt text present | All `<img>` tags have alt attributes | high |
| Descriptive alt text | Alt text describes image content (not "image1") | medium |
| Keywords in alt text | Target keyword in at least one image alt | low |
| Descriptive filenames | `banana-bread.jpg` not `img_123.jpg` | low |
| Images compressed | File sizes optimized for web | high |
| Responsive images | `srcset` or responsive sizing used | medium |
| Lazy loading | Images below fold use lazy loading | medium |

### Internal Linking
| Check | Pass Criteria | Impact |
|-------|--------------|--------|
| Internal links present | Page links to other site pages | high |
| Descriptive anchors | Anchor text describes destination (not "click here") | medium |
| Links to related content | Links contextually relevant | medium |
| No broken internal links | All internal links resolve (200 status) | high |
| Reasonable link count | 5-10 contextual internal links per page | low |
| Breadcrumb navigation | Breadcrumbs present for nested pages | medium |

### Keyword Usage
| Check | Pass Criteria | Impact |
|-------|--------------|--------|
| Keyword in first 100 words | Primary keyword appears early in content | high |
| Keyword density | 1-2% density, naturally distributed | medium |
| LSI/semantic keywords | Related terms and synonyms present | medium |
| No keyword stuffing | Natural reading flow maintained | critical |
| Secondary keywords | 2-3 additional keywords targeted | medium |
| Long-tail variations | Natural long-tail phrases included | low |

---

## Technical SEO Checks

### Security & Protocol
| Check | Pass Criteria | Impact |
|-------|--------------|--------|
| HTTPS enabled | Site served over HTTPS with valid SSL | critical |
| HTTP redirects to HTTPS | All HTTP URLs 301 redirect to HTTPS | high |
| HSTS header | Strict-Transport-Security header present | medium |
| No mixed content | All resources loaded over HTTPS | high |

### Performance (Core Web Vitals)
| Check | Pass Criteria | Impact |
|-------|--------------|--------|
| Page load time | Under 4 seconds | critical |
| Largest Contentful Paint | LCP under 2.5 seconds | high |
| First Contentful Paint | FCP under 2 seconds | high |
| Cumulative Layout Shift | CLS under 0.1 | high |
| Interaction to Next Paint | INP under 200ms | high |
| Image optimization | Images compressed, correct format | high |
| Caching enabled | Browser caching headers present | medium |
| CDN usage | Static assets served via CDN | medium |
| Minified assets | CSS/JS minified | medium |
| Render-blocking resources | Critical CSS inlined, JS deferred | medium |

### Crawling & Indexing
| Check | Pass Criteria | Impact |
|-------|--------------|--------|
| Robots.txt exists | Valid robots.txt at root | high |
| Robots.txt not blocking important pages | Key pages not disallowed | critical |
| XML sitemap exists | Sitemap.xml present and valid | high |
| Sitemap submitted | Submitted to Google Search Console | high |
| Sitemap accurate | Contains all indexable URLs | medium |
| No orphan pages | All pages reachable via internal links | medium |
| Canonical tags | Canonical URLs specified correctly | high |
| No duplicate content | No substantial duplicate pages | high |
| Proper redirects | 301s for moved content (not 302s) | medium |
| No broken links | No 4xx/5xx responses | high |
| Crawl depth | Important pages within 3 clicks of home | medium |

### Structured Data / Schema
| Check | Pass Criteria | Impact |
|-------|--------------|--------|
| Schema markup present | At least one schema type implemented | high |
| Schema valid | Passes Google Rich Results Test | high |
| Appropriate schema type | Matches content (Article, Product, FAQ, etc.) | medium |
| Required properties | All required schema fields populated | medium |
| BreadcrumbList schema | Breadcrumb schema for navigation | medium |
| Organization schema | Company/site-wide schema present | low |

### Site Architecture
| Check | Pass Criteria | Impact |
|-------|--------------|--------|
| Logical hierarchy | Clear category > subcategory > page structure | medium |
| Flat architecture | Key pages within 3 levels of root | medium |
| Consistent navigation | Same nav structure across pages | low |
| 404 page exists | Custom 404 with navigation options | low |
| Pagination | Proper prev/next or load-more patterns | medium |

---

## Content Quality Checks

| Check | Pass Criteria | Impact |
|-------|--------------|--------|
| Content length | 300+ words (1000+ for competitive keywords) | high |
| Answers search intent | Content matches what user searches for | critical |
| Unique content | No duplicate or thin content | critical |
| Readability | Grade 8-10 reading level for general audience | medium |
| Formatting | Short paragraphs, bullets, bold key phrases | medium |
| Multimedia | Images, videos, or infographics included | medium |
| Freshness | Updated within last 12 months | medium |
| E-E-A-T signals | Author bio, credentials, citations, experience | high |
| Sources cited | Claims backed by credible sources | medium |
| Call-to-action | Clear next step for user | low |
| No thin pages | No pages with minimal/no content | high |
| Comprehensive coverage | Topic fully addressed | high |

---

## Off-Page SEO Checks

| Check | Pass Criteria | Impact |
|-------|--------------|--------|
| Backlink profile | Links from relevant, authoritative domains | high |
| Backlink diversity | Links from varied domains (not just one) | medium |
| Anchor text variety | Natural mix of anchor text types | medium |
| No toxic backlinks | No links from spam/penalized sites | high |
| Social presence | Active social media profiles linked | low |
| Brand mentions | Mentions across web (linked or unlinked) | low |
| Local citations | NAP consistent across directories (if local) | high |
| Google Business Profile | Complete, optimized GBP (if local) | high |

---

## AEO Checks (Answer Engine Optimization)

| Check | Pass Criteria | Impact |
|-------|--------------|--------|
| FAQ section present | Q&A section on relevant pages | high |
| FAQ schema markup | FAQPage schema implemented | high |
| Featured snippet format | Content structured for position zero (40-60 word answers, lists, tables) | high |
| Conversational tone | Content written in natural language | medium |
| Question-based headings | H2/H3s formatted as questions users ask | high |
| Direct answers | Questions answered concisely in first sentence | high |
| People Also Ask coverage | Related questions addressed in content | medium |
| HowTo schema | Step-by-step content has HowTo markup | medium |
| Voice search ready | Conversational, long-tail keyword targeting | medium |
| Structured answers | Answers in paragraph, list, or table format | medium |
| Definition format | Key terms defined clearly for AI extraction | medium |

---

## Local SEO Checks

Only applicable for businesses with physical locations or service areas.

| Check | Pass Criteria | Impact |
|-------|--------------|--------|
| Google Business Profile | Claimed and verified | critical |
| GBP completeness | All fields filled (hours, description, categories, photos) | high |
| NAP consistency | Name, Address, Phone identical everywhere | high |
| Local keywords | Location-based keywords in content | high |
| Local schema | LocalBusiness schema implemented | high |
| Reviews | Active review profile with responses | high |
| Local citations | Listed in relevant directories (Yelp, BBB, industry) | medium |
| Location pages | Unique pages for each service area | medium |
| Google Maps | Correct pin location on map | medium |
| Local content | Blog/content about local topics | low |

---

## Mobile SEO Checks

| Check | Pass Criteria | Impact |
|-------|--------------|--------|
| Responsive design | Layout adapts to all screen sizes | critical |
| Mobile-friendly test | Passes Google Mobile-Friendly Test | critical |
| Viewport configured | `<meta name="viewport">` tag present | critical |
| Touch-friendly | Buttons/links have adequate tap targets (48px+) | high |
| Readable text | Font size 16px+ without zooming | high |
| No horizontal scroll | Content fits viewport width | high |
| Fast mobile load | Under 3 seconds on 4G | high |
| No intrusive interstitials | No full-screen popups on mobile | medium |
| Mobile navigation | Accessible, usable menu on small screens | medium |

---

## Scoring Framework

### Category Weights
| Category | Weight | Description |
|----------|--------|-------------|
| Technical SEO | 25% | Infrastructure, speed, crawlability |
| On-Page SEO | 25% | Tags, structure, keyword optimization |
| Content Quality | 20% | Depth, relevance, freshness, E-E-A-T |
| AEO Readiness | 15% | AI/voice search optimization |
| Off-Page/Links | 10% | Backlinks, social signals, authority |
| Mobile | 5% | Mobile experience (already weighted in technical) |

### Impact Scoring
- **Critical** issues: -15 points each (from 100 baseline)
- **High** impact issues: -8 points each
- **Medium** impact issues: -4 points each
- **Low** impact issues: -2 points each

### Score Interpretation
| Score Range | Rating | Meaning |
|-------------|--------|---------|
| 90-100 | Excellent | Well-optimized, minor tweaks only |
| 75-89 | Good | Strong foundation, some improvements needed |
| 60-74 | Fair | Significant gaps, prioritize fixes |
| 40-59 | Poor | Major issues blocking performance |
| 0-39 | Critical | Fundamental SEO problems, complete overhaul needed |

### Priority Matrix
Issues are prioritized by: Impact (high/medium/low) x Effort (quick-win/moderate/major)

| | Quick Win | Moderate Effort | Major Effort |
|---|-----------|----------------|--------------|
| **High Impact** | P1 - Do first | P2 - Plan next | P3 - Roadmap |
| **Medium Impact** | P2 - Plan next | P3 - Roadmap | P4 - Backlog |
| **Low Impact** | P3 - Roadmap | P4 - Backlog | P5 - Skip |
