# Profile design system

The palette comes from the portfolio’s [design.css](https://github.com/vishaka1203/vishaka-parab-portfolio/blob/main/src/app/design.css). The [token file](../data/design-tokens.json) records all literal colour values in its active light and dark declarations. The deployed stylesheet also includes earlier base tokens. Its later design declarations supply the palette used here.

| Token | Light | Dark | Use |
| --- | --- | --- | --- |
| Paper | `#f3f5f0` | `#0b1511` | Asset background |
| Surface | `#ffffff` | `#14231c` | Metric cards and diagram nodes |
| Ink | `#152a23` | `#f1f2e9` | Main text |
| Muted | `#52665c` | `#afbeb2` | Secondary text |
| Line | `#d5dfd6` | `#2e4335` | Decorative rules only |
| Accent | `#164f3d` | `#b6d9bc` | Jade emphasis, bars, and diagram lines |
| Soft | `#e4ede4` | `#1b3023` | Bar tracks and dark hero panel |
| Panel | `#eaf0e7` | `#102219` | Supporting surfaces |
| Champagne | `#806235` | `#ceb989` | Metric labels and editorial highlights |

Use an approximate **60–30–10** composition across assets. Neutral backgrounds carry the largest area, jade groups major visual elements, and champagne marks selected values and taglines. The hero uses an approximately one-third illustration panel. Align asset blocks to an 8 px grid and use 4 px corrections for optical alignment. Keep symbols geometric and consistent at a 2–3 px stroke. Reserve the `vp.` mark for the hero and closing line.

The portfolio declares Manrope and Cormorant Garamond Italic in [layout.tsx](https://github.com/vishaka1203/vishaka-parab-portfolio/blob/main/src/app/layout.tsx). The hero embeds those WOFF2 files with local fallback fonts. GitHub supplies Markdown typography. Charts use system sans-serif, direct labels, a zero baseline, and a 0–100 scale for percentages and scores. Diagram arrows and labels carry meaning without relying on colour. Screenshots use actual browser captures and descriptive alternative text.

## Contrast

Ratios use the WCAG relative luminance formula. The target for text is 4.5:1. Essential strokes and fills target 3:1.

| Foreground / background | Light | Dark | Purpose |
| --- | ---: | ---: | --- |
| Ink / paper | 13.79 | 16.48 | Main text |
| Muted / paper | 5.60 | 9.59 | Captions and supporting text |
| Accent / paper | 8.62 | 12.08 | Mark and primary accents |
| Champagne / paper | 5.15 | 9.67 | Tagline and chart values |
| Accent / surface | 9.46 | 10.60 | Metric values and diagram outlines |
| Ink / surface | 15.14 | 14.47 | Card and diagram labels |
| Accent / soft | 7.90 | 9.13 | Chart fills and dark hero strokes |
| Paper / accent (light illustration) | 8.62 | — | Hero geometric strokes |
| Line / paper | 1.25 | 1.74 | Decorative only |

Meaningful content has a text equivalent in Markdown or in the linked metric data and case studies. Use paired variants in `picture` with light image fallback. Check the README at narrow widths in both themes. Keep any additional project under a heading with a one-paragraph problem and implementation summary, an optional real screenshot, and verified source, live, and case study links. For open-source entries, add the repository, concrete contribution, status, and an upstream evidence link.

Regenerate the SVGs with `python3 scripts/generate-assets.py` after changing tokens, metrics, or the generator.
