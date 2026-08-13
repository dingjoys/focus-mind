#!/usr/bin/env python3
"""Build the LaunchMinds 'From Assistant to Autonomous' presentation (PPTX)."""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ---- Brand palette (dark, indigo/mint accents) ----
BG_DARK = RGBColor(0x0B, 0x0F, 0x1A)
BG_PANEL = RGBColor(0x14, 0x1B, 0x2E)
BG_PANEL2 = RGBColor(0x18, 0x21, 0x38)
ACCENT = RGBColor(0x7C, 0x9C, 0xFF)      # indigo
ACCENT2 = RGBColor(0x5E, 0xE6, 0xC0)     # mint
WARN = RGBColor(0xFF, 0xB4, 0x6C)        # amber (for "next" status)
TEXT_MAIN = RGBColor(0xF2, 0xF4, 0xF8)
TEXT_DIM = RGBColor(0xA6, 0xAF, 0xC2)
TEXT_FAINT = RGBColor(0x6B, 0x74, 0x8C)

FONT = "Avenir Next"
SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

prs = Presentation()
prs.slide_width = SLIDE_W
prs.slide_height = SLIDE_H
BLANK = prs.slide_layouts[6]


def add_bg(slide, color=BG_DARK):
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = color


def add_rect(slide, x, y, w, h, color, line_color=None, radius=None):
    shape_type = MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE
    shp = slide.shapes.add_shape(shape_type, x, y, w, h)
    if radius:
        try:
            shp.adjustments[0] = radius
        except Exception:
            pass
    shp.fill.solid()
    shp.fill.fore_color.rgb = color
    if line_color is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line_color
        shp.line.width = Pt(1)
    shp.shadow.inherit = False
    return shp


def add_text(slide, x, y, w, h, text, size=18, color=TEXT_MAIN, bold=False,
             align=PP_ALIGN.LEFT, font=FONT, anchor=MSO_ANCHOR.TOP,
             line_spacing=1.15, italic=False):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    lines = text.split("\n")
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = line_spacing
        r = p.add_run()
        r.text = line
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.italic = italic
        r.font.color.rgb = color
        r.font.name = font
    return tb


def add_bullets(slide, x, y, w, h, items, size=15, color=TEXT_MAIN,
                 marker_color=None, font=FONT, space_after=10,
                 line_spacing=1.2, bold_first_words=None):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.line_spacing = line_spacing
        p.space_after = Pt(space_after)
        r = p.add_run()
        r.text = f"—  {item}"
        r.font.size = Pt(size)
        r.font.color.rgb = color
        r.font.name = font
    return tb


def add_kicker(slide, text, num_text=None):
    add_rect(slide, Inches(0.55), Inches(0.52), Inches(0.42), Inches(0.055), ACCENT2)
    add_text(slide, Inches(0.55), Inches(0.62), Inches(8), Inches(0.4),
             text.upper(), size=12.5, color=TEXT_DIM, bold=True)
    if num_text:
        add_text(slide, Inches(11.9), Inches(0.55), Inches(0.9), Inches(0.4),
                 num_text, size=12.5, color=TEXT_FAINT, align=PP_ALIGN.RIGHT)


def add_footer(slide, text="LaunchMinds  ·  From Assistant to Autonomous  ·  2026"):
    add_text(slide, Inches(0.55), Inches(7.1), Inches(9), Inches(0.3),
             text, size=9.5, color=TEXT_FAINT)


def add_badge(slide, x, y, text, color):
    w = Inches(0.16 * len(text) + 0.5)
    shp = add_rect(slide, x, y, w, Inches(0.32), BG_DARK, line_color=color, radius=0.5)
    tf = shp.text_frame
    tf.word_wrap = False
    tf.margin_left = Pt(2)
    tf.margin_right = Pt(2)
    tf.margin_top = Pt(0)
    tf.margin_bottom = Pt(0)
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = text
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = color
    r.font.name = FONT
    return shp


def new_slide(bg=BG_DARK):
    s = prs.slides.add_slide(BLANK)
    add_bg(s, bg)
    return s


def set_notes(slide, text):
    notes = slide.notes_slide
    notes.notes_text_frame.text = text


# ---------------------------------------------------------------------------
# Slide 1 — Title
# ---------------------------------------------------------------------------
s = new_slide()
add_rect(s, Inches(0), Inches(0), Inches(0.14), SLIDE_H, ACCENT2)
add_text(s, Inches(0.9), Inches(2.15), Inches(11), Inches(0.5),
         "LAUNCHMINDS", size=20, color=ACCENT2, bold=True)
add_text(s, Inches(0.85), Inches(2.6), Inches(11.5), Inches(1.6),
         "From Assistant\nto Autonomous", size=54, color=TEXT_MAIN, bold=True, line_spacing=1.05)
add_text(s, Inches(0.9), Inches(4.35), Inches(10.5), Inches(0.6),
         "How we're teaching AI to run the entire brand campaign lifecycle",
         size=19, color=TEXT_DIM, italic=True)
add_bullets(s, Inches(0.9), Inches(5.25), Inches(10.8), Inches(1.6), [
    "AI-native, end-to-end brand marketing platform",
    "Not a better tool — AI that figures out the strategy",
    "Today: where we are, and where we're going next",
], size=15, color=TEXT_DIM, space_after=8)
add_footer(s, "LaunchMinds · 2026")
set_notes(s, "Thanks everyone. Today I want to walk you through LaunchMinds — not just what it does, but how "
             "it's evolving, and where it's headed next. Our founding idea has always been simple: don't give "
             "brands a better tool to run campaigns — have AI figure out the campaign strategy for them. "
             "Everything we've built follows from that one line.")

# ---------------------------------------------------------------------------
# Slide 2 — The Problem
# ---------------------------------------------------------------------------
s = new_slide()
add_kicker(s, "The Problem", "01 / 08")
add_text(s, Inches(0.55), Inches(1.05), Inches(11.5), Inches(0.9),
         "Brand marketing today is fragmented", size=36, color=TEXT_MAIN, bold=True)
add_bullets(s, Inches(0.55), Inches(2.4), Inches(11.5), Inches(3.2), [
    "Campaign marketing is fragmented across tools",
    "Strategy is manual, slow, and inconsistent",
    "Execution and analysis live in separate silos",
    "No real feedback loop back into the next campaign",
], size=20, color=TEXT_MAIN, space_after=20)
add_footer(s)
set_notes(s, "Anyone who's run a brand campaign knows the pain. You're juggling five tools to plan it, another "
             "few to launch it across Twitter, Discord, Telegram, on-chain — and then performance data sits in "
             "a spreadsheet nobody revisits. There's no loop. Every campaign starts from scratch. That's the "
             "gap we built LaunchMinds to close.")

# ---------------------------------------------------------------------------
# Slide 3 — Our Positioning
# ---------------------------------------------------------------------------
s = new_slide()
add_kicker(s, "Positioning", "02 / 08")
add_text(s, Inches(0.55), Inches(1.05), Inches(11.5), Inches(0.7),
         "What LaunchMinds is, today", size=36, color=TEXT_MAIN, bold=True)
quote_box = add_rect(s, Inches(0.55), Inches(2.05), Inches(12.2), Inches(2.55), BG_PANEL, radius=0.06)
add_rect(s, Inches(0.55), Inches(2.05), Inches(0.09), Inches(2.55), ACCENT2)
add_text(s, Inches(1.0), Inches(2.3), Inches(11.3), Inches(2.1),
         "“LaunchMinds is an AI-native, end-to-end brand marketing platform that "
         "leverages Harness to build proprietary enterprise contexts, automating the "
         "entire lifecycle from campaign design and multi-platform deployment to "
         "resource orchestration.”",
         size=22, color=TEXT_MAIN, italic=True, line_spacing=1.3)
add_bullets(s, Inches(0.55), Inches(4.95), Inches(11.5), Inches(1.6), [
    "Transforms complex marketing needs into structured, actionable workflows",
    "Drives scalable user growth and brand impact",
    "Harness = the mechanism that builds a persistent, proprietary brand context",
], size=16.5, color=TEXT_DIM, space_after=10)
add_footer(s)
set_notes(s, "Here's how we describe ourselves today: LaunchMinds is an AI-native, end-to-end brand marketing "
             "platform that leverages Harness to build proprietary enterprise contexts — automating the entire "
             "lifecycle from campaign design and multi-platform deployment to resource orchestration. In plain "
             "terms: we turn a messy marketing problem into a structured, actionable workflow, and that workflow "
             "is what drives scalable growth. Harness is the core of that — it's how we build a persistent, "
             "proprietary understanding of a brand, and everything downstream runs on top of it.")

# ---------------------------------------------------------------------------
# Slide 4 — A Familiar Pattern (framework intro)
# ---------------------------------------------------------------------------
s = new_slide()
add_kicker(s, "The Framework", "03 / 08")
add_text(s, Inches(0.55), Inches(1.05), Inches(11.5), Inches(0.7),
         "A familiar pattern", size=36, color=TEXT_MAIN, bold=True)
add_text(s, Inches(0.55), Inches(1.85), Inches(11.8), Inches(0.9),
         "AI-assisted coding evolved through three recognizable stages.\nLaunchMinds is climbing the exact same ladder.",
         size=18, color=TEXT_DIM, line_spacing=1.3)

stage_labels = ["Assisted\nCompletion", "Single-Session\nExecution", "Agent\nMode"]
stage_x = [Inches(0.9), Inches(4.95), Inches(9.0)]
box_w = Inches(3.4)
box_y = Inches(3.1)
box_h = Inches(2.5)
colors = [TEXT_FAINT, ACCENT, ACCENT2]
for i, (label, x, c) in enumerate(zip(stage_labels, stage_x, colors)):
    add_rect(s, x, box_y, box_w, box_h, BG_PANEL, radius=0.08)
    add_text(s, x, box_y + Inches(0.3), box_w, Inches(0.4), f"STAGE {i+1}",
             size=13, color=c, bold=True, align=PP_ALIGN.CENTER)
    add_text(s, x, box_y + Inches(0.85), box_w, Inches(1.2), label,
             size=22, color=TEXT_MAIN, bold=True, align=PP_ALIGN.CENTER, line_spacing=1.15)
    if i < 2:
        arr = add_text(s, x + box_w + Inches(0.05), box_y + Inches(0.95), Inches(0.5), Inches(0.6),
                        "→", size=30, color=TEXT_DIM, align=PP_ALIGN.CENTER)
add_text(s, Inches(0.55), Inches(6.05), Inches(11.8), Inches(0.7),
         "We're not guessing at the roadmap — we're following a proven curve.",
         size=17, color=ACCENT2, italic=True)
add_footer(s)
set_notes(s, "To explain where LaunchMinds is headed, I want to borrow an analogy from something we all live in "
             "daily: how AI-assisted coding has evolved. It went through three distinct stages — and LaunchMinds "
             "is climbing that same ladder, one rung behind but on the same trajectory. Let's walk through it.")


# ---------------------------------------------------------------------------
# Helper for the three side-by-side "stage" slides
# ---------------------------------------------------------------------------
def stage_slide(kicker, num_text, stage_num, stage_name, status_text, status_color,
                 coding_title, coding_bullets, lm_title, lm_bullets, footer_line, notes):
    s = new_slide()
    add_kicker(s, kicker, num_text)
    add_text(s, Inches(0.55), Inches(1.0), Inches(8.5), Inches(0.7),
             f"Stage {stage_num}: {stage_name}", size=32, color=TEXT_MAIN, bold=True)
    add_badge(s, Inches(10.6), Inches(1.08), status_text, status_color)

    col_y = Inches(1.95)
    col_h = Inches(4.6)
    col_w = Inches(5.95)
    left_x = Inches(0.55)
    right_x = Inches(6.85)

    add_rect(s, left_x, col_y, col_w, col_h, BG_PANEL, radius=0.05)
    add_text(s, left_x + Inches(0.4), col_y + Inches(0.35), col_w - Inches(0.8), Inches(0.5),
             "IN CODING", size=14, color=TEXT_FAINT, bold=True)
    add_text(s, left_x + Inches(0.4), col_y + Inches(0.8), col_w - Inches(0.8), Inches(0.6),
             coding_title, size=19, color=TEXT_DIM, bold=True, line_spacing=1.2)
    add_bullets(s, left_x + Inches(0.4), col_y + Inches(1.55), col_w - Inches(0.8), Inches(2.8),
                coding_bullets, size=14.5, color=TEXT_DIM, space_after=12)

    add_rect(s, right_x, col_y, col_w, col_h, BG_PANEL2, radius=0.05)
    add_rect(s, right_x, col_y, Inches(0.08), col_h, status_color)
    add_text(s, right_x + Inches(0.4), col_y + Inches(0.35), col_w - Inches(0.8), Inches(0.5),
             "IN LAUNCHMINDS", size=14, color=status_color, bold=True)
    add_text(s, right_x + Inches(0.4), col_y + Inches(0.8), col_w - Inches(0.8), Inches(0.6),
             lm_title, size=19, color=TEXT_MAIN, bold=True, line_spacing=1.2)
    add_bullets(s, right_x + Inches(0.4), col_y + Inches(1.55), col_w - Inches(0.8), Inches(2.8),
                lm_bullets, size=14.5, color=TEXT_MAIN, space_after=12)

    add_text(s, Inches(0.55), Inches(6.75), Inches(11.8), Inches(0.4),
             footer_line, size=13.5, color=TEXT_FAINT, italic=True)
    add_footer(s)
    set_notes(s, notes)
    return s


# Slide 5 — Stage 1
stage_slide(
    "The Evolution · Stage 1", "04 / 08", 1, "Assisted Completion", "DONE", TEXT_FAINT,
    "Inline autocomplete",
    [
        "Early Copilot-style tools",
        "Human drives, AI suggests fragments",
        "Bounded to the next few lines",
    ],
    "AI-assisted campaign copy",
    [
        "AI helped write campaign copy & task descriptions",
        "Human still designed and assembled the whole campaign",
        "Useful, but narrow",
    ],
    "This was our starting point — already behind us.",
    "Stage one in coding was inline completion — tools like early Copilot suggesting the next few lines "
    "while a human still drove the whole thing. That was LaunchMinds' starting point too. Our AI helped "
    "generate campaign content — task descriptions, narrative copy — but a person still designed the "
    "strategy and assembled every piece by hand. Useful, but narrow.",
)

# Slide 6 — Stage 2
stage_slide(
    "The Evolution · Stage 2", "05 / 08", 2, "Single-Session Execution", "TODAY", ACCENT,
    "One session, full execution",
    [
        "A full brief goes in, one LLM session executes it end-to-end",
        "Bounded to one continuous session, one thread",
    ],
    "Registration → Plan → Deploy, in one pass",
    [
        "One session handles registration, strategy planning, AND deployment",
        "Powered by our internal skill system — encodes the full campaign schema",
        "Brief in, live campaign out — shipped and working today",
    ],
    "This is real. This is where LaunchMinds stands right now.",
    "Stage two in coding is where a single session can take a full task description and just execute it, "
    "start to finish, in one sitting. That's exactly where LaunchMinds is right now. Today, one session "
    "handles project registration, campaign strategy planning, and deployment to the platform — all in one "
    "pass. It's powered by our internal skill system, which encodes the entire campaign schema and workflow, "
    "so we go from a brief to a live campaign without switching tools or people. This is shipped. This is "
    "real, working today.",
)

# Slide 7 — Stage 3
stage_slide(
    "The Evolution · Stage 3", "06 / 08", 3, "Agent Mode", "NEXT MILESTONE", ACCENT2,
    "Persistent, multi-agent systems",
    [
        "Not one bounded session — a persistent system",
        "Multiple agents, each with a role",
        "Coordinate with each other over time",
    ],
    "A workspace per project, seeded by Harness",
    [
        "Persistent workspace for every project / brand",
        "Multiple “Minds” divide the labor: plan, execute, analyze, adjust",
        "A continuous, self-improving loop — not one-shot",
    ],
    "The milestone we're now chasing.",
    "Stage three in coding is agent mode — not one bounded session, but a persistent system of multiple "
    "agents, each with a role, coordinating over time. That's the milestone we're now chasing. We're "
    "building a persistent workspace for every project, seeded by Harness — our proprietary brand context. "
    "Inside it, multiple 'Minds' divide the labor: one plans the marketing strategy, one executes and "
    "deploys it, one analyzes how the campaign actually performed, and one feeds that analysis back into "
    "the next round's plan. Not one-shot — a continuous, self-improving loop.",
)

# ---------------------------------------------------------------------------
# Slide 8 — Sapien collaboration
# ---------------------------------------------------------------------------
s = new_slide()
add_kicker(s, "Partnership", "07 / 08")
add_text(s, Inches(0.55), Inches(1.05), Inches(11.5), Inches(0.7),
         "Raising the bar on analysis", size=36, color=TEXT_MAIN, bold=True)
add_badge(s, Inches(0.55), Inches(1.95), "EXPLORING · EARLY STAGE", WARN)
add_bullets(s, Inches(0.55), Inches(2.55), Inches(11.5), Inches(2.6), [
    "The “analyze” Mind is only as good as its rigor",
    "We're exploring a collaboration with Sapien",
    "Goal: combine forces for the most professional, rigorous marketing analysis possible",
    "Active conversation — not yet finalized",
], size=19, color=TEXT_MAIN, space_after=18)
add_footer(s)
set_notes(s, "One piece of that loop deserves special mention: the analysis Mind. Marketing attribution is hard "
             "to get right, and we want it to be genuinely rigorous, not just a dashboard. So we're currently "
             "exploring a collaboration with Sapien, with the goal of combining forces to deliver the most "
             "professional, rigorous marketing analysis in the space. It's early — an active conversation, not "
             "a done deal — but it's a direction we're excited about.")

# ---------------------------------------------------------------------------
# Slide 9 — Closing / Vision
# ---------------------------------------------------------------------------
s = new_slide()
add_kicker(s, "Where This Is Going", "08 / 08")
add_text(s, Inches(0.55), Inches(1.0), Inches(11.5), Inches(0.7),
         "Built. Shipping. Building next.", size=36, color=TEXT_MAIN, bold=True)

timeline_y = Inches(2.1)
stages = [
    ("Stage 1", "Content assistance", "DONE", TEXT_FAINT),
    ("Stage 2", "Single-session execution", "TODAY", ACCENT),
    ("Stage 3", "Agent mode workspace", "NEXT", ACCENT2),
]
tx = [Inches(0.55), Inches(4.75), Inches(8.95)]
tw = Inches(3.65)
for (label, desc, status, c), x in zip(stages, tx):
    add_rect(s, x, timeline_y, tw, Inches(1.7), BG_PANEL, radius=0.08)
    add_rect(s, x, timeline_y, tw, Inches(0.07), c)
    add_text(s, x + Inches(0.3), timeline_y + Inches(0.25), tw - Inches(0.6), Inches(0.4),
             label, size=15, color=c, bold=True)
    add_text(s, x + Inches(0.3), timeline_y + Inches(0.65), tw - Inches(0.6), Inches(0.6),
             desc, size=17, color=TEXT_MAIN, bold=True, line_spacing=1.15)
    add_badge(s, x + Inches(0.3), timeline_y + Inches(1.25), status, c)

add_text(s, Inches(0.55), Inches(4.25), Inches(12.2), Inches(1.0),
         "Structured, actionable workflows → scalable user growth, real brand impact.",
         size=21, color=ACCENT2, italic=True, line_spacing=1.3)
add_text(s, Inches(0.55), Inches(5.35), Inches(12.2), Inches(1.3),
         "We've built the first two stages. Now we're building the third.",
         size=26, color=TEXT_MAIN, bold=True)
add_text(s, Inches(0.55), Inches(6.35), Inches(6), Inches(0.5),
         "Thank you.", size=18, color=TEXT_DIM, italic=True)
add_footer(s, "LaunchMinds · 2026")
set_notes(s, "So to recap: we've already lived through the first two stages ourselves — content assistance, "
             "then full single-session execution, which is running today. The next milestone we're chasing is "
             "agent mode: persistent, per-brand workspaces where multiple Minds plan, execute, analyze, and "
             "adjust in a continuous loop. That's how we turn complex marketing needs into structured, "
             "actionable workflows — and that's what drives scalable user growth and real brand impact. We've "
             "built the first two stages. Now we're building the third. Thank you.")

prs.save("/tmp/claude-1000/-home-ubuntu/5e8a870b-0a20-4672-b81f-1aebc813a8e3/scratchpad/launchminds-deck/launchminds-deck.pptx")
print("Saved.")
