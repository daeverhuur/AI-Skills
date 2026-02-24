---
name: sea-advertising
description: >
  SEA and digital advertising setup, management, and auditing. Covers Google Ads (search, display, shopping,
  Performance Max, YouTube), Facebook/Meta Ads (pixel, CAPI, campaigns, audiences, retargeting), social media
  marketing (Instagram, LinkedIn, TikTok, Pinterest), and digital marketing strategy (funnels, CRO, email,
  analytics). Use when the user asks to: (1) Set up or configure Google/Facebook ad campaigns, (2) Audit
  advertising account performance, (3) Plan paid advertising strategy, (4) Optimize ROAS, CPA, or conversions,
  (5) Set up conversion tracking (Google Tag, Pixel, CAPI), (6) Do keyword research or audience targeting,
  (7) Create ad copy, (8) Build social media strategy, (9) Plan marketing budgets, (10) Start or scale an
  agency (SMMA), (11) Anything related to PPC, paid search, paid social, SEM, SEA, remarketing, or
  digital advertising.
---

# SEA & Digital Advertising Toolkit

Setup, manage, optimize, and audit paid advertising campaigns across Google, Meta, and social platforms.

## Workflow

### 1. Assess Current State

Before making changes, audit what exists:

- Read [audit-checklists.md](references/audit-checklists.md) for platform-specific audit templates
- Check: Is conversion tracking set up? Are campaigns structured logically? Is budget allocated efficiently?
- Identify quick wins (missing extensions, broken tracking, wasted spend on irrelevant keywords)

### 2. Choose Platform & Load Reference

Based on the user's needs, load the relevant platform reference:

| Need | Reference File |
|------|---------------|
| Google Ads (Search, Display, Shopping, PMax, YouTube) | [google-ads.md](references/google-ads.md) |
| Facebook/Instagram Ads (Meta) | [facebook-ads.md](references/facebook-ads.md) |
| Social media marketing & advertising | [social-media-marketing.md](references/social-media-marketing.md) |
| Overall strategy, funnels, CRO, email, analytics | [digital-marketing-strategy.md](references/digital-marketing-strategy.md) |
| Audit checklists (any platform) | [audit-checklists.md](references/audit-checklists.md) |

Load only the reference file(s) relevant to the current task.

### 3. Set Up or Optimize

Follow the platform-specific setup or optimization workflow from the loaded reference. Key principles that apply across all platforms:

**Before launching any campaign:**
1. Conversion tracking must be verified and working
2. Website/landing pages must be optimized for conversions
3. Budget must be calculated from business metrics (AOV, target CPA, conversion rate)
4. Negative targeting must be prepared (negative keywords, audience exclusions)

**The Relevance Chain (universal):**
```
Targeting → Ad Creative → Landing Page → Offer
```
All four must be aligned. Misalignment at any point wastes budget.

**Budget Allocation Rule of Thumb:**
- Minimum viable spend per channel: ~$500/month (need enough data)
- Testing phase (month 1-2): Split evenly across 2-3 channels
- Optimization phase (month 2-4): Shift 60-70% to top performers
- Scale phase (month 4+): Double down on proven channels

### 4. Monitor & Optimize

**Weekly:** Review search terms / audience reports, add negatives, check budgets
**Monthly:** A/B test creative, review conversion data, adjust bids/budgets
**Quarterly:** Strategic review, channel reallocation, competitor analysis

### 5. Report & Iterate

Focus reporting on business metrics (revenue, CPA, ROAS, leads), not vanity metrics (impressions, clicks). Use UTM tracking for cross-channel attribution.

## Platform Quick-Reference

### Google Ads Core Concepts
- **Ad Rank** = Max CPC Bid x Quality Score (QS 7+ is the target)
- **Match Types**: Start with Phrase + Exact only. Never start with Broad.
- **Smart Bidding**: Need 30+ conversions/month before automated strategies work well
- **Extensions**: Always set up ALL relevant extensions (sitelinks, callouts, structured snippets, calls)
- **Negative Keywords**: Build list BEFORE launch, maintain weekly

### Meta Ads Core Concepts
- **Pixel + CAPI**: Both required for accurate tracking post-iOS 14
- **Funnel Structure**: TOF (cold) → MOF (engagers) → BOF (retargeting)
- **Creative is king**: Test 3-5 variations per ad set. Refresh every 2-4 weeks.
- **Audiences**: Start with lookalikes from purchasers/high-value customers
- **Learning Phase**: Need ~50 conversions per ad set per week. Don't make changes during learning.

### Social Media Core Concepts
- **Short-form video**: Highest reach format across all platforms (Reels, TikTok, Shorts)
- **Consistency > perfection**: Regular posting with good content beats occasional perfect posts
- **80/20 rule**: 80% value content, 20% promotional
- **Engagement**: Social is two-way. Respond to comments within 2 hours.

## Key Benchmarks

| Metric | Poor | Average | Good | Excellent |
|--------|------|---------|------|-----------|
| Google Ads CTR (Search) | <2% | 3-5% | 5-8% | >8% |
| Google Ads Quality Score | 1-4 | 5-6 | 7-8 | 9-10 |
| Google Ads Conv. Rate | <1% | 2-3% | 4-5% | >5% |
| Facebook CTR (Cold) | <0.5% | 0.8-1.2% | 1.5-2% | >2% |
| Facebook CPC | >$3 | $1-2 | $0.50-1 | <$0.50 |
| Facebook ROAS | <1x | 2-3x | 3-5x | >5x |
| Email Open Rate | <15% | 20-25% | 25-35% | >35% |
| Landing Page Conv. | <1% | 2-3% | 5-8% | >10% |
| Social Engagement Rate | <1% | 2-3% | 4-5% | >6% |
| LTV:CAC Ratio | <1:1 | 2:1 | 3:1 | >4:1 |

## Common Mistakes (Cross-Platform)

1. Launching ads without conversion tracking
2. No negative keyword/audience exclusion strategy
3. Sending traffic to homepage instead of dedicated landing pages
4. Setting and forgetting (no ongoing optimization)
5. Following platform rep recommendations blindly (they optimize for platform revenue, not yours)
6. Spreading budget too thin across too many channels
7. No retargeting strategy
8. Ignoring mobile experience
9. Vanity metrics focus instead of business metrics
10. No A/B testing culture
