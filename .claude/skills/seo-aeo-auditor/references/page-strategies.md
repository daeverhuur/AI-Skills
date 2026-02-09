# SEO Page Strategy Guide

## Table of Contents
- [Page Types for SEO](#page-types-for-seo)
- [Page Suggestion Framework](#page-suggestion-framework)
- [Content Pillars & Clusters](#content-pillars--clusters)
- [Keyword-to-Page Mapping](#keyword-to-page-mapping)
- [Schema Recommendations by Page Type](#schema-recommendations-by-page-type)

---

## Page Types for SEO

### Landing Pages
- **Purpose**: Convert visitors for specific keywords or campaigns
- **Target**: Transactional and commercial keywords
- **Structure**: Hero section, benefits, social proof, CTA
- **Word count**: 500-1500 words
- **Schema**: Product, Service, or Organization

### Blog / Article Pages
- **Purpose**: Target informational keywords, build authority
- **Target**: Informational and question-based keywords
- **Structure**: Introduction, H2 sections, conclusion, FAQ
- **Word count**: 1000-2500 words
- **Schema**: Article, BlogPosting, FAQPage

### Product Pages
- **Purpose**: Showcase individual products for transactional searches
- **Target**: Product-specific keywords, "buy X" queries
- **Structure**: Product details, images, reviews, specifications, FAQ
- **Word count**: 300-800 words + specs
- **Schema**: Product with offers, reviews, aggregateRating

### Category / Collection Pages
- **Purpose**: Target broader category-level keywords
- **Target**: Category keywords, "best X" queries
- **Structure**: Category description, filtered product/content grid
- **Word count**: 300-500 intro + listings
- **Schema**: CollectionPage, ItemList

### Location Pages
- **Purpose**: Rank for local/geographic keywords
- **Target**: "[service] in [city]" keywords
- **Structure**: Local content, address, hours, reviews, map
- **Word count**: 500-1000 words unique per location
- **Schema**: LocalBusiness, GeoCoordinates

### FAQ Pages
- **Purpose**: Capture question-based searches, support AEO
- **Target**: "how to", "what is", "why" queries
- **Structure**: Question-answer pairs, grouped by topic
- **Word count**: 200+ chars per answer
- **Schema**: FAQPage (critical)

### Comparison Pages
- **Purpose**: Capture "[X] vs [Y]" and "best [category]" searches
- **Target**: Comparison and commercial investigation keywords
- **Structure**: Feature comparison table, pros/cons, verdict
- **Word count**: 1500-3000 words
- **Schema**: Article, Table markup

### Glossary / Definition Pages
- **Purpose**: Capture "what is [term]" searches, support AEO
- **Target**: Definitional keywords in your niche
- **Structure**: Term definition, explanation, examples, related terms
- **Word count**: 300-800 words per term
- **Schema**: DefinedTerm, FAQPage

### Hub / Pillar Pages
- **Purpose**: Central authority page for a topic cluster
- **Target**: Broad, high-volume head terms
- **Structure**: Comprehensive overview linking to subtopic pages
- **Word count**: 2000-5000 words
- **Schema**: Article, BreadcrumbList

### How-To / Tutorial Pages
- **Purpose**: Capture procedural search queries
- **Target**: "how to [action]" keywords
- **Structure**: Step-by-step instructions with images/video
- **Word count**: 1000-2000 words
- **Schema**: HowTo (critical for AEO/rich snippets)

---

## Page Suggestion Framework

When analyzing an app/site for SEO page opportunities, evaluate these dimensions:

### 1. Keyword Gap Analysis
- Identify high-volume keywords the site doesn't rank for
- Find keywords competitors rank for but you don't
- Look for emerging/trending keywords in the niche
- Check "People Also Ask" for uncovered questions

### 2. Search Intent Coverage
Ensure pages exist for all four intent types:
- **Informational**: "what is X", "how to Y", "guide to Z"
- **Navigational**: Brand terms, product names
- **Commercial**: "best X", "X vs Y", "X reviews"
- **Transactional**: "buy X", "X pricing", "X signup"

### 3. Funnel Stage Coverage
- **Awareness**: Educational blog posts, guides, glossary
- **Consideration**: Comparison pages, case studies, reviews
- **Decision**: Product pages, pricing, testimonials, demos
- **Retention**: Help docs, tutorials, community content

### 4. Content Cluster Gaps
- Map existing content into topic clusters
- Identify clusters without a pillar page
- Find pillar pages without supporting content
- Look for orphaned content not in any cluster

### 5. Local Opportunity Assessment
- Does the business serve specific areas? Create location pages
- Are there "near me" keywords being missed?
- Is Google Business Profile optimized?

### 6. AEO Opportunity Assessment
- Which pages could have FAQ sections added?
- Are there "People Also Ask" questions without answers?
- Can existing content be restructured for featured snippets?
- Are HowTo pages missing schema markup?

---

## Content Pillars & Clusters

### Structure
```
Pillar Page (broad topic, 2000-5000 words)
├── Cluster Page 1 (subtopic, 1000-2000 words)
├── Cluster Page 2 (subtopic, 1000-2000 words)
├── Cluster Page 3 (subtopic, 1000-2000 words)
├── FAQ Page (questions about the topic)
└── Glossary entries (key terms)
```

### Interlinking Rules
- Every cluster page links back to its pillar page
- Pillar page links to all cluster pages
- Related cluster pages interlink horizontally
- Use descriptive anchor text with target keywords

### Example: SaaS Product
```
Pillar: "Complete Guide to Project Management"
├── "Agile vs Waterfall: Which Methodology is Right?"
├── "How to Create a Project Timeline"
├── "10 Best Project Management Tools Compared"
├── "Project Management for Remote Teams"
├── FAQ: "Project Management Questions Answered"
└── Glossary: Sprint, Kanban, Scrum, Milestone, etc.
```

---

## Keyword-to-Page Mapping

### Assignment Rules
- One primary keyword per page
- 2-3 secondary keywords per page
- Multiple long-tail variations per page
- No two pages should target the same primary keyword (cannibalization)

### Mapping Template
For each suggested page, provide:
```
Page: [page title]
Primary Keyword: [main keyword] (volume: X, difficulty: X)
Secondary Keywords: [kw1], [kw2]
Long-tail Keywords: [phrase1], [phrase2], [phrase3]
Search Intent: informational|commercial|transactional|navigational
Content Type: blog|landing|product|category|faq|comparison|glossary|hub|howto|location
Estimated Word Count: X words
Suggested Schema: [schema type]
Internal Links From: [existing pages that should link here]
Internal Links To: [pages this should link to]
```

---

## Schema Recommendations by Page Type

| Page Type | Primary Schema | Secondary Schema |
|-----------|---------------|-----------------|
| Blog / Article | Article, BlogPosting | FAQPage, BreadcrumbList |
| Product | Product (with Offer, Review) | BreadcrumbList, FAQPage |
| Category | CollectionPage, ItemList | BreadcrumbList |
| FAQ | FAQPage | BreadcrumbList |
| How-To | HowTo | FAQPage, BreadcrumbList |
| Location | LocalBusiness | GeoCoordinates, BreadcrumbList |
| Comparison | Article | FAQPage, Table |
| Landing | Service, Product | Organization, FAQPage |
| Glossary | DefinedTerm | BreadcrumbList |
| Hub/Pillar | Article | BreadcrumbList, FAQPage |
| Home | WebSite, Organization | SiteNavigationElement |

### Schema Priority
1. Always implement BreadcrumbList site-wide
2. FAQPage on any page with Q&A content
3. Page-type-specific schema (Product, Article, etc.)
4. Organization schema on home/about pages
5. HowTo for any step-by-step content
