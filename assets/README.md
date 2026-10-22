# Visual assets

The identity follows the navy, teal, typography, and diagram language of [Awesome Reliable Text-to-SQL](https://github.com/duyvuleo/awesome-reliable-text-to-sql/tree/main/assets), adapted for this research toolkit. Both collections use CC0 for their original artwork.

| Asset | Use |
| --- | --- |
| [social-preview.png](social-preview.png) | GitHub/social card, 1280 × 640, below 1 MB. |
| [social-preview.svg](social-preview.svg) | Editable social-card source. |
| [banner-light.svg](banner-light.svg) | Light-theme README banner, 1280 × 360. |
| [banner-dark.svg](banner-dark.svg) | Dark-theme README banner, 1280 × 360. |

The graphic emphasizes **Compare · Evaluate · Reproduce**, with no changing catalog counts or performance claims. SVG title/description text and README alternative text describe the artwork.

Regenerate the editable sources:

    python3 scripts/build_visuals.py

Export social-preview.svg as a 1280 × 640 PNG with an SVG renderer, then visually inspect text, spacing, and labels. Arial or a metrically compatible sans-serif font is needed. Use a solid navy background (#101c2f) for the PNG so rounded corners remain predictable across sharing platforms.

The committed PNG was exported with CairoSVG 2.9.1 and Arial. With CairoSVG and its native Cairo library available, the export command is:

    cairosvg assets/social-preview.svg -b '#101c2f' --output-width 1280 --output-height 640 -o assets/social-preview.png

The SVG builder and validation checks themselves use only Python's standard library; the renderer is needed only when re-exporting the PNG.

    python3 scripts/build_visuals.py --check

This check verifies source consistency and PNG format/dimensions/file size; it does not compare raster pixels with the SVG. The README selects the light or dark banner automatically. Committing a PNG does not configure GitHub's social-preview setting: upload it under **Settings → General → Social preview → Edit → Upload an image**, following [GitHub's guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview).
