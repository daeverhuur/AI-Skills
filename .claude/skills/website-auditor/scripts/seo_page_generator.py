#!/usr/bin/env python3
"""SEO Page Registry Manager - Create, read, update SEO page entries in JSON format."""

import json
import sys
import os
from datetime import datetime, timezone


SCHEMA_VERSION = "1.0"


def create_registry(domain: str, language: str = "en") -> dict:
    """Create a new empty SEO page registry."""
    return {
        "$schema": "seo-pages-schema",
        "version": SCHEMA_VERSION,
        "lastUpdated": datetime.now(timezone.utc).isoformat(),
        "pages": [],
        "siteConfig": {
            "domain": domain,
            "defaultLanguage": language,
            "sitemapPath": "/sitemap.xml",
            "robotsTxtPath": "/robots.txt",
        },
    }


def create_page_entry(
    page_id: str,
    title: str,
    slug: str,
    page_type: str = "blog",
    primary_keyword: str = "",
    secondary_keywords: list = None,
    longtail_keywords: list = None,
    meta_title: str = "",
    meta_description: str = "",
    h1: str = "",
    sections: list = None,
    schema_type: str = "Article",
    content_type: str = "informational",
    priority: str = "medium",
    links_to: list = None,
    linked_from: list = None,
    hub: str = None,
) -> dict:
    """Create a single SEO page entry."""
    if secondary_keywords is None:
        secondary_keywords = []
    if longtail_keywords is None:
        longtail_keywords = []
    if sections is None:
        sections = []
    if links_to is None:
        links_to = []
    if linked_from is None:
        linked_from = []

    word_count = sum(s.get("wordCountTarget", 300) for s in sections) if sections else 1000

    return {
        "id": page_id,
        "title": title,
        "slug": slug,
        "type": page_type,
        "status": "draft",
        "priority": priority,
        "targetKeywords": {
            "primary": primary_keyword,
            "secondary": secondary_keywords,
            "longtail": longtail_keywords,
        },
        "meta": {
            "title": meta_title or title[:60],
            "description": meta_description[:160] if meta_description else "",
            "canonical": slug,
            "robots": "index,follow",
            "ogTitle": meta_title or title[:60],
            "ogDescription": meta_description[:160] if meta_description else "",
            "ogImage": "",
        },
        "content": {
            "h1": h1 or title,
            "sections": sections,
            "estimatedWordCount": word_count,
            "contentType": content_type,
        },
        "schema": {"type": schema_type, "data": {}},
        "interlinking": {
            "linksTo": links_to,
            "linkedFrom": linked_from,
            "hub": hub,
        },
        "audit": {
            "lastAuditDate": None,
            "score": None,
            "issues": [],
        },
        "analytics": {
            "monthlySearchVolume": 0,
            "currentRanking": None,
            "estimatedTraffic": 0,
        },
    }


def add_page(registry_path: str, page: dict) -> dict:
    """Add a page to an existing registry file."""
    with open(registry_path, "r", encoding="utf-8") as f:
        registry = json.load(f)

    # Check for duplicate IDs
    existing_ids = {p["id"] for p in registry["pages"]}
    if page["id"] in existing_ids:
        print(f"Error: Page ID '{page['id']}' already exists.", file=sys.stderr)
        sys.exit(1)

    registry["pages"].append(page)
    registry["lastUpdated"] = datetime.now(timezone.utc).isoformat()

    with open(registry_path, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)

    return registry


def update_audit(registry_path: str, page_id: str, score: int, issues: list) -> dict:
    """Update audit results for a page."""
    with open(registry_path, "r", encoding="utf-8") as f:
        registry = json.load(f)

    for page in registry["pages"]:
        if page["id"] == page_id:
            page["audit"] = {
                "lastAuditDate": datetime.now(timezone.utc).isoformat(),
                "score": score,
                "issues": issues,
            }
            break
    else:
        print(f"Error: Page ID '{page_id}' not found.", file=sys.stderr)
        sys.exit(1)

    registry["lastUpdated"] = datetime.now(timezone.utc).isoformat()

    with open(registry_path, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)

    return registry


def list_pages(registry_path: str) -> None:
    """List all pages in the registry with status and scores."""
    with open(registry_path, "r", encoding="utf-8") as f:
        registry = json.load(f)

    if not registry["pages"]:
        print("No pages in registry.")
        return

    print(f"{'ID':<30} {'Type':<12} {'Status':<12} {'Score':<8} {'Priority':<10}")
    print("-" * 72)
    for page in registry["pages"]:
        score = page.get("audit", {}).get("score", "-")
        score_str = str(score) if score is not None else "-"
        print(
            f"{page['id']:<30} {page['type']:<12} {page['status']:<12} "
            f"{score_str:<8} {page['priority']:<10}"
        )


def generate_sitemap_data(registry_path: str) -> list:
    """Extract published page URLs for sitemap generation."""
    with open(registry_path, "r", encoding="utf-8") as f:
        registry = json.load(f)

    domain = registry["siteConfig"]["domain"].rstrip("/")
    urls = []
    for page in registry["pages"]:
        if page["status"] == "published":
            urls.append({
                "loc": f"{domain}{page['slug']}",
                "lastmod": registry["lastUpdated"][:10],
                "changefreq": "weekly" if page["type"] == "blog" else "monthly",
                "priority": {"high": "1.0", "medium": "0.7", "low": "0.4"}.get(
                    page["priority"], "0.5"
                ),
            })
    return urls


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  seo_page_generator.py init <registry_path> <domain>")
        print("  seo_page_generator.py list <registry_path>")
        print("  seo_page_generator.py sitemap <registry_path>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "init":
        if len(sys.argv) < 4:
            print("Usage: seo_page_generator.py init <registry_path> <domain>")
            sys.exit(1)
        path = sys.argv[2]
        domain = sys.argv[3]
        registry = create_registry(domain)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(registry, f, indent=2, ensure_ascii=False)
        print(f"Created registry at {path}")

    elif command == "list":
        if len(sys.argv) < 3:
            print("Usage: seo_page_generator.py list <registry_path>")
            sys.exit(1)
        list_pages(sys.argv[2])

    elif command == "sitemap":
        if len(sys.argv) < 3:
            print("Usage: seo_page_generator.py sitemap <registry_path>")
            sys.exit(1)
        urls = generate_sitemap_data(sys.argv[2])
        print(json.dumps(urls, indent=2))

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
