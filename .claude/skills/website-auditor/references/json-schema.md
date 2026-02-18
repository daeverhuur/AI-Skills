# SEO Page Management JSON Schema

## Page Registry Schema

The page registry (`seo-pages.json`) tracks all SEO pages in the application.

```json
{
  "$schema": "seo-pages-schema",
  "version": "1.0",
  "lastUpdated": "ISO-8601 timestamp",
  "pages": [
    {
      "id": "unique-slug-id",
      "title": "Page Title - Primary Keyword",
      "slug": "/url-path/to-page",
      "type": "landing|blog|product|category|location|faq|comparison|glossary|hub",
      "status": "draft|published|needs-review|archived",
      "priority": "high|medium|low",
      "targetKeywords": {
        "primary": "main target keyword",
        "secondary": ["secondary keyword 1", "secondary keyword 2"],
        "longtail": ["long tail phrase 1", "long tail phrase 2"]
      },
      "meta": {
        "title": "SEO Title (50-60 chars)",
        "description": "Meta description (150-160 chars)",
        "canonical": "/canonical-url",
        "robots": "index,follow",
        "ogTitle": "Open Graph title",
        "ogDescription": "Open Graph description",
        "ogImage": "/path/to/image.jpg"
      },
      "content": {
        "h1": "Main Heading",
        "sections": [
          {
            "heading": "H2 Section Heading",
            "targetKeyword": "keyword this section targets",
            "contentBrief": "Brief description of section content",
            "wordCountTarget": 300
          }
        ],
        "estimatedWordCount": 1500,
        "contentType": "informational|transactional|navigational|commercial"
      },
      "schema": {
        "type": "Article|FAQPage|Product|LocalBusiness|HowTo|BreadcrumbList",
        "data": {}
      },
      "interlinking": {
        "linksTo": ["page-id-1", "page-id-2"],
        "linkedFrom": ["page-id-3"],
        "hub": "parent-hub-page-id"
      },
      "audit": {
        "lastAuditDate": "ISO-8601 timestamp",
        "score": 0-100,
        "issues": [
          {
            "severity": "critical|warning|info",
            "category": "on-page|technical|content|links",
            "message": "Description of the issue",
            "recommendation": "How to fix it"
          }
        ]
      },
      "analytics": {
        "monthlySearchVolume": 0,
        "currentRanking": null,
        "estimatedTraffic": 0
      }
    }
  ],
  "siteConfig": {
    "domain": "https://example.com",
    "defaultLanguage": "en",
    "sitemapPath": "/sitemap.xml",
    "robotsTxtPath": "/robots.txt"
  }
}
```

## Page Generation Request Schema

When suggesting new pages, output in this format:

```json
{
  "suggestions": [
    {
      "rationale": "Why this page should exist",
      "searchIntent": "informational|transactional|navigational|commercial",
      "estimatedVolume": "high|medium|low",
      "competitionLevel": "high|medium|low",
      "page": {
        "...": "Full page object from registry schema above"
      }
    }
  ]
}
```

## Audit Report Schema

When outputting audit results:

```json
{
  "auditReport": {
    "date": "ISO-8601 timestamp",
    "pageId": "slug-id or URL",
    "overallScore": 0-100,
    "categories": {
      "onPage": {
        "score": 0-100,
        "checks": [
          {
            "name": "Check name",
            "status": "pass|fail|warning",
            "current": "Current value",
            "recommended": "Recommended value",
            "impact": "high|medium|low"
          }
        ]
      },
      "technical": { "score": 0-100, "checks": [] },
      "content": { "score": 0-100, "checks": [] },
      "offPage": { "score": 0-100, "checks": [] },
      "aeo": { "score": 0-100, "checks": [] }
    },
    "topIssues": [],
    "recommendations": []
  }
}
```

## Usage Patterns

### Add a new page to registry
Read existing `seo-pages.json`, append new page object, write back.

### Audit a page
Read page source/content, run checks against audit criteria, output audit report JSON.

### Suggest new pages
Analyze existing pages, identify gaps, output suggestions JSON with full page objects ready to merge into registry.

### Generate sitemap data
Read registry, filter published pages, output sitemap-compatible data.
