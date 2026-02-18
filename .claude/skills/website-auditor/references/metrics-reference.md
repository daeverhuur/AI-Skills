# Product Metrics Reference

## Table of Contents
1. [Retention & Churn Metrics](#retention--churn-metrics)
2. [Activation & Engagement Metrics](#activation--engagement-metrics)
3. [Customer Satisfaction Metrics](#customer-satisfaction-metrics)
4. [Acquisition Metrics](#acquisition-metrics)
5. [Traffic & Engagement Metrics](#traffic--engagement-metrics)
6. [Revenue Metrics](#revenue-metrics)
7. [Virality Metrics](#virality-metrics)

---

## Retention & Churn Metrics

### Churn Rate
- **Formula**: (Users at start - Users at end) / Users at start
- **Context**: Critical for SaaS. Measure daily/weekly/monthly depending on sales cycle.
- **Benchmark**: <5% monthly churn is healthy for SaaS; <2% is excellent.

### Retention Rate
- **Formula**: (Users at end of period - New users during period) / Users at start
- **Context**: Inverse of churn. Focus on cohort retention curves.

### Customer Lifetime Value (CLV/LTV)
- **Formula**: Average customer lifespan x Average revenue per customer
- **Context**: Increase through upselling, cross-selling, and reducing churn. CLV should be >3x CAC.

---

## Activation & Engagement Metrics

### Daily Active Users (DAU)
- **Definition**: Users performing meaningful actions in one day
- **Context**: Define "meaningful action" specific to the product (not just login)

### Monthly Active Users (MAU)
- **Definition**: Users performing meaningful actions within 30 days

### Stickiness (DAU/MAU Ratio)
- **Formula**: (DAU / MAU) x 100
- **Benchmark**: 20%+ is good; 50%+ is excellent (Facebook-level)

### Feature Adoption Rate
- **Formula**: (Users using feature / Product MAU) x 100
- **Context**: Identify underused features that may need better discovery

### Average Session Duration (Dwell Time)
- **Formula**: Total session duration / Number of sessions
- **Context**: Higher = more engagement (for content/apps). For tools, shorter may be better.

---

## Customer Satisfaction Metrics

### Net Promoter Score (NPS)
- **Scale**: 0-10 (Detractors: 0-6, Passives: 7-8, Promoters: 9-10)
- **Formula**: % Promoters - % Detractors
- **Benchmark**: >0 is okay; >30 is good; >70 is world-class

### Customer Satisfaction Score (CSAT)
- **Formula**: (Ratings 4-5 / Total responses) x 100
- **Context**: Best measured immediately after an interaction

### Customer Effort Score (CES)
- **Definition**: Measures ease of interaction
- **Context**: Lower effort = higher satisfaction and retention

---

## Acquisition Metrics

### Customer Acquisition Cost (CAC)
- **Formula**: Total sales & marketing spend / Number of customers acquired
- **Includes**: Advertising, overhead, sales staff, software costs
- **Context**: Must be lower than CLV (ideally CLV:CAC > 3:1)

### Lead Types
- **MQL (Marketing Qualified Lead)**: Shows interest via marketing (downloads, webinar signups)
- **SQL (Sales Qualified Lead)**: Ready to talk to sales
- **PQL (Product Qualified Lead)**: Qualified by in-product behavior during trial

### Time to Value (TTV)
- **Definition**: Time from first use until customer realizes core benefit
- **Context**: Shorter TTV = higher activation rates

---

## Traffic & Engagement Metrics

### Bounce Rate
- **Formula**: (Single-page visitors / Total visits) x 100
- **Causes**: Non-engaging landing page, message-value mismatch, poor UX, slow load time
- **Benchmark**: 26-40% excellent; 41-55% average; 56-70% needs improvement; >70% poor

### Click-Through Rate (CTR)
- **Formula**: (Clicks / Impressions or Emails delivered) x 100
- **Benchmark**: Email: 2-5%; Google Ads: 2-3%; Display: 0.5-1%

### Impressions
- **Definition**: Total times content displayed (engagement not required)

### Reach
- **Definition**: Number of unique people who saw content

### Organic vs Paid Traffic
- **Organic**: Unpaid traffic from search engine results (SEO-driven)
- **Paid**: Traffic from advertising (Google Ads, social media ads)

---

## Revenue Metrics

### Monthly Recurring Revenue (MRR)
- **Formula**: Monthly subscription price x Number of paying customers
- **Tracks**: Growth rate, expansion MRR, contraction MRR, churned MRR

### Average Revenue Per Account (ARPA)
- **Formula**: Total revenue / Total number of accounts

### Average Revenue Per User (ARPU)
- **Formula**: Total revenue / Total number of users

### Return on Investment (ROI)
- **Inputs**: Build time, resources needed, value definition, time to first sale

---

## Virality Metrics

### Virality Factor (K-factor)
- **Formula**: V = New users from existing users / Total users
- **Context**: V > 1 means exponential growth
- **Tactics**: Social sharing, referral programs, word-of-mouth

### App Installs
- **Context**: Track alongside uninstalls and active usage for true picture

### App Store Ratings
- **Context**: Both quantitative scores and qualitative reviews
