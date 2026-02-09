---
name: product-management-auditor
description: "Audit websites for product management improvements across retention, conversion, engagement, activation, and growth. Use when the user asks to audit a website, analyze a product's UX for conversion optimization, identify retention issues, evaluate onboarding flows, assess pricing pages, review funnel performance, or get product improvement recommendations. Triggers on: website audit, product audit, conversion audit, retention analysis, growth analysis, UX review, funnel analysis, onboarding review, pricing review, engagement analysis, bounce rate, churn analysis, feature adoption, user journey review."
---

# Product Management Auditor

Audit websites and digital products to identify improvement areas across retention, conversion, engagement, activation, and growth using established product management frameworks.

## Audit Workflow

1. Ask user for the website URL (or use the one provided)
2. Navigate to the website using browser automation tools
3. Perform the audit using the structured framework below
4. Generate a prioritized report with findings and recommendations
5. Use RICE scoring to rank recommendations by impact

## Audit Framework

Perform each audit category sequentially. For each, take screenshots, inspect page elements, and evaluate against the criteria.

### 1. First Impressions & Value Proposition (Bounce Rate Impact)

Navigate to the homepage. Evaluate:

- **Value proposition clarity**: Can a visitor understand what the product does within 5 seconds?
- **Headline effectiveness**: Is it specific, benefit-driven, and jargon-free?
- **CTA visibility**: Is the primary call-to-action above the fold and clearly visible?
- **Visual hierarchy**: Does the page guide the eye to the most important elements first?
- **Trust signals**: Are there logos, testimonials, security badges, or social proof visible?
- **Page load perception**: Does the page feel fast and responsive?

Score: 1-5 for each criterion.

### 2. Conversion Funnel Analysis

Navigate through the primary conversion path (sign-up, purchase, or lead capture). Evaluate:

- **Number of steps**: Count clicks/pages from landing to conversion
- **Form friction**: Number of fields, required vs optional, inline validation
- **Progress indicators**: Does the user know where they are in the process?
- **Exit points**: Are there distracting links or navigation that lead away from conversion?
- **Error handling**: Submit incomplete forms to check for helpful error messages
- **Social login / SSO**: Are low-friction sign-up options available?
- **Mobile responsiveness**: Test the funnel on mobile viewport

Metric targets:
- Form fields: Fewer is better. Each additional field reduces conversion ~7%
- Steps to conversion: 3 or fewer is ideal
- CTR on primary CTA: Benchmark against industry (2-5% typical)

### 3. Onboarding & Activation

If a free trial or demo is available, evaluate the onboarding flow:

- **Time to value (TTV)**: How quickly can a new user experience the core benefit?
- **Empty states**: Are blank screens helpful (guided) or confusing (empty)?
- **Progressive disclosure**: Is complexity introduced gradually?
- **Checklist / progress**: Is there an onboarding checklist or progress tracker?
- **Tooltips and guidance**: Are interactive guides or tooltips present?
- **Aha moment path**: Is the user guided toward the product's core value quickly?

### 4. Retention & Engagement Signals

Evaluate features that drive return visits:

- **Email capture**: Are there newsletter signups, content upgrades, or lead magnets?
- **Notification systems**: Push notifications, email digests, or in-app notifications
- **Content freshness**: Is content regularly updated (blog dates, news, changelog)?
- **Community features**: Forums, comments, user-generated content
- **Personalization**: Does the experience adapt to the user?
- **Habit loops**: Are there triggers that bring users back (daily summaries, streaks, updates)?
- **Feature depth**: Are there features that increase engagement over time?

### 5. Pricing & Monetization

Navigate to the pricing page. Evaluate:

- **Tier clarity**: Can users quickly understand what each tier offers?
- **Value anchoring**: Is the recommended plan visually highlighted?
- **Free tier / trial**: Is there a risk-free way to start?
- **Feature comparison**: Is there a clear comparison table?
- **Price-to-value alignment**: Does each tier justify its price jump?
- **Annual vs monthly**: Are annual discounts prominent?
- **Objection handling**: Are FAQs, guarantees, or cancellation policies visible?

Reference: See [references/pricing-frameworks.md](references/pricing-frameworks.md) for tier analysis methodology.

### 6. User Experience & Navigation

Evaluate the overall UX:

- **Navigation clarity**: Can users find key pages within 2 clicks?
- **Search functionality**: Is there a search bar? Does it return relevant results?
- **Mobile experience**: Test responsive breakpoints
- **Accessibility**: Check contrast ratios, alt text, keyboard navigation
- **Loading states**: Are there skeleton screens or spinners during load?
- **Error pages**: Check 404 page for helpfulness
- **Breadcrumbs / orientation**: Does the user always know where they are?

### 7. Trust & Social Proof

Evaluate elements that build credibility:

- **Testimonials**: Real names, photos, company names, specific results
- **Case studies**: Detailed success stories with metrics
- **Logos**: Client or partner logos prominently displayed
- **Reviews / ratings**: Third-party review integration
- **Security**: SSL, privacy policy, data handling transparency
- **Team / about page**: Does the company feel real and trustworthy?

### 8. Growth & Virality Mechanics

Evaluate built-in growth loops:

- **Referral program**: Is there a refer-a-friend mechanism?
- **Social sharing**: Can users share content or achievements?
- **Embeddable content**: Are there widgets, badges, or embed codes?
- **SEO foundations**: Meta titles, descriptions, heading structure, URL structure
- **Content marketing**: Blog quality, frequency, and SEO optimization
- **Backlink potential**: Is there linkable content (tools, data, reports)?

## Scoring & Prioritization

### RICE Framework for Recommendations

Score each finding:

- **Reach**: How many users does this affect? (1-10 scale, 10 = all users)
- **Impact**: How much will this improve the target metric? (0.25 = minimal, 0.5 = low, 1 = medium, 2 = high, 3 = massive)
- **Confidence**: How certain are you? (100% = high, 80% = medium, 50% = low)
- **Effort**: Person-months to implement (lower = better)
- **RICE Score**: (Reach x Impact x Confidence) / Effort

### Priority Categories

- **P1 - Quick Wins**: High RICE score, low effort. Implement immediately.
- **P2 - Strategic**: High impact but higher effort. Plan for next sprint.
- **P3 - Nice-to-have**: Moderate impact. Backlog for future consideration.
- **P4 - Defer**: Low impact relative to effort. Icebox.

## Report Output Format

Generate the audit report as follows:

```
## Website Audit Report: [Site Name]
**Date**: [Date]
**URL**: [URL]
**Auditor**: Claude Product Management Auditor

### Executive Summary
[2-3 sentence overview of the most critical findings]

### Scores by Category
| Category | Score (1-5) | Priority Issues |
|----------|-------------|-----------------|
| Value Proposition | X/5 | ... |
| Conversion Funnel | X/5 | ... |
| Onboarding | X/5 | ... |
| Retention | X/5 | ... |
| Pricing | X/5 | ... |
| UX & Navigation | X/5 | ... |
| Trust & Social Proof | X/5 | ... |
| Growth Mechanics | X/5 | ... |
| **Overall** | **X/5** | |

### Top Recommendations (RICE-Ranked)
| # | Recommendation | Category | RICE Score | Priority |
|---|---------------|----------|------------|----------|
| 1 | ... | ... | ... | P1 |
| 2 | ... | ... | ... | P1 |
| ... | | | | |

### Detailed Findings
[Per-category breakdown with screenshots and specific observations]

### Metric Impact Estimates
| Recommendation | Target Metric | Estimated Impact |
|---------------|---------------|-----------------|
| ... | Conversion Rate | +X% |
| ... | Bounce Rate | -X% |
| ... | Retention | +X% |

### Next Steps
[Prioritized action items organized by effort level]
```

## Reference Files

- **Metrics reference**: See [references/metrics-reference.md](references/metrics-reference.md) for all metric definitions and formulas
- **Pricing frameworks**: See [references/pricing-frameworks.md](references/pricing-frameworks.md) for tier analysis
- **Prioritization guide**: See [references/prioritization-guide.md](references/prioritization-guide.md) for RICE, MoSCoW, and Kano frameworks
