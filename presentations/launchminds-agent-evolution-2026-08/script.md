# LaunchMinds: From Assistant to Autonomous

**A ~5-minute presentation for the Minds team and Minds community developers — what LaunchMinds has built on top of Minds, and where the partnership goes next.**

Companion file to [`launchminds-deck.pptx`](./launchminds-deck.pptx). Full narration is also embedded as speaker notes on each slide in the PPTX.

Deck title: **LaunchMinds: From Assistant to Autonomous**
Subtitle: *Built on Minds, from day one*

> **Note on terminology:** Minds is **not** a foundation model. It is the persistent agent platform LaunchMinds is built on, providing hosted agent execution, model access and routing, identity, long-term memory, Skills and Tools, collaboration, and wallet infrastructure. (Minds' own privacy policy states it doesn't operate its own LLM; Animoca Brands' Aug 6, 2026 update names Minds' current primary cognition model as MiniMax M3, running a "Mastermind Agent" architecture on top.) LaunchMinds adds a domain-specific **Campaign Operations Control Plane** — our proprietary layer for trusted project intelligence, campaign state, approval and budget policies, participation verification, incentive and settlement logic, and outcome learning. In this deck: **Minds = horizontal agent platform; LaunchMinds = vertical campaign operations system.** ("Harness" is retired as our external product-layer name — too technical, and it implied we were rebuilding general agent-harness capability Minds already provides.)

---

## Slide 1 — From Assistant to Autonomous

**On slide:**
- Agentic Campaign Operations System for project teams
- Built on Minds' persistent agent platform
- Plan → Approve → Execute → Verify → Settle → Learn

**Narration:**
> Good afternoon. LaunchMinds is the Agentic Campaign Operations System for project teams. Instead of helping with one isolated marketing task, it maintains project intelligence, carries campaign work across sessions, and moves from an objective to a verified outcome within explicit approval boundaries. We built it on Minds because campaign operations are long-running, stateful, multi-party, and increasingly transactional. Our name reflects that directly — Launch, plus Minds — because everything we're about to show you is built on your platform, not next to it. Today I want to show you how we're moving from assisted work to persistent, accountable campaign operations.

---

## Slide 2 — The Problem

**On slide:**
- One tool for campaign design, another for deployment, a spreadsheet for the rest
- Campaign design, deployment, resource orchestration — all disconnected
- Nothing persists between sessions, and nothing is accountable across the lifecycle
- The fix isn't another point tool — it's persistent, accountable campaign operations

**Narration:**
> Campaign operations today are stitched together by hand — one tool for campaign design, another for deployment, a spreadsheet for resource orchestration, and a person holding it all in their head. Nothing persists between sessions, and nothing is accountable across the full lifecycle, from objective to verified outcome. We don't think the fix is another point tool. It's a system that carries state, enforces approval, and stays accountable across the entire campaign lifecycle.

---

## Slide 3 — Minds + LaunchMinds: Platform and Vertical Control Plane

**On slide:**
- Minds: persistent agent platform — model routing, identity, memory, Skills, Tools, collaboration, wallet
- LaunchMinds: campaign operations control plane — project intelligence, state, approvals, verification, incentives, settlement, learning
- Minds provides general agency; LaunchMinds provides campaign accountability
- Objective → Approve → Execute → Verify → Settle → Learn

**Narration:**
> Minds is not simply the model underneath LaunchMinds. It is the horizontal agent platform that gives every Mind continuity, identity, memory, tools, collaboration, and the ability to keep working beyond a single chat. LaunchMinds is the vertical operating layer built on top. We maintain the trusted project intelligence, campaign state, approval rules, budget constraints, participant evidence, settlement logic, and outcome history. Minds provides the general ability to reason and act. LaunchMinds defines how that ability operates safely and measurably inside campaign operations. That is the division of labor: Minds makes agents persistent and capable; LaunchMinds makes campaign operations accountable.

---

## Slide 4 — How Agents Evolve

**On slide:**
- Assisted completion → single-session execution → persistent, bounded operation
- The same arc coding tools went through
- We're climbing this ladder, stage by stage, natively on Minds

**Narration:**
> If you've watched how coding assistants evolved, you've seen this arc: first, assisted completion — suggestions, not action. Then single-session execution — an agent that completes a full task in one sitting, with a human watching. Then persistent, bounded operation — long-running, accountable, checking its own work within explicit limits. We're building LaunchMinds through that same three-stage arc, applied to campaign operations instead of code. And because we built it Minds-native from the start, each stage is a Minds workflow — not a script with a model bolted on.

---

## Slide 5 — Stage 1: Assisted Completion *(status: DONE)*

**On slide:**
- In coding: inline suggestions, not action — human reviews every one
- Minds drafts campaign structures, task mechanics, and copy
- Grounded in trusted project intelligence maintained by LaunchMinds
- Human approves every output

**Narration:**
> Stage one is assisted completion. A Mind drafts campaign structures, task mechanics, and copy grounded in the trusted project intelligence maintained by LaunchMinds. The operator reviews and approves every output. The value at this stage is speed and consistency, but the human still owns every step of the workflow.

---

## Slide 6 — Stage 2: Single-Session Execution *(status: TODAY)*

**On slide:**
- In coding: full task, one sitting, human watching
- One session, one Mind: registration + planning + deployment, no handoffs
- Runs through campaign-specific Skills, Tools, state, and approval gates on Minds
- Minds supplies the persistent runtime and execution; LaunchMinds supplies the campaign intelligence and permissions

**Narration:**
> Stage two is single-session execution. One persistent Mind can take a project from registration and briefing through campaign planning and deployment preparation without handoffs between different tools. LaunchMinds supplies the campaign-specific intelligence, Skills, state, and permissions. Minds supplies the persistent agent runtime and tool execution. This is where the Mind stops only suggesting and starts completing real operational work — while a human still supervises the session and approves high-impact actions.

---

## Slide 7 — Stage 3: Persistent, Bounded Campaign Operations *(status: NEXT MILESTONE)*

**On slide:**
- Long-running project workspace with shared campaign state and evidence
- A dynamic team of Minds assembled around each objective
- Approval gates for launch, budget changes, and settlement
- Verify before reward; recover from failure; log every action
- Every outcome improves the next campaign

**Narration:**
> Stage three is not simply about adding more agents. It is the shift from single-session execution to persistent, bounded campaign operations. Each project gets a continuously maintained operating state: its objectives, constraints, budgets, active campaigns, participant evidence, pending approvals, unresolved work, and results. Minds provides the persistent agents, memory, tools, and coordination. LaunchMinds provides the campaign control plane: the trusted project intelligence, action permissions, approval gates, verification rules, and settlement logic. A dynamic team of Minds can form around each campaign — researching, planning, executing, monitoring, verifying, and recovering — without being locked into a fixed pipeline or permanent set of roles. The shape of the team follows the work. Humans define the mandate and approve high-impact actions. Routine operations continue autonomously within those boundaries. Every action is logged, participation is verified before rewards are released, and real outcomes update the next plan. That closes the campaign operations loop: plan, approve, execute, verify, settle, and learn.

---

## Slide 8 — Built on Minds, With Minds' Community

**On slide:**
- Stage 1 & 2: built, live today
- Stage 3: next milestone, in motion
- Not an integration bolted on after the fact — built on Minds from day one
- "Minds makes agents persistent and capable. LaunchMinds makes campaign operations accountable."

**Narration:**
> So: two stages built and live today, one stage actively in motion, built on Minds from day one — not as an integration bolted on after the fact, but as the foundation. Minds makes agents persistent and capable. LaunchMinds makes campaign operations accountable. We're showing you this because we think it's a good answer to the question every platform has to answer eventually — what gets built on top of us? We'd like to keep building that answer together, with your platform and your community. Thanks for the time.

---

## Not carried into this deck (advisory only)

The dev team's note also included fundraising-narrative guidance beyond this 5-minute deck: a narrower top-level pitch ("The operating system for incentivized campaigns"), a longer 2–3 minute investor-review script, a metrics table mapping LaunchMinds activity to Minds-platform value (active Minds per project, cognition consumption per campaign, Skill/Tool calls, Bazaar reuse, etc.), and a requirement for three third-party-verifiable claims (with real numbers/demos/partner names) for a Minds Investment Programme application. None of that is reflected in the slides above — it needs real traction data we don't have yet, and the doc itself warns against fabricating numbers. Worth a separate one-pager once there's real data to put in it.

---

*Estimated run time: ~4.5–5 minutes at a natural speaking pace (~150 wpm) — 8 slides, 7 numbered content slides. Revised 2026-08-13 (round 3) after the dev team corrected a factual error: Minds is not a foundation model/LLM provider — it's a hosted persistent autonomous agent platform built on third-party LLMs (currently MiniMax M3 per Animoca Brands). Repositioned LaunchMinds as the vertical "Campaign Operations Control Plane" on top of Minds' horizontal agent platform; retired "Harness" as an external-facing term; retitled Stage 3 from "Agent Mode" to "Persistent, Bounded Campaign Operations" with explicit state/approval/verification/settlement/learning language. The original anchor positioning line ("AI-native, end-to-end brand marketing platform that leverages Harness...") is no longer used verbatim on slide 3, since it doesn't reflect the corrected architecture — flagging this explicitly since it was the founding brief for this deck. Title kept as "From Assistant to Autonomous" per user preference. Grounded in [`launchminds-business-plan-2026-en.md`](../../launchminds-business-plan-2026-en.md) and the team's actual build progress (Stages 1–2 built and live, Stage 3 in progress).*
