# Layout & Spacing Standards Reference

## Table of Contents
1. [Grid & Container Standards](#grid--container-standards)
2. [Spacing System](#spacing-system)
3. [Responsive Breakpoints](#responsive-breakpoints)
4. [Responsive Design Checklist](#responsive-design-checklist)
5. [Accessibility Standards](#accessibility-standards)
6. [Performance & Loading](#performance--loading)

---

## Grid & Container Standards

### Container Width

| Context | Max Width | Notes |
|---------|----------|-------|
| Full-width sections | 100% | Background images, hero sections |
| Content container | 1100-1300px | Most page content |
| Text-heavy content | 600-800px | Blog posts, articles, long-form text |
| Narrow focus content | 500-600px | Forms, login boxes, centered CTAs |

### Column Grids

| Grid | Common Use | Notes |
|------|-----------|-------|
| 1 column | Hero text, CTAs, testimonials | Full-width impact |
| 2 columns | Text + image, feature highlights | 50/50 or 60/40 splits |
| 3 columns | Feature cards, pricing tiers | Equal width columns |
| 4 columns | Icon grids, partner logos, stats | Works on desktop, stacks on mobile |
| Bento/masonry | Photo galleries, portfolio | Asymmetric grid for visual interest |

### Column Gap Standards

| Breakpoint | Typical Gap |
|-----------|-------------|
| Desktop | 30-60px |
| Tablet | 20-40px |
| Mobile | 15-25px |

---

## Spacing System

### Spacing Scale (8px Base)

Use multiples of 8px for a harmonious rhythm:

| Token | Value | Common Usage |
|-------|-------|-------------|
| xs | 8px | Inline spacing, icon-to-text gap |
| sm | 16px | Between related elements (label + input) |
| md | 24px | Between paragraphs, list items |
| lg | 32px | Between groups of elements |
| xl | 48px | Between content blocks within a section |
| 2xl | 64px | Between sections |
| 3xl | 80-120px | Major section dividers, hero padding |

### Section Spacing

| Element | Desktop | Tablet | Mobile |
|---------|---------|--------|--------|
| Section top/bottom padding | 80-120px | 60-80px | 40-60px |
| Between heading and content | 24-32px | 20-24px | 16-20px |
| Between content blocks | 48-64px | 32-48px | 24-32px |
| Card internal padding | 24-32px | 20-24px | 16-20px |
| Navigation height | 60-80px | 56-64px | 48-56px |

### Margin vs Padding

- **Padding**: Space inside an element (between border and content)
- **Margin**: Space outside an element (between this element and neighbors)
- **Consistency rule**: Similar elements should have identical spacing. Inconsistent spacing is one of the most common amateur design tells.

---

## Responsive Breakpoints

### Standard Breakpoints

| Breakpoint | Width | Target |
|-----------|-------|--------|
| Mobile portrait | 320-375px | Small phones |
| Mobile landscape | 376-480px | Phones rotated |
| Tablet portrait | 481-768px | Tablets, small laptops |
| Tablet landscape | 769-1024px | Tablets rotated, small screens |
| Desktop | 1025-1440px | Standard desktop |
| Large desktop | 1441px+ | Wide monitors |

### What Changes at Each Breakpoint

| Element | Desktop | Tablet | Mobile |
|---------|---------|--------|--------|
| Navigation | Horizontal links | Hamburger or condensed | Hamburger menu |
| Grid columns | 3-4 columns | 2 columns | 1 column |
| Hero layout | Side-by-side (text + image) | Stacked or adjusted | Fully stacked |
| Font sizes | Full scale | ~85% of desktop | ~75% of desktop |
| Section padding | Full spacing | ~75% of desktop | ~60% of desktop |
| Images | Full size | Scaled to fit | Full-width or hidden |
| Logo | Full logo + text | May reduce size | Smaller, may be icon only |

### Typography Scale Across Breakpoints

| Element | Desktop | Tablet | Mobile |
|---------|---------|--------|--------|
| H1 | 48-60px | 36-44px | 28-36px |
| H2 | 32-42px | 28-34px | 24-28px |
| H3 | 24-32px | 22-28px | 20-24px |
| Body | 16-18px | 16px | 16px (never go below) |
| Small | 14px | 14px | 14px |

---

## Responsive Design Checklist

### Must-Haves

- [ ] No horizontal scrolling on any breakpoint
- [ ] All text is readable without zooming on mobile (16px minimum body)
- [ ] Touch targets are at least 44x44px on mobile
- [ ] Images resize or hide appropriately on smaller screens
- [ ] Navigation collapses to a mobile-friendly pattern
- [ ] Forms are usable on mobile (fields stack, keyboard-friendly)
- [ ] Content order makes sense on mobile (important content first)

### Should-Haves

- [ ] Different image crops or sizes loaded per breakpoint (art direction)
- [ ] Spacing reduces proportionally on smaller screens
- [ ] Multi-column layouts stack gracefully
- [ ] Interactive elements have visible focus states for keyboard navigation
- [ ] Font sizes scale down but maintain readable hierarchy
- [ ] Cards and components maintain readable proportions

### Common Responsive Issues

- Content overflowing horizontally on mobile (missing `overflow-x: hidden` or too-wide elements)
- Fixed-width elements that don't adapt (images, iframes, tables)
- Text too large on mobile making single words per line
- Navigation that doesn't collapse or is inaccessible on mobile
- Buttons too small to tap comfortably
- Desktop-only hover interactions with no mobile alternative
- Hero images that lose their subject when cropped on mobile

---

## Accessibility Standards

### WCAG Key Requirements for Design

| Requirement | Standard | Check |
|-------------|----------|-------|
| Text contrast (normal) | 4.5:1 minimum | Test all text/background combos |
| Text contrast (large) | 3:1 minimum | 18px+ bold or 24px+ regular |
| Non-text contrast | 3:1 minimum | Buttons, form borders, icons |
| Focus indicators | Visible on all interactive elements | Tab through the page |
| Alt text | All meaningful images | Check img tags |
| Keyboard navigation | All interactive elements reachable | Tab through the page |
| Heading structure | Logical H1-H6 order | No skipping levels |
| Color not sole indicator | Don't rely only on color for meaning | Use icons, text, patterns too |

### Quick Accessibility Checks

1. **Zoom to 200%**: Is everything still usable?
2. **Tab through the page**: Can you reach and activate every interactive element?
3. **Remove images**: Does the page still make sense (alt text)?
4. **Grayscale test**: Can you still distinguish elements without color?
5. **Screen reader test**: Do headings and landmarks make structural sense?

---

## Performance & Loading

### Page Speed Impact on Design

| Load Time | Impact |
|-----------|--------|
| 0-2 seconds | Excellent user experience |
| 2-4 seconds | Acceptable, minor frustration |
| 4-7 seconds | High bounce risk, significant frustration |
| 7+ seconds | Most users abandon |

### Design Choices That Affect Performance

| Element | Lighter Alternative |
|---------|-------------------|
| Large hero images (5MB+) | Compress to <200KB, use WebP, lazy load |
| Multiple custom fonts | Limit to 2 fonts, subset unused characters |
| Heavy animations | Use CSS transforms over JavaScript, reduce complexity |
| Auto-playing video | Load on interaction, use poster image |
| Unoptimized icons | Use SVG sprites or icon fonts |
| Multiple large images | Lazy load below-the-fold images |

### Loading State Design

- **Skeleton screens**: Show content placeholders shaped like the final layout
- **Progressive loading**: Show text first, then images
- **Lazy loading**: Load below-fold images only when user scrolls near them
- **Transitions**: Use subtle fade-ins as content loads (avoid jarring pop-in)
