# FocusMind — AI Life Assistant for ADHD: Business Plan

> **One-line Positioning**: FocusMind is an AI Agent life assistant designed specifically for people with ADHD. Through conversational strategy planning and real-time decision support powered by large language models, it helps users break through executive function barriers, improve daily productivity, and enhance quality of life.

---

## Table of Contents

1. [Problem & Opportunity](#1-problem--opportunity)
2. [Target Users](#2-target-users)
3. [Competitive Analysis](#3-competitive-analysis)
4. [Product Solution](#4-product-solution)
5. [Core Features](#5-core-features)
6. [Technical Architecture](#6-technical-architecture)
7. [Business Model](#7-business-model)
8. [Market Size & Growth](#8-market-size--growth)
9. [Go-to-Market Strategy](#9-go-to-market-strategy)
10. [Milestones & Roadmap](#10-milestones--roadmap)
11. [Team & Resource Requirements](#11-team--resource-requirements)
12. [Risks & Mitigation](#12-risks--mitigation)

---

## 1. Problem & Opportunity

### The Core Challenge of ADHD

Attention Deficit Hyperactivity Disorder (ADHD) affects approximately **5–7%** of the global population, with over **366 million** adults living with the condition. The fundamental challenge they face is not a lack of ability, but **executive dysfunction**:

- **Task initiation difficulty**: Knowing what to do but being unable to start
- **Priority dysregulation**: Everything feels equally urgent or equally unimportant
- **Decision paralysis**: The brain "freezes" when faced with options, consuming enormous time and emotional energy
- **Time blindness**: Severely over- or under-estimating how long tasks take
- **Emotional dysregulation**: Cycles of frustration and anxiety that further erode executive function
- **Fragile schedules**: Any interruption can cause the entire day's plan to collapse

### Why Existing Tools Fail

Current productivity tools (Notion, Todoist, Tiimo, etc.) are **designed for neurotypical users** who can already self-organize. They require users to have stable self-planning abilities — precisely the skill ADHD individuals lack most.

> "I know Notion is powerful, but I spent 3 hours building a template and never opened it again."  
> — Typical ADHD user feedback

---

## 2. Target Users

### Core User Personas

**Primary: Adults with ADHD (ages 18–45)**
- Diagnosed or self-identified ADHD
- Strong motivation to improve daily functioning
- High receptivity to AI tools
- Primarily urban users and overseas communities

**Secondary:**
- People with executive function challenges who are undiagnosed (chronic procrastinators, anxiety sufferers)
- Parents of children with ADHD (helping structure their child's schedule)
- High-pressure professionals who need external structure

### User Pain Point Priority Matrix

| Pain Point | Frequency | Emotional Intensity | Existing Solutions |
|------------|-----------|--------------------|--------------------|
| Don't know where to start today | Daily | Extremely high | Ineffective |
| Decision paralysis, need someone to decide | High | High | None |
| Can't recover after an interruption | High | High | None |
| Task too large to break down | Medium | Medium | Partial |
| Forgetting important items | High | High | Reminder apps |

---

## 3. Competitive Analysis

### Competitor Comparison

| Feature | Tiimo | TickTick | Notion | Goblin Tools | **FocusMind** |
|---------|-------|---------|--------|--------------|---------------|
| Designed for ADHD | ✅ | ❌ | ❌ | ✅ | ✅ |
| AI conversational planning | ❌ | Basic | Basic | ❌ | ✅✅ |
| Daily strategy generation | ❌ | ❌ | ❌ | ❌ | ✅ |
| LLM integration | ❌ | ❌ | ❌ | Partial | ✅✅ |
| Decision paralysis support | ❌ | ❌ | ❌ | ❌ | ✅ |
| Schedule visualization | ✅✅ | ✅ | ✅ | ❌ | ✅ |
| Task decomposition | ❌ | ❌ | ❌ | ✅ | ✅✅ |
| Emotion-aware adjustments | ❌ | ❌ | ❌ | ❌ | ✅ |
| Interruption recovery | ❌ | ❌ | ❌ | ❌ | ✅ |
| Monthly price (USD) | $4.99 | $3.99 | $8 | Free | $9.99 |

### Core Weaknesses of Competitors

**Tiimo**: Excellent visual design, but zero AI capability. Users must plan everything before inputting it — the hardest step for someone with ADHD.

**TickTick**: Feature-rich but built for general users. AI only assists with tag classification, with no understanding of ADHD executive dysfunction.

**Notion AI**: A general-purpose AI writing assistant that doesn't understand ADHD and cannot generate personalized daily execution strategies.

**Goblin Tools**: The Magic ToDo feature (task decomposition) is ADHD-friendly, but functionality is narrow — no continuous conversation or schedule integration.

### FocusMind's Core Differentiation

> **From "Tool" to "AI Co-Pilot"**  
> Competitors require users to think it through before inputting; FocusMind helps users think it through via conversation.

---

## 4. Product Solution

### Product Philosophy

FocusMind's core is not task management — it is **Decision Offloading**: externalizing the most cognitively expensive step ("figuring out what to do") to an AI Agent, freeing up mental bandwidth for actual execution.

### Three Core Experiences

#### Experience 1: Morning Strategy Session

FocusMind initiates a conversation when the user wakes up:

```
FocusMind: Good morning! How are you feeling today? (1–5)

User: 3/5, okay, a bit anxious

FocusMind: Got it. I see you have 6 things on your list today:
  · Submit project report (deadline: today 6PM)
  · Reply to Sarah's email
  · Schedule dentist appointment
  · Grocery run
  · Prepare Thursday team meeting slides
  · Tidy up your workspace

Based on your current state (3/5), here's today's strategy:

  🔴 Must complete: Project report (2-hr focus block + 1-hr buffer)
  🟡 Quick win: Reply to Sarah (10 minutes)
  🟢 Defer: The other 4 items — move to tomorrow

Does this work for you, or would you like to adjust anything?
```

#### Experience 2: Real-Time Decision Support

Users can turn to FocusMind at any moment:

```
User: I'm stuck — I don't know whether to keep writing the report or go eat lunch first

FocusMind: When did you last eat something?

User: 8am

FocusMind: It's 12:30pm — you've gone 4.5 hours without food. Low blood sugar with ADHD makes focus significantly harder.

Recommendation: Eat first (30 minutes), then come back to the report. You'll likely find it much easier to write.
Leave your phone in your bag during lunch so your brain can actually rest.

Want me to remind you to come back in 30 minutes?
```

#### Experience 3: Interruption Recovery

When the day's schedule is disrupted:

```
FocusMind: You've been away from the report task for 45 minutes.
It's 3:15PM. Your deadline is 6:00PM.

You have 2 hours and 45 minutes left — that's enough.

Last time, you were working on the conclusion of Chapter 3.
For the next 20 minutes, your only goal is to write the first sentence of that conclusion.

Ready to begin?
```

---

## 5. Core Features

### MVP Feature Set (Phase 1)

#### 5.1 AI Conversational Strategy Planning

- **Morning Check-in**: Emotional state assessment + daily task review
- **Intelligent priority sorting**: Auto-ranked by deadline, emotional state, and task complexity
- **Time block generation**: Assigns tasks to specific time slots with built-in buffers and breaks
- **Strategy explanations**: Every recommendation includes a brief "why," helping users accept and act on it

#### 5.2 Large Language Model Conversational Capabilities

- **Multi-model support**: Claude, GPT-4, Gemini — user-configurable
- **ADHD-optimized prompting**: System prompts tailored to ADHD characteristics; model acts as an "executive co-pilot"
- **Decision paralysis resolver**: Helps users choose between options by giving a concrete recommendation, not a list of pros and cons
- **Task decomposition**: Breaks vague big tasks into immediately actionable micro-steps (Minimum Viable Actions)
- **Emotional support**: Recognizes frustration, provides appropriate validation and reframing

#### 5.3 Schedule & Task Management

- **Frictionless input**: Supports voice and natural language ("meeting tomorrow at 3pm")
- **Calendar view**: Time-block visualization with color-coded task types and priorities
- **Reminder system**: Progressive alerts (15 min, 5 min, and at task start)
- **Completion check-ins**: Simple logging with positive reinforcement on every completion

#### 5.4 Focus Mode

- **Pomodoro timer**: Configurable focus/break intervals
- **Distraction-blocking prompts**: Suggestions to mute notifications during focus sessions
- **Progress visualization**: Real-time display of time remaining and completion percentage

### Advanced Feature Set (Phase 2)

- **Pattern recognition**: Analyzes user data to identify peak performance windows and common blockers
- **Proactive Agent**: Initiates conversations at appropriate moments (e.g., user idle for 15+ minutes)
- **Calendar sync**: Two-way sync with Google Calendar and Apple Calendar
- **External tool integration**: Pulls tasks from Notion/Todoist for unified planning in FocusMind
- **Support network mode**: Allows trusted individuals (partner, therapist) to view daily reports and co-create strategies

---

## 6. Technical Architecture

### System Overview

```
┌─────────────────────────────────────────────────────┐
│                 FocusMind Client                     │
│          iOS App / Android App / Web PWA             │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│                   API Gateway                        │
│                 (Node.js / Express)                  │
└────┬─────────────────┬──────────────────┬────────────┘
     │                 │                  │
┌────▼─────┐  ┌────────▼──────┐  ┌───────▼────────────┐
│ Strategy │  │  LLM Adapter  │  │   Task & Calendar  │
│  Engine  │  │  (Multi-model)│  │      Service       │
└────┬─────┘  └────────┬──────┘  └───────┬────────────┘
     │                 │                  │
     └─────────────────▼──────────────────┘
                       │
          ┌────────────▼────────────┐
          │      PostgreSQL +       │
          │      Redis (Cache)      │
          └─────────────────────────┘
```

### Technology Stack

| Layer | Choice | Rationale |
|-------|--------|-----------|
| Frontend | React Native (Expo) | Cross-platform, rapid iteration |
| Backend | Node.js + TypeScript | Team familiarity, mature ecosystem |
| AI Layer | Anthropic Claude API (primary) + OpenAI fallback | Claude excels at empathetic, nuanced conversation suited to a coaching role |
| Database | PostgreSQL + Redis | Task persistence + session caching |
| Real-time | WebSocket | Streaming AI responses with no perceptible latency |
| Push notifications | FCM + APNs | Cross-platform reminders |
| Auth | Clerk / Auth0 | Fast integration |

### AI Strategy Engine Design

```
User input (emotion score + task list + historical preferences)
         ↓
   [Context Builder]
   · Current time / time to deadlines
   · User's historical execution patterns
   · Daily emotional score
   · Task priority rules
         ↓
   [LLM Reasoning Layer] — Claude / GPT-4
   · System Prompt: ADHD Coach role definition
   · Few-shot examples: ADHD-friendly strategy patterns
   · Chain-of-Thought: Explicit reasoning process
         ↓
   [Structured Output Parser]
   · Strategy JSON → frontend rendering
   · Time blocks → calendar component
   · Priority labels → color coding
```

---

## 7. Business Model

### Pricing Strategy

| Plan | Price | Includes |
|------|-------|---------|
| **Free** | $0/month | 3 AI conversations/day, basic task management, Pomodoro timer |
| **Pro** | $9.99/month | Unlimited AI conversations, full strategy planning, multi-model choice, data analytics |
| **Pro + Family** | $14.99/month | All Pro features + 2 support accounts |
| **Annual discount** | –30% | 30% off annual plans (Pro: $83.9/year) |

### Revenue Streams

1. **Subscription revenue** (primary): Monthly/annual SaaS subscriptions
2. **AI usage overages**: Pay-per-use once free tier limits are exceeded
3. **Enterprise/institutional licensing** (mid-term): Mental health clinics, ADHD support organizations
4. **Anonymized data insights** (long-term, opt-in): Research partnerships using anonymized behavioral data (requires explicit user consent)

### Key Financial Projections (Conservative)

| Metric | Year 1 | Year 2 | Year 3 |
|--------|--------|--------|--------|
| Registered users | 10,000 | 50,000 | 200,000 |
| Paid conversion rate | 8% | 12% | 15% |
| Paying users | 800 | 6,000 | 30,000 |
| ARPU (annual) | $80 | $90 | $95 |
| ARR | $64K | $540K | $2.85M |
| Gross margin | 65% | 72% | 78% |

> **AI cost control**: Through context window optimization, caching strategies, and prompt compression, target per-user monthly AI cost of $0.80–$1.50.

---

## 8. Market Size & Growth

### TAM / SAM / SOM

```
TAM (Global ADHD-related App market)
  $5.2B (2025) → $12.8B (2030)
  CAGR: 19.7%
        ↓
SAM (English + Chinese markets, adult ADHD productivity tools)
  $800M
        ↓
SOM (3-year addressable market)
  $30M (based on 30,000 paying users × $95 ARPU)
```

### Growth Drivers

1. **Rising ADHD diagnosis rates**: Growing awareness of adult ADHD; global confirmed cases increasing 5–8% annually
2. **AI tool adoption**: Rapid consumer acceptance of AI assistants; ChatGPT has completed market education
3. **Mental health focus**: Post-pandemic explosion in the mental wellness app market
4. **Community-driven growth**: ADHD communities (Reddit r/ADHD, social platforms) have strong organic word-of-mouth dynamics

---

## 9. Go-to-Market Strategy

### Phase 1: Community Cold Start (Months 0–6)

**Goal**: 1,000 core users, NPS > 50

- **Community infiltration**: Authentic participation in ADHD communities (Reddit, Discord, forums) — share the product naturally, engage in discussions, gather feedback
- **ADHD creator partnerships**: Invite 10–20 ADHD content creators to beta test in exchange for authentic reviews
- **Free early access**: First 500 users receive lifetime free Pro — seed word-of-mouth
- **Content marketing**: Publish practical resources like "ADHD Productivity Guides" for SEO and community sharing

### Phase 2: Word-of-Mouth Expansion (Months 6–18)

**Goal**: 10,000 users, 3% → 8% paid conversion

- **Referral rewards**: Both referrer and referee get 1 month of free Pro when a referral converts to paid
- **App Store optimization**: Keyword optimization targeting top rankings for "ADHD" and related terms
- **Mental health professional partnerships**: Reduced pricing for clinicians who recommend FocusMind to patients
- **Press outreach**: Pitch to TechCrunch, Product Hunt, mental health publications

### Phase 3: Scale (Months 18–36)

**Goal**: 50,000 users, 10%+ paid conversion

- **Paid acquisition**: Leverage data from phases 1–2 for targeted social media ads (Meta, TikTok)
- **Enterprise partnerships**: ADHD clinics, school counseling centers, corporate EAP programs
- **International expansion**: English-speaking markets (US, UK, Australia) as primary targets

---

## 10. Milestones & Roadmap

### Phase 0: Validation (Months 1–2)

- [ ] User research: 20 in-depth interviews with ADHD adults
- [ ] Competitive teardown: Deep-dive experience with Tiimo, Goblin Tools, TickTick
- [ ] MVP prototype: Figma prototype for core conversation flows
- [ ] Early adopters: Recruit 50-person closed beta group

### Phase 1: MVP Launch (Months 3–5)

- [ ] Core AI conversation features (morning strategy + real-time support)
- [ ] Basic task management (CRUD + reminders)
- [ ] iOS TestFlight beta
- [ ] Payment integration (Stripe)
- [ ] Target: 100 paying users

### Phase 2: Refinement & Growth (Months 6–12)

- [ ] Interruption recovery feature
- [ ] Android app
- [ ] Multi-model support (Claude + GPT-4 + Gemini)
- [ ] Analytics dashboard
- [ ] App Store public launch
- [ ] Target: 1,000 paying users

### Phase 3: Scale (Months 13–24)

- [ ] Calendar integration (Google / Apple)
- [ ] External tool connectors (Notion / Todoist)
- [ ] Family & support network features
- [ ] Enterprise tier
- [ ] Target: 10,000 paying users

---

## 11. Team & Resource Requirements

### Minimum Viable Team (Bootstrap Stage)

| Role | Responsibilities | Headcount |
|------|-----------------|-----------|
| Product / Founder | Product strategy, user research, business development | 1 |
| Full-stack Engineer | Frontend (React Native) + Backend | 1–2 |
| AI Engineer | Prompt engineering, model tuning, strategy engine | 1 |
| Designer (part-time) | UI/UX, ADHD-friendly design | 0.5 |

### Funding Requirements

| Purpose | Amount (USD) | Notes |
|---------|-------------|-------|
| AI API costs (year 1) | $15,000 | Claude + GPT-4 API |
| Infrastructure (year 1) | $8,000 | Servers, database, push services |
| Design tools | $3,000 | Figma, test devices |
| Marketing (cold start) | $10,000 | Creator partnerships, content production |
| Legal / incorporation | $5,000 | Company registration, privacy policy |
| Contractor labor | $30,000 | Part-time engineers, designers |
| **Total** | **$71,000** | |

> If the founding team has in-house engineering capability, initial capital requirements can be reduced to **$20,000–$30,000**.

---

## 12. Risks & Mitigation

| Risk | Likelihood | Impact | Mitigation Strategy |
|------|-----------|--------|---------------------|
| AI API cost overruns | Medium | High | Fine-grained prompt compression, usage caps, local small-model fallback |
| Big Tech replication (Apple, Google) | Medium | High | Build community moat fast; deep vertical specialization that generalist AI cannot replicate |
| Unhealthy user dependency | Low | Medium | Build in "autonomy scaffolding" features that gradually reduce reliance on AI as habits form |
| Data privacy compliance | Medium | High | GDPR + CCPA compliance from day one; minimal data collection; local-first storage |
| Low retention | High | High | Deepen morning check-in habit loop; positive reinforcement mechanics on task completion |
| LLM output quality inconsistency | Medium | Medium | Output quality scoring, human feedback annotation, continuous prompt iteration |

---

## Appendix: Core Design Principles

1. **Minimum input, maximum value**: ADHD users struggle with lengthy forms — every input interface should complete in 1–3 steps
2. **Immediate positive feedback**: Instant visual/audio feedback on every action to activate dopamine circuits
3. **Non-judgmental tone**: Language is always warm and accepting — never pressuring or critical
4. **Visible progress**: All waiting states and progress must be visualized to reduce time-blindness anxiety
5. **Reversible actions**: Everything should be easily undoable and editable — reduce decision pressure
6. **Single focus**: The interface presents only the single most important thing at a time — prevent information overload

---

*Document Version: v1.0 | Date: 2026-06-26 | Author: FocusMind Founding Team*
