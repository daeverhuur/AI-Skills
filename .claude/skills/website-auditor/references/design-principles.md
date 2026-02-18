# Web Design Principles Reference

## Table of Contents
1. [Typography](#typography)
2. [Color Theory](#color-theory)
3. [Visual Hierarchy](#visual-hierarchy)
4. [Imagery & Photography](#imagery--photography)
5. [Brand Consistency](#brand-consistency)
6. [Mood & Emotional Design](#mood--emotional-design)

---

## Typography

### Font Selection Guidelines

- **Heading fonts** should be distinctive and convey brand personality. Avoid overused defaults (Arial, Times New Roman). Consider whether a serif, sans-serif, or display font matches the brand tone.
- **Body fonts** must prioritize readability. Sans-serif fonts (Inter, Noto Sans, system fonts) work well for body text. Avoid display or decorative fonts for body copy.
- **Font pairing**: Use at most 2-3 fonts. A common pattern is a distinctive heading font + a clean body font (e.g., a premium serif heading with a neutral sans-serif body).

### Typographic Scale

| Element | Typical Desktop Size | Weight | Purpose |
|---------|---------------------|--------|---------|
| H1 | 40-60px | Bold/Black | Page title, one per page |
| H2 | 30-42px | Bold/Medium | Section headings |
| H3 | 24-35px | Semi-bold | Sub-section headings |
| H4 | 18-24px | Semi-bold | Card titles, minor headings |
| Body | 16-18px | Regular (400) | Main paragraph text |
| Small | 14px | Regular | Captions, metadata |
| Nav links | 14-18px | Medium (500) | Navigation items |

### Line Height & Spacing

- **Body text line-height**: 1.4-1.6 (140-160% of font size)
- **Headings line-height**: 1.1-1.3 (tighter for large text)
- **Paragraph spacing**: 1em-1.5em between paragraphs
- **Letter spacing**: -0.02em to -0.01em for large headings (tighten); 0.02em-0.1em for uppercase small text (loosen)

### Line Length

- **Optimal**: 50-75 characters per line for body text
- **Maximum readable width**: ~700px for 16px body text
- **Container max-width** for text-heavy sections: 600-800px

### Common Typography Issues

- Generic system fonts with no personality
- Too many different fonts (visual noise)
- Heading sizes too similar (weak hierarchy)
- Body text too small (<16px) or too light (< 400 weight)
- Line-height too tight (cramped feel) or too loose (disconnected lines)
- Text on images without sufficient contrast (overlay needed)
- Inconsistent text styles across similar elements

---

## Color Theory

### Color Palette Structure

A professional web palette typically includes:

| Role | Count | Usage |
|------|-------|-------|
| **Primary** | 1 color | Brand identity, headers, key elements |
| **Secondary** | 1-2 colors | Supporting elements, section backgrounds |
| **Accent** | 1 color | CTAs, buttons, highlights, links |
| **Neutral** | 3-5 shades | Backgrounds (white/light gray), text (dark gray/black), borders |
| **Semantic** | 3-4 colors | Success (green), error (red), warning (yellow), info (blue) |

### Color Psychology in Web Design

| Color | Associations | Best for |
|-------|-------------|----------|
| Blue | Trust, stability, professionalism | Finance, healthcare, technology, corporate |
| Green | Growth, health, nature, calm | Wellness, environment, finance |
| Red/Orange | Energy, urgency, excitement | Food, entertainment, CTAs, sales |
| Purple | Premium, creativity, luxury | Beauty, luxury, creative industries |
| Black/Dark | Sophistication, power, elegance | Luxury, fashion, premium brands |
| White | Clean, minimal, modern | Technology, healthcare, minimalist brands |
| Warm tones | Inviting, friendly, energetic | Restaurants, retail, social platforms |
| Cool tones | Professional, calming, trustworthy | B2B, healthcare, finance |

### Contrast Requirements (WCAG)

| Level | Normal Text | Large Text (18px+ bold or 24px+) |
|-------|-------------|----------------------------------|
| AA (minimum) | 4.5:1 | 3:1 |
| AAA (enhanced) | 7:1 | 4.5:1 |

### Common Color Issues

- Too many colors creating visual chaos
- No clear accent color for CTAs (buttons blend in)
- Insufficient contrast on text (especially light gray on white)
- Colors that clash or feel unintentional
- No color consistency (same element in different colors)
- Color not adapted for different section backgrounds
- Gradient overuse or poorly executed gradients

---

## Visual Hierarchy

### The Visual Hierarchy Toolkit

Control where the eye goes using these tools (ordered by impact):

1. **Size**: Larger elements are seen first
2. **Color/Contrast**: High-contrast elements demand attention
3. **Position**: Top-left is seen first (in LTR layouts), center draws focus
4. **Whitespace**: Elements with more surrounding space feel more important
5. **Typography weight**: Bold text draws the eye before light text
6. **Imagery**: Photos and illustrations grab attention over text
7. **Motion**: Animation draws the eye (use sparingly)

### Hierarchy Patterns

- **Z-pattern**: For pages with minimal text. Eye moves: top-left > top-right > bottom-left > bottom-right
- **F-pattern**: For text-heavy pages. Eye scans horizontally at top, then vertically down the left side
- **Focal point**: Use one dominant visual element per section to anchor attention

### Common Hierarchy Issues

- Everything competing for attention (nothing stands out)
- CTA buttons not visually prominent enough
- Headings and body text too similar in size/weight
- Important content buried below the fold
- No clear reading order or flow through the page

---

## Imagery & Photography

### Image Quality Standards

- **Resolution**: Export at 2x for retina displays (a 600px-wide image needs a 1200px source)
- **File formats**: JPEG for photos, PNG for transparency, SVG for logos/icons, WebP for modern optimization
- **Compression**: Balance quality and file size. Target < 200KB for most images
- **Aspect ratios**: Keep consistent within a section (all cards same ratio, all hero images same ratio)

### Photography Style Guidelines

- **Color consistency**: All photos should share a similar color temperature (warm/cool) and tone
- **Custom vs stock**: Custom photography is always preferred. Stock photos should feel authentic, not staged
- **Editing consistency**: Apply the same color grading, brightness, and contrast adjustments across all photos
- **People in photos**: Show real team members or real customers when possible. Avoid generic stock people
- **Subject relevance**: Every image should directly support the content it accompanies

### Icon Guidelines

- Use a **single icon set** with consistent style (outline, filled, or duotone)
- Maintain consistent **weight/stroke width** across all icons
- Keep icons the **same size** when used in a row or grid
- Ensure icons have **clear meaning** and are recognizable

### Common Imagery Issues

- Low-resolution or blurry images
- Mixed photography styles (different color temperatures, lighting)
- Generic stock photography that feels inauthentic
- Icons from different sets with inconsistent styles
- Logo walls with inconsistently sized logos
- Images that are decorative but don't support the message
- Missing alt text for accessibility

---

## Brand Consistency

### Brand Consistency Checklist

- [ ] Same logo used everywhere (no variations in color/layout without reason)
- [ ] Color palette used consistently (same colors for same purposes)
- [ ] Typography consistent across all pages (same fonts, sizes, weights)
- [ ] Photography style consistent (same tone, editing, quality)
- [ ] Icon style consistent (same set, weight, size)
- [ ] Button styles consistent (same shape, color, size for same function)
- [ ] Spacing rhythm consistent (same gaps between similar elements)
- [ ] Tone of voice consistent in copy (formal/casual/playful matching design)

### Common Consistency Issues

- Different button styles on the same page
- Heading sizes changing without clear hierarchy reason
- Mixed icon sets or random decorative elements
- Photography that ranges from professional to amateur
- Spacing that varies randomly between similar sections

---

## Mood & Emotional Design

### Design Conveys a Message

Every design choice sends a signal. The key question is: what message does this choice convey?

| Element | Premium/Trust | Friendly/Approachable | Bold/Energetic |
|---------|--------------|----------------------|----------------|
| Colors | Muted, dark, monochrome | Bright, warm, pastel | Saturated, high-contrast |
| Typography | Serif or thin sans-serif | Rounded sans-serif | Heavy/black weight |
| Imagery | Clean, minimal, editorial | Candid, warm, real people | Dynamic, high-contrast |
| Spacing | Generous whitespace | Moderate, cozy | Tight, dense |
| Shapes | Sharp corners or subtle rounds | Rounded corners, circles | Angular, geometric |
| Animations | Subtle, elegant | Playful, bouncy | Fast, impactful |

### The Mood Board Method

Professional designers collect visual references before designing:

1. **Research**: Search for inspiration in the brand's industry and adjacent industries
2. **Collect**: Screenshot designs, colors, typography, layouts that feel right
3. **Curate**: Narrow down to a focused mood board (3-10 key references)
4. **Extract**: Pull color palettes, font choices, and layout patterns from references
5. **Differentiate**: Ensure the final direction stands apart from competitors

### Evaluating Mood Alignment

When auditing, ask:
- Does this design match what the business is trying to communicate?
- Would a visitor immediately understand the industry and tone?
- Does it feel intentional, or like random design choices?
- Is the mood consistent across all pages and sections?
