# Diagram Design Prompt Pack

Ten ready-to-paste prompts for **diagram-design**, the free, open-source (MIT) agent skill by Cathryn Lavery that turns one plain sentence into an editorial diagram saved as ONE self-contained HTML + SVG file (52 diagram types).
Skill: https://github.com/cathrynlavery/diagram-design

## Who it is for
Creators, founders, developers, teachers: anyone who needs a clean diagram for a video, a doc, a pitch or a README and does not want to open a design tool.

## Step by step
1. You need an AI agent that reads Agent Skills: Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI, Cline, Windsurf, Amp, Qoder (the skill is free; the agent is your own and may be on a paid plan).
2. Install the skill with one line in your terminal:
   `npx skills add cathrynlavery/diagram-design`
   (Claude Code also: `/plugin marketplace add cathrynlavery/diagram-design` then `/plugin install diagram-design@diagram-design`)
3. Optional, once: make every diagram match your brand:
   `Onboard diagram-design to https://yoursite.com`
4. Paste a prompt below, replace the words in CAPITALS, open the `.html` file it writes (double-click).
5. Need a PNG or SVG? In Claude Code: `/diagram-design:export-diagram path/to/diagram.html`

## The prompts
Prompts 1 and 2 are the exact prompts we tested on camera (2026-11-23); 3-5 are the examples from the skill's own README; 6-10 are our templates.

1. `Make me an architecture diagram of my video pipeline: script writer, critic, voice clone, renderer, quality check, delivery to my PC.`  (tested: the skill picked Architecture)
2. `I need a quadrant showing my YouTube video ideas by effort vs views: AI news recap, free tool Short, long tutorial, concept explainer, live coding stream.`  (tested: the skill picked Quadrant)
3. `Make me an architecture diagram of my app: frontend, backend, database, Redis cache.`
4. `I need a quadrant showing Q2 projects by impact vs effort.`
5. `Give me a sequence of a bearer call with token refresh on 401.`
6. `Draw the customer journey of MY PRODUCT from first ad to paid plan: STEP, STEP, STEP. Mark where people drop off.`
7. `Make a timeline of MY PROJECT from DATE to DATE with these milestones: A, B, C. Highlight the launch.`
8. `Make an org chart of my team: NAMES AND ROLES. Highlight who I report to.`
9. `Draw a flowchart of how a support ticket moves: new, triage, fix, review, closed, with the loop back when review fails.`
10. `Make a sankey of where my monthly budget goes: TOTAL, then CATEGORIES with amounts. Highlight the biggest leak.`

## Tips
- Say the diagram type if you know it ("quadrant", "timeline", "sequence"); otherwise the agent picks one and states its plan.
- One thing to highlight per diagram: the skill keeps one accent colour for the 1-2 things that matter.
- Licence of the skill: MIT (free of charge). This pack: free, MIT.
