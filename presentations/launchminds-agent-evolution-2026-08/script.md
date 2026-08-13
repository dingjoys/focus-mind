# LaunchMinds: From Assistant to Autonomous

**A ~5-minute presentation for the Minds team and Minds community developers — what LaunchMinds has built on top of Minds, and where the partnership goes next.**

Companion file to [`launchminds-deck.pptx`](./launchminds-deck.pptx). Full narration is also embedded as speaker notes on each slide in the PPTX.

Deck title: **LaunchMinds: From Assistant to Autonomous**
Subtitle: *Built on Minds, from day one*

> **Note on terminology:** "Minds" is our underlying AI/LLM foundation model provider — it plays the same role for LaunchMinds that Claude or GPT-4 plays for other companies (see `launchminds-business-plan-2026-en.md`, §8.2: "LLM: Minds API"). It is a proper noun throughout this deck, not a generic term. **Harness** is a separate, complementary layer: our own proprietary context/memory system that sits on top of Minds. The deck deliberately keeps these two distinct: Harness = context layer, Minds = model layer.

---

## Slide 1 — From Assistant to Autonomous

**On slide:**
- AI-native, end-to-end brand marketing platform
- Powered by Minds, built with Harness
- A partnership story, not just a product demo

**Narration:**
> Good [morning/afternoon] — today I want to walk you through how LaunchMinds is evolving, from an assistant to something increasingly autonomous, and what that's been like to build on Minds. Our name isn't an accident: Launch, plus Minds. We picked it because Minds is the foundation everything we do stands on. What you'll see today is proof of what that foundation makes possible, and where we want to take it next, together.

---

## Slide 2 — The Problem

**On slide:**
- One tool for campaign design, another for deployment, a spreadsheet for the rest
- Campaign design, deployment, resource orchestration — all disconnected
- It doesn't scale, and it doesn't get smarter over time
- The fix isn't another point tool — it's a system that reasons across the whole lifecycle

**Narration:**
> Brand marketing today is stitched together by hand — one tool for campaign design, another for deployment, a spreadsheet for resource orchestration, and a person holding it all in their head. That doesn't scale, and it doesn't get smarter over time. We don't think the fix is another point tool. It's a system that reasons across the entire lifecycle — and that requires real intelligence at the core, not automation scripts with an AI label on them.

---

## Slide 3 — Positioning: Harness + Minds

**On slide:**
- LaunchMinds = Harness (context layer) + Minds (model layer)
- Harness: our proprietary enterprise context and memory
- Minds: the reasoning engine underneath
- Core line: *"LaunchMinds is an AI-native, end-to-end brand marketing platform that leverages Harness to build proprietary enterprise contexts, automating the entire lifecycle from campaign design and multi-platform deployment to resource orchestration."*
- Minds-driven, not just Minds-adjacent

**Narration:**
> [read core line]. Two things are doing the work here, and they're worth separating for this room. Harness is our layer — the proprietary context and memory that make a plan actually understand a specific brand, a specific market, a specific history of what's worked before. Minds is what Harness runs on — the model layer, the actual reasoning underneath every plan we generate. Harness without Minds is just a database. Minds without Harness is generic. Together, that's what makes this Minds-driven, not just Minds-adjacent.

---

## Slide 4 — How Agents Evolve

**On slide:**
- Assisted completion → single-session execution → agent mode
- The same arc coding tools went through
- We're climbing this ladder, stage by stage, natively on Minds

**Narration:**
> If you've watched how coding assistants evolved, you've seen this arc: first, assisted completion — suggestions, not action. Then single-session execution — an agent that completes a full task in one sitting, with a human watching. Then true agent mode — long-running, autonomous, checking its own work. We're building LaunchMinds through that same three-stage arc, applied to brand marketing instead of code. And because we built it Minds-native from the start, each stage is a Minds workflow — not a script with a model bolted on.

---

## Slide 5 — Stage 1: Assisted Completion *(status: DONE)*

**On slide:**
- In coding: inline suggestions, not action — human reviews every one
- Minds-assisted campaign drafting: proposes structure, drafts copy
- Pulls in context Harness has already stored
- Human in the loop at every step

**Narration:**
> Stage one is done and live. This is assisted completion — Minds helping a human draft a campaign: proposing structure, pulling in context Harness has stored, drafting copy. The human stays in the loop at every step. It's the smallest, safest version of Minds-driven work, and it's already saving our team real hours today.

---

## Slide 6 — Stage 2: Single-Session Execution *(status: TODAY)*

**On slide:**
- In coding: full task, one sitting, human watching
- One session, one Mind: registration + planning + deployment, no handoffs
- Runs on our internal skill system — structured capabilities handed to Minds so it can act, not just suggest
- Live in production today

**Narration:**
> Stage two is what's running in production right now. One session, one Mind, handling registration, planning, and deployment end to end — no handoffs between tools. It runs through our internal skill system, which is essentially a set of structured capabilities we hand to Minds so it can act, not just suggest. This is the first stage where Minds does real work autonomously within a session, and it's in daily use today.

---

## Slide 7 — Stage 3: Agent Mode *(status: NEXT MILESTONE)*

**On slide:**
- In coding: long-running, autonomous, self-checking
- Per-project workspace: one Mind plans, one executes, one analyzes, one adjusts
- Not roles loosely called "Minds" — literal Minds models, coordinating in a loop
- Where we push toward real multi-agent coordination on your platform

**Narration:**
> Stage three is our next milestone, and it's the part I think matters most for this room. We're building a per-project workspace where multiple Minds instances run side by side — one planning, one executing, one analyzing results, one adjusting the plan based on what it sees — coordinating with each other in a continuous loop. These aren't roles we're loosely calling "Minds." They're literal Minds models, each doing a distinct job, talking to each other. This is the clearest place you'll see what your platform makes possible when we push it toward real multi-agent coordination.

> Confirmed: multi-agent (multi-Minds) collaboration of this kind is a feasible pattern on Minds today, so this claim stands as stated.

---

## Slide 8 — One Open Thread: Sapien

**On slide:**
- Early conversations, not finalized
- Potential collaboration on the "analyze" step of the Stage 3 loop
- Evaluating whether their approach complements what Minds already gives us
- Full transparency: exploration, not a commitment

**Narration:**
> One open thread, for full transparency: we're in early conversations with Sapien about the analyze step in that stage-three loop — whether their approach complements what Minds already gives us. To be clear, this is exploration, not a commitment. We want to be upfront about what's decided and what's still being evaluated, because that honesty is part of how we want to build this relationship with you.

---

## Slide 9 — Built on Minds, With Minds' Community

**On slide:**
- Stage 1 & 2: shipped, in daily use
- Stage 3: next milestone, in motion
- Not an integration bolted on after the fact — built on Minds from day one
- "What gets built on top of a platform is the best answer a platform can have."

**Narration:**
> So: two stages shipped and running, one stage actively in motion, built on Minds from day one — not as an integration bolted on after the fact, but as the foundation. We're showing you this because we think it's a good answer to the question every platform has to answer eventually: what gets built on top of us? We'd like to keep building that answer together — with your platform, and with your community. Thanks for the time.

---

*Estimated run time: ~5 minutes at a natural speaking pace (~150 wpm). Revised 2026-08-13 to foreground Minds as the underlying model platform (analogous to Claude/GPT for other companies) and reframe the talk for an audience of Minds and Minds-community developers, per user direction. Title kept as "From Assistant to Autonomous" per user preference. Grounded in [`launchminds-business-plan-2026-en.md`](../../launchminds-business-plan-2026-en.md) (§8.2 confirms Minds as the primary LLM) and the team's actual build progress (Stages 1–2 shipped, Stage 3 in progress).*
