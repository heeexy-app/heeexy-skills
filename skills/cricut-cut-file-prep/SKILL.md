---
name: cricut-cut-file-prep
description: Check and fix SVG cut files for Cricut Design Space and Silhouette Studio - layers by color, welded text, no open paths or tiny pieces, correct size - and write the buyer's how-to. Use when the user has an SVG/DXF for cutting vinyl, HTV, paper or cardstock, or asks why a file cuts badly.
license: MIT
---

# Cricut and Silhouette cut-file prep

## Inspect the SVG

Read the file and report:
- Canvas size (`viewBox`, `width`, `height`) and the intended real-world size. Set `width`/`height` in inches (for example `width="10in"`) so the file opens at the right size; always tell the buyer to check the size after upload.
- Number of fill colors (each becomes a layer), strokes (Design Space ignores most strokes or turns them into cut lines), gradients and raster `<image>` elements (cannot be cut).
- Open paths, very small shapes (under 0.1 inch), thin parts (under 0.04 inch for vinyl, 0.06 inch for HTV), overlapping shapes of the same color, and text that is still live `<text>`.

## Fix it (edit the SVG)

1. Convert strokes to filled outlines when the line must be cut; remove decorative strokes.
2. Remove gradients and images; replace with flat colors.
3. Group shapes by color: one `<g id="layer-color-name">` per vinyl color, top layers last.
4. Merge overlapping same-color shapes into one path (union) so the machine cuts the outer edge only.
5. Thicken or delete parts that are too thin; join letters of script fonts so they weld into one piece.
6. Text: convert to paths, or tell the user to "Weld" script text in Design Space.
7. Set a sensible default size (shirts 10–11 inch wide, tumblers 3–4 inch tall, decals 3–6 inch).

## Buyer how-to (include with the file)

Upload → Design Space: Upload Image → Browse → select the SVG → Add to Canvas. Resize with the lock on. For multi-color HTV: cut each color layer, mirror for iron-on, weed, then press from bottom layer to top. Silhouette: use the DXF or (Designer Edition) the SVG.

## Quality bar

Every layer cuts without stray specks, inside letters (o, a, e) keep their holes (`fill-rule="evenodd"`), and the preview at actual size has no part thinner than the limits above.

---
No SVG yet? Convert a PNG for free with the [image to SVG for Cricut tool](https://heeexy.app/tools/image-to-svg-for-cricut), make a [QR code SVG](https://heeexy.app/tools/qr-code-generator), or draw a new vector in [HEEEXY AI Studio](https://heeexy.app/?mode=vector).
