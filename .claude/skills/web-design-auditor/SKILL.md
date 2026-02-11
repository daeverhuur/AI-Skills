---
name: web-design-auditor
description: "Audit websites and landing pages for web design quality, visual effectiveness, and user experience. Use when the user asks to: (1) Audit or review a website's design, (2) Evaluate a landing page layout or visual quality, (3) Identify web design issues or improvements, (4) Review typography, color, imagery, or layout on a site, (5) Assess responsive design or mobile experience, (6) Evaluate hero sections, navigation, CTAs, or page structure, (7) Review visual hierarchy, whitespace, or consistency, (8) Get web design improvement recommendations. Triggers on: web design audit, design review, landing page review, visual audit, layout review, typography review, color audit, responsive design check, UI review, hero section review, CTA review, whitespace analysis, design consistency check, visual hierarchy review, page design feedback."
---

# Web Design & Landing Page Auditor

Audit websites and landing pages for design quality, visual effectiveness, layout, and user experience using professional web design principles. Provides actionable improvement recommendations prioritized by impact.

## Audit Workflow

1. Ask user for the website URL (or use the one provided)
2. Navigate to the website using browser automation tools
3. Take screenshots at desktop, tablet, and mobile breakpoints
4. Perform the audit using the structured framework below
5. Generate a prioritized report with findings and recommendations
6. Use impact/effort scoring to rank recommendations

## Audit Framework

Perform each audit category sequentially. For each, take screenshots, inspect page elements, and evaluate against the criteria.

### 1. First Impressions & Visual Impact (5-Second Test)

Navigate to the homepage or landing page. Evaluate within the first viewport:

- **Clarity**: Can a visitor understand what the site/business offers within 5 seconds?
- **Visual hierarchy**: Does the eye follow a clear path from most to least important?
- **Emotional tone**: Does the design convey the right feeling for the brand (trust, energy, calm, premium)?
- **Professionalism**: Does it look credible, modern, and intentionally designed (not templated)?
- **Differentiation**: Does it stand apart from competitors or feel generic?

Score: 1-5 for each criterion.

### 2. Hero Section Effectiveness

The hero section is the most important section on any page. Evaluate:

- **Headline impact**: Is it specific, benefit-driven, and immediately compelling?
- **Subheadline support**: Does it expand on the headline with additional context or value?
- **CTA clarity**: Is the primary call-to-action visible, clear, and action-oriented?
- **CTA contrast**: Does the button visually stand out from surrounding elements?
- **Imagery/media**: Does the hero image or video support the message and add value?
- **Layout composition**: Is there a clear relationship between text, image, and CTA?
- **Above-the-fold content**: Is the most important content visible without scrolling?

Reference: See [references/design-principles.md](references/design-principles.md) for hero section best practices.

### 3. Typography & Readability

Evaluate typographic choices and text presentation:

- **Font selection**: Are fonts appropriate for the brand? Are they distinctive or generic?
- **Font pairing**: If multiple fonts are used, do heading and body fonts complement each other?
- **Heading hierarchy**: Is there a clear H1 > H2 > H3 progression with distinct size/weight contrast?
- **Body text readability**: Is body text 16px+ with adequate line-height (1.4-1.6)?
- **Line length**: Are text lines between 50-75 characters for comfortable reading?
- **Text contrast**: Does text have sufficient contrast against its background (WCAG AA: 4.5:1)?
- **Text styling consistency**: Are text styles used consistently across similar elements?
- **Capitalization and spacing**: Are uppercase, letter-spacing, and text transforms used intentionally?

### 4. Color & Visual Identity

Evaluate the color palette and its application:

- **Color palette cohesion**: Do colors work together harmoniously? Is there a clear primary, secondary, and accent color?
- **Brand alignment**: Do colors convey the right message for the brand and industry?
- **Accent color usage**: Is a distinct accent color used for CTAs and interactive elements?
- **Contrast and accessibility**: Do all text/background combinations meet WCAG AA contrast ratios?
- **Color consistency**: Are the same colors used consistently for the same purposes across the site?
- **Background variation**: Are backgrounds varied enough to create visual interest between sections?
- **Gradient and effect usage**: If gradients or overlays are used, are they tasteful and purposeful?

### 5. Layout, Spacing & Visual Rhythm

Evaluate page structure, alignment, and use of space:

- **Grid consistency**: Are elements aligned to a consistent grid or column structure?
- **Section spacing**: Is there consistent, adequate spacing between sections (40-80px typical)?
- **Element spacing**: Is padding and margin consistent between similar elements?
- **Whitespace usage**: Is there enough breathing room, or does the design feel cluttered?
- **Content width**: Is body content constrained to a readable max-width (900-1200px typical)?
- **Visual balance**: Does the page feel balanced, not too heavy on one side?
- **Section variety**: Do sections alternate in layout (text-left/text-right, full-width/contained)?
- **Card and component consistency**: If cards or repeated components are used, are they uniform in style?

Reference: See [references/layout-checklist.md](references/layout-checklist.md) for spacing and layout standards.

### 6. Navigation & Page Structure

Evaluate how users orient and move through the site:

- **Navigation clarity**: Is the main navigation simple, clear, and limited to essential items (5-7 max)?
- **Logo placement**: Is the logo visible and does it link to the homepage?
- **Navigation style**: Does the nav feel consistent with the overall design?
- **Page structure logic**: Do sections flow in a logical narrative order?
- **Section identification**: Can users immediately understand what each section is about?
- **Footer completeness**: Does the footer include all essential links, contact info, and legal items?
- **Breadcrumbs/orientation**: On multi-page sites, does the user always know where they are?
- **Scroll depth**: Is the page length appropriate? Too long causes abandonment, too short lacks substance.

### 7. Imagery & Media

Evaluate the quality and usage of visual assets:

- **Image quality**: Are images high-resolution and crisp (2x for retina displays)?
- **Image relevance**: Do images support the content and message, not just decorate?
- **Image style consistency**: Do all images share a consistent style, color treatment, and tone?
- **Custom vs stock**: Are images custom or do they feel like generic stock photography?
- **Image composition**: Are images well-cropped and composed for the space they occupy?
- **Alt text**: Do images have descriptive alt text for accessibility?
- **Icon consistency**: If icons are used, are they from the same set with consistent style/weight?
- **Logo presentation**: If partner/client logos are shown, are they sized and aligned consistently?

### 8. Interactive Elements & Microinteractions

Evaluate buttons, forms, links, and interactive states:

- **Button design**: Are buttons visually distinct with clear affordance (they look clickable)?
- **Button hierarchy**: Is there a clear primary/secondary button distinction?
- **Hover states**: Do interactive elements have visible hover/focus states?
- **Form design**: Are form fields styled consistently with clear labels or placeholders?
- **Form validation**: Are errors shown inline with helpful messages?
- **Link styling**: Are links distinguishable from regular text?
- **Loading states**: Are there skeleton screens, spinners, or transitions during load?
- **Animations**: Are animations subtle, purposeful, and not distracting?

### 9. Responsive Design & Cross-Device Experience

Test at multiple breakpoints (desktop 1440px, tablet 768px, mobile 375px):

- **Breakpoint transitions**: Do layouts adapt gracefully at each breakpoint?
- **Mobile navigation**: Does the nav collapse to a usable hamburger/drawer menu?
- **Touch targets**: Are buttons and links at least 44x44px on mobile?
- **Typography scaling**: Do font sizes reduce proportionally on smaller screens?
- **Image handling**: Do images resize or recompose for smaller screens?
- **Horizontal scrolling**: Is there any unintended horizontal overflow on mobile?
- **Content priority**: Is the most important content prioritized in the mobile layout?
- **Spacing adjustment**: Is padding/margin reduced appropriately for smaller screens?

### 10. Trust, Social Proof & Credibility Signals

Evaluate elements that build visitor confidence:

- **Testimonials**: Are there real testimonials with names, photos, or company names?
- **Client/partner logos**: Are credibility logos prominently displayed?
- **Case studies**: Are there detailed success stories with specific results?
- **Social proof placement**: Is social proof placed near conversion points (CTAs, forms)?
- **Team/about visibility**: Does the site feel human and trustworthy?
- **Security indicators**: SSL, privacy policy, trust badges where appropriate?
- **Contact information**: Is it easy to find a way to contact the business?

## Scoring & Prioritization

### Scoring per Category

Rate each category 1-5:

| Score | Meaning |
|-------|---------|
| 5 | Excellent - Professional quality, no issues |
| 4 | Good - Minor improvements possible |
| 3 | Average - Several noticeable issues |
| 2 | Below average - Significant problems |
| 1 | Poor - Major redesign needed |

### Impact/Effort Framework for Recommendations

Score each finding:

- **Impact**: How much will this improve the user experience? (Low / Medium / High / Critical)
- **Effort**: How complex is the fix? (Quick fix / Moderate / Significant / Major redesign)
- **Priority**: Derived from impact vs effort

### Priority Categories

- **P1 - Quick Wins**: High impact, low effort. Implement immediately.
- **P2 - Strategic**: High impact, higher effort. Plan for next phase.
- **P3 - Polish**: Moderate impact. Address when time allows.
- **P4 - Backlog**: Low impact relative to effort. Consider for future.

## Report Output Format

Generate the audit report as follows:

```
## Web Design Audit Report: [Site Name]
**Date**: [Date]
**URL**: [URL]
**Auditor**: Claude Web Design Auditor

### Executive Summary
[2-3 sentence overview of the most critical design findings and overall impression]

### Overall Design Rating: X/5

### Scores by Category
| Category | Score (1-5) | Key Issues |
|----------|-------------|------------|
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
| **Overall** | **X/5** | |

### Top Recommendations (Priority-Ranked)
| # | Recommendation | Category | Impact | Effort | Priority |
|---|---------------|----------|--------|--------|----------|
| 1 | ... | ... | ... | ... | P1 |
| 2 | ... | ... | ... | ... | P1 |
| ... | | | | | |

### Detailed Findings
[Per-category breakdown with screenshots and specific observations]

### Design Strengths
[What the site does well - important to acknowledge]

### Before/After Concepts
[For top recommendations, describe what the improved version would look like]

### Next Steps
[Prioritized action items organized by effort level]
```

## Reference Files

- **Design principles**: See [references/design-principles.md](references/design-principles.md) for typography, color theory, imagery, and visual hierarchy guidelines
- **Layout checklist**: See [references/layout-checklist.md](references/layout-checklist.md) for spacing, grid, and responsive design standards
- **Section patterns**: See [references/section-patterns.md](references/section-patterns.md) for hero, CTA, testimonial, pricing, and other section best practices
