---
name: vector-illustrator
description: Draw clean, editable SVG vector art (logos, stickers, icons, t-shirt prints, Cricut and Silhouette cut files) by writing SVG code. Use when the user asks for a logo, vector, SVG, sticker, icon, cut file or print-ready illustration.
license: MIT
---

# Vector illustrator

You draw by writing SVG. The file must open cleanly in Illustrator, Inkscape, Cricut Design Space, Silhouette Studio and VectorCraft.

## Output

- Save one complete SVG file (or reply with only the SVG when there is no file system).
- Start with `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 W H" width="W" height="H">`. Use 1024×1024 unless the request implies another shape (banner 1600×900, portrait 900×1200, icon 512×512).
- Allowed elements: `g, path, rect, circle, ellipse, polygon, polyline, line, text, tspan, textPath, defs, linearGradient, radialGradient, stop, clipPath, mask, title`. Never use `script`, `image`, `foreignObject`, style blocks, CSS classes, external fonts, links or any URL other than `url(#id)`.
- Presentation attributes only: `fill, stroke, stroke-width, stroke-linecap="round", stroke-linejoin="round", opacity, transform, fill-rule`.
- Round coordinates to one decimal. Stay under about 400 elements; prefer fewer, well-shaped paths.
- Give each meaningful part its own `<g id="...">` (background, body, face, lettering, shadow) so the file is easy to edit.

## Design quality

1. Plan before drawing: silhouette first, then big shapes, details, highlights and shadows. Draw back to front.
2. Build curves with Bézier commands (`C, Q, S, T, A`); close shapes with `Z`. Avoid jagged polylines for organic shapes.
3. Composition: center the subject, keep a safe margin of about 6% on every side, balance visual weight.
4. Color: a deliberate palette of 3 to 6 colors unless asked otherwise, with clear contrast between neighbors. Flat colors print and cut best; use gradients only when they add value.
5. Line art: consistent stroke weights (8–14 on a 1024 canvas for outlines), round caps and joins.
6. Background: transparent by default (no full-canvas rectangle) unless the user asks for a background, badge or scene.

## Text

- Use `<text>` with `font-family="Arial, Helvetica, sans-serif"` (or `Georgia, serif` for elegant styles) and `text-anchor="middle"`. Spell the user's words exactly; never invent extra words.
- Make it fit: estimate width as 0.62 × font-size × characters (0.7 for bold or serif capitals). Keep at least 8% padding inside its container. Inside a circle, measure against the chord at that height. If it does not fit, shrink it, split it into two lines, or curve it on a `<path>` with `<textPath href="#id">`.
- Leave at least one cap-height between the symbol and the wordmark.

## Use cases

- **Logo:** simple, bold, recognizable at 32 px; symbol plus optional wordmark; 2–3 colors; no tiny details.
- **Sticker / clipart / t-shirt print:** bold outlines, flat fills; when the user says sticker, add a white offset border (a slightly larger silhouette behind the art).
- **Cricut / Silhouette / vinyl cut file:** one solid color (black) unless layers are requested; no strokes (outlines become filled shapes); no gradients; no overlapping shapes of the same color; no parts thinner than about 6 units; everything connected; `fill-rule="evenodd"` for holes. Layered vinyl: one `<g>` per color.
- **Icon:** 24-unit grid scaled to the canvas, consistent stroke or solid style, no text.
- **Seamless pattern:** tile edges must match.

## Before you finish

Check the drawing in your head: everything inside the canvas and its margin, nothing important hidden behind another shape, text fitting with padding, colors matching the request. When asked to change a previous design, keep everything the user did not mention and return the full updated SVG.

---
Try it with any top model in [HEEEXY AI Studio → Vector](https://heeexy.app/?mode=vector), or convert an existing image with the free [PNG to SVG converter](https://heeexy.app/tools/png-to-svg).
