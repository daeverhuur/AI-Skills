# Prioritization Frameworks Guide

## Table of Contents
1. [RICE Framework](#rice-framework)
2. [MoSCoW Method](#moscow-method)
3. [Kano Model](#kano-model)
4. [Value vs Complexity Matrix](#value-vs-complexity-matrix)
5. [Priority Levels](#priority-levels)

---

## RICE Framework

The most data-driven approach. Score each recommendation:

### Variables

| Variable | Description | Scale |
|----------|------------|-------|
| **Reach** | Users affected in a given time period | 1-10 (10 = all users) |
| **Impact** | Effect on the target metric per user | 0.25 = minimal, 0.5 = low, 1 = medium, 2 = high, 3 = massive |
| **Confidence** | Certainty in reach and impact estimates | 100% = high, 80% = medium, 50% = low |
| **Effort** | Person-months to implement | Estimate in person-months (lower = better) |

### Formula

```
RICE Score = (Reach x Impact x Confidence) / Effort
```

### Example

| Finding | Reach | Impact | Confidence | Effort | RICE Score |
|---------|-------|--------|------------|--------|------------|
| Simplify signup form | 8 | 2 | 80% | 0.5 | 25.6 |
| Add social proof | 6 | 1 | 50% | 0.25 | 12.0 |
| Redesign pricing page | 4 | 3 | 80% | 2 | 4.8 |

Higher RICE score = higher priority.

---

## MoSCoW Method

Group findings into four buckets:

| Category | Description | Action |
|----------|------------|--------|
| **Must Have** | Product doesn't work properly without fixing this | Fix immediately |
| **Should Have** | Important improvement, significant user impact | Plan for next sprint |
| **Could Have** | Nice improvement, moderate impact | Add to backlog |
| **Won't Have** | Low impact relative to effort | Defer or discard |

Allocate resources: Must Haves first, then Should Haves until capacity is reached.

---

## Kano Model

Categorize findings by customer satisfaction impact:

| Category | Absent | Present | Strategy |
|----------|--------|---------|----------|
| **Basic** | Causes dissatisfaction | Expected (no delight) | Must fix. These are table-stakes. |
| **Performance** | Less satisfaction | More satisfaction (linear) | Invest proportionally. More effort = more satisfaction. |
| **Excitement** | No impact | Delights users | High-value, often low-effort surprises. |

### Application to Audit

- **Basic findings**: Broken links, missing SSL, slow load times, broken mobile layout
- **Performance findings**: Better search, clearer navigation, faster forms
- **Excitement findings**: Personalization, micro-animations, unexpected helpful features

---

## Value vs Complexity Matrix

Quick visual prioritization:

```
High Value |  Strategic   |  Quick Wins
           |  Projects    |  (DO FIRST)
           |              |
-----------+--------------+------------
           |              |
Low Value  |  Money Pits  |  Fill-ins
           |  (AVOID)     |  (if time)
           |              |
           Low Effort      High Effort
```

- **Quick Wins** (high value, low effort): Implement immediately
- **Strategic Projects** (high value, high effort): Plan carefully
- **Fill-ins** (low value, low effort): Do when spare capacity exists
- **Money Pits** (low value, high effort): Avoid

---

## Priority Levels

Map findings to actionable priority levels:

| Level | Label | Timeline | Criteria |
|-------|-------|----------|----------|
| P1 | Critical | Immediate | Broken functionality, security issues, major conversion blockers |
| P2 | High | 1-2 weeks | Significant UX issues, clear conversion improvements |
| P3 | Medium | 1-3 months | Nice-to-have improvements, moderate impact |
| P4 | Low | Backlog | Minor enhancements, future consideration |

### External Communication States

When reporting to stakeholders, translate priorities:

- **P1**: "In progress" or "Fix planned this sprint"
- **P2**: "Prioritized for upcoming release"
- **P3**: "On roadmap, timeline TBD"
- **P4**: "Noted for future consideration"
