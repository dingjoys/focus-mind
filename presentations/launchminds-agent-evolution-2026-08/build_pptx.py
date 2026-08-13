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
                 font=FONT, space_after=10, line_spacing=1.2):
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


def add_footer(slide, text="LaunchMinds  ·  Built on Minds  ·  2026"):
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
add_text(s, Inches(0.9), Inches(1.85), Inches(11), Inches(0.5),
         "LAUNCHMINDS", size=20, color=ACCENT2, bold=True)
add_text(s, Inches(0.85), Inches(2.3), Inches(11.5), Inches(1.9),
         "From Assistant\nto Autonomous", size=54, color=TEXT_MAIN, bold=True, line_spacing=1.05)
add_text(s, Inches(0.9), Inches(4.3), Inches(10.5), Inches(0.6),
         "Built on Minds, from day one.",
         size=19, color=TEXT_DIM, italic=True)
add_bullets(s, Inches(0.9), Inches(5.1), Inches(10.8), Inches(1.8), [
    "AI-native, end-to-end brand marketing platform",
    "Powered by Minds, built with Harness",
    "A partnership story, not just a product demo",
], size=15, color=TEXT_DIM, space_after=8)
add_footer(s, "LaunchMinds · 2026")
set_notes(s, "Good [morning/afternoon] — today I want to walk you through how LaunchMinds is evolving, from "
             "an assistant to something increasingly autonomous, and what that's been like to build on Minds. "
             "Our name isn't an accident: Launch, plus Minds. We picked it because Minds is the foundation "
             "everything we do stands on — the same role Claude or GPT-4 plays for other companies, Minds "
             "plays for us. What you'll see today is proof of what that foundation makes possible, and where "
             "we want to take it next, together.")

# ---------------------------------------------------------------------------
# Slide 2 — The Problem
# ---------------------------------------------------------------------------
s = new_slide()
add_kicker(s, "The Problem", "01 / 07")
add_text(s, Inches(0.55), Inches(1.05), Inches(11.5), Inches(1.3),
         "Marketing today is stitched\ntogether by hand", size=36, color=TEXT_MAIN, bold=True, line_spacing=1.1)
add_bullets(s, Inches(0.55), Inches(2.85), Inches(11.5), Inches(3.2), [
    "One tool for campaign design, another for deployment, a spreadsheet for the rest",
    "Campaign design, deployment, resource orchestration — all disconnected",
    "It doesn't scale, and it doesn't get smarter over time",
    "The fix isn't another point tool — it's a system that reasons across the whole lifecycle",
], size=19, color=TEXT_MAIN, space_after=18)
add_footer(s)
set_notes(s, "Brand marketing today is stitched together by hand — one tool for campaign design, another for "
             "deployment, a spreadsheet for resource orchestration, and a person holding it all in their head. "
             "That doesn't scale, and it doesn't get smarter over time. We don't think the fix is another point "
             "tool. It's a system that reasons across the entire lifecycle — and that requires real intelligence "
             "at the core, not automation scripts with an AI label on them.")

# ---------------------------------------------------------------------------
# Slide 3 — Positioning: Harness + Minds
# ---------------------------------------------------------------------------
s = new_slide()
add_kicker(s, "Positioning", "02 / 07")
add_text(s, Inches(0.55), Inches(1.0), Inches(11.5), Inches(0.7),
         "LaunchMinds = Harness + Minds", size=34, color=TEXT_MAIN, bold=True)

# two-part layer diagram
layer_y = Inches(1.85)
layer_h = Inches(1.0)
harness_box = add_rect(s, Inches(0.55), layer_y, Inches(5.4), layer_h, BG_PANEL, radius=0.08)
add_text(s, Inches(0.9), layer_y + Inches(0.16), Inches(4.7), Inches(0.35),
         "HARNESS", size=15, color=ACCENT2, bold=True)
add_text(s, Inches(0.9), layer_y + Inches(0.52), Inches(4.7), Inches(0.4),
         "Context layer — proprietary enterprise memory", size=13.5, color=TEXT_DIM)
add_text(s, Inches(6.15), layer_y + Inches(0.28), Inches(0.5), Inches(0.5),
         "+", size=30, color=TEXT_FAINT, align=PP_ALIGN.CENTER)
minds_box = add_rect(s, Inches(6.85), layer_y, Inches(5.4), layer_h, BG_PANEL2, radius=0.08)
add_rect(s, Inches(6.85), layer_y, Inches(0.08), layer_h, ACCENT)
add_text(s, Inches(7.2), layer_y + Inches(0.16), Inches(4.7), Inches(0.35),
         "MINDS", size=15, color=ACCENT, bold=True)
add_text(s, Inches(7.2), layer_y + Inches(0.52), Inches(4.7), Inches(0.4),
         "Model layer — the reasoning engine underneath", size=13.5, color=TEXT_DIM)

quote_box = add_rect(s, Inches(0.55), Inches(3.2), Inches(12.2), Inches(2.05), BG_PANEL, radius=0.06)
add_rect(s, Inches(0.55), Inches(3.2), Inches(0.09), Inches(2.05), ACCENT2)
add_text(s, Inches(1.0), Inches(3.4), Inches(11.3), Inches(1.7),
         "“LaunchMinds is an AI-native, end-to-end brand marketing platform that "
         "leverages Harness to build proprietary enterprise contexts, automating the "
         "entire lifecycle from campaign design and multi-platform deployment to "
         "resource orchestration.”",
         size=18.5, color=TEXT_MAIN, italic=True, line_spacing=1.28)
add_text(s, Inches(0.55), Inches(5.55), Inches(11.8), Inches(0.9),
         "Harness without Minds is just a database. Minds without Harness is generic.\n"
         "Together, that's Minds-driven — not just Minds-adjacent.",
         size=16.5, color=ACCENT2, italic=True, line_spacing=1.3)
add_footer(s)
set_notes(s, "[read core line]. Two things are doing the work here, and they're worth separating for this room. "
             "Harness is our layer — the proprietary context and memory that make a plan actually understand a "
             "specific brand, a specific market, a specific history of what's worked before. Minds is what "
             "Harness runs on — the model layer, the actual reasoning underneath every plan we generate. "
             "Harness without Minds is just a database. Minds without Harness is generic. Together, that's what "
             "makes this Minds-driven, not just Minds-adjacent.")

# ---------------------------------------------------------------------------
# Slide 4 — How Agents Evolve (framework intro)
# ---------------------------------------------------------------------------
s = new_slide()
add_kicker(s, "The Framework", "03 / 07")
add_text(s, Inches(0.55), Inches(1.05), Inches(11.5), Inches(0.7),
         "How agents evolve", size=36, color=TEXT_MAIN, bold=True)
add_text(s, Inches(0.55), Inches(1.85), Inches(11.8), Inches(0.9),
         "The same arc coding tools went through.\nWe're climbing it stage by stage — natively on Minds.",
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
        add_text(s, x + box_w + Inches(0.05), box_y + Inches(0.95), Inches(0.5), Inches(0.6),
                 "→", size=30, color=TEXT_DIM, align=PP_ALIGN.CENTER)
add_text(s, Inches(0.55), Inches(6.05), Inches(11.8), Inches(0.7),
         "Each stage is a Minds workflow — not a script with a model bolted on.",
         size=17, color=ACCENT2, italic=True)
add_footer(s)
set_notes(s, "If you've watched how coding assistants evolved, you've seen this arc: first, assisted "
             "completion — suggestions, not action. Then single-session execution — an agent that completes a "
             "full task in one sitting, with a human watching. Then true agent mode — long-running, autonomous, "
             "checking its own work. We're building LaunchMinds through that same three-stage arc, applied to "
             "brand marketing instead of code. And because we built it Minds-native from the start, each stage "
             "is a Minds workflow — not a script with a model bolted on.")


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
             "ON MINDS, IN LAUNCHMINDS", size=14, color=status_color, bold=True)
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
    "The Evolution · Stage 1", "04 / 07", 1, "Assisted Completion", "DONE", TEXT_FAINT,
    "Inline suggestions, not action",
    [
        "Suggestions only — human reviews every one",
        "Human stays in control of the outcome",
    ],
    "Minds-assisted campaign drafting",
    [
        "Minds proposes structure, drafts copy",
        "Pulls in context Harness has already stored",
        "Human in the loop at every step",
    ],
    "Already saving our team real hours today.",
    "Stage one is done and live. This is assisted completion — Minds helping a human draft a campaign: "
    "proposing structure, pulling in context Harness has stored, drafting copy. The human stays in the loop "
    "at every step. It's the smallest, safest version of Minds-driven work, and it's already saving our team "
    "real hours today.",
)

# Slide 6 — Stage 2
stage_slide(
    "The Evolution · Stage 2", "05 / 07", 2, "Single-Session Execution", "TODAY", ACCENT,
    "Full task, one sitting, human watching",
    [
        "One session completes an entire task",
        "A human observes, doesn't drive step by step",
    ],
    "One session, one Mind, full pipeline",
    [
        "Registration + planning + deployment — no handoffs between tools",
        "Runs on our internal skill system: structured capabilities we hand to Minds so it can act, not just suggest",
        "Minds doing real autonomous work within a session",
    ],
    "The first stage where Minds truly acts, not just assists.",
    "Stage two is what's live right now. One session, one Mind, handling registration, "
    "planning, and deployment end to end — no handoffs between tools. It runs through our internal skill "
    "system, which is essentially a set of structured capabilities we hand to Minds so it can act, not just "
    "suggest. This is the first stage where Minds does real work autonomously within a session.",
)

# Slide 7 — Stage 3
stage_slide(
    "The Evolution · Stage 3", "06 / 07", 3, "Agent Mode", "NEXT MILESTONE", ACCENT2,
    "Long-running, autonomous, self-checking",
    [
        "Not one session — a persistent, ongoing system",
        "Checks and corrects its own work over time",
    ],
    "A workspace of coordinating Minds",
    [
        "Per-project workspace: multiple Minds instances coordinating",
        "No fixed pipeline of roles — the group's shape adapts to what the campaign needs",
        "Where we push toward real multi-agent coordination on your platform",
    ],
    "The clearest place you'll see what your platform makes possible.",
    "Stage three is our next milestone, and it's the part I think matters most for this room. We're building "
    "a per-project workspace where multiple Minds instances coordinate with each other — thinking through "
    "strategy, executing it, reading the results, and adjusting together. We're not locking that into a fixed "
    "pipeline of roles; the shape of that group adapts to what each campaign actually needs. This is the "
    "clearest place you'll see what your platform makes possible when we push it toward real multi-agent "
    "coordination.",
)

# ---------------------------------------------------------------------------
# Slide 8 — Closing / Vision
# ---------------------------------------------------------------------------
s = new_slide()
add_kicker(s, "Where This Goes", "07 / 07")
add_text(s, Inches(0.55), Inches(1.0), Inches(11.5), Inches(0.7),
         "Built on Minds — with Minds' community", size=32, color=TEXT_MAIN, bold=True)

timeline_y = Inches(2.0)
stages = [
    ("Stage 1", "Minds-assisted drafting", "DONE", TEXT_FAINT),
    ("Stage 2", "One Mind, full session", "TODAY", ACCENT),
    ("Stage 3", "Multi-Mind workspace", "NEXT", ACCENT2),
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

add_text(s, Inches(0.55), Inches(4.0), Inches(12.2), Inches(0.9),
         "Not an integration bolted on after the fact — built on Minds from day one.",
         size=19, color=ACCENT2, italic=True, line_spacing=1.3)
add_text(s, Inches(0.55), Inches(4.85), Inches(12.2), Inches(1.4),
         "What gets built on top of a platform is the best answer\na platform can have.",
         size=25, color=TEXT_MAIN, bold=True, line_spacing=1.2)
add_text(s, Inches(0.55), Inches(6.15), Inches(11.5), Inches(0.6),
         "We'd like to keep building that answer together — with your platform, and with your community.",
         size=15.5, color=TEXT_DIM, italic=True)
add_text(s, Inches(0.55), Inches(6.72), Inches(6), Inches(0.4),
         "Thank you.", size=16, color=TEXT_DIM, italic=True)
add_footer(s, "LaunchMinds · 2026")
set_notes(s, "So: two stages built and live today, one stage actively in motion, built on Minds from day one — "
             "not as an integration bolted on after the fact, but as the foundation. We're showing you this "
             "because we think it's a good answer to the question every platform has to answer eventually: "
             "what gets built on top of us? We'd like to keep building that answer together — with your "
             "platform, and with your community. Thanks for the time.")

prs.save("/tmp/claude-1000/-home-ubuntu/5e8a870b-0a20-4672-b81f-1aebc813a8e3/scratchpad/launchminds-deck/launchminds-deck.pptx")
print("Saved.")
