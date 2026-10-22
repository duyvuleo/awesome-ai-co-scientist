"""Build editable SVG identity assets; check the GitHub PNG export dimensions."""
import argparse
from html import escape
from pathlib import Path
import struct

ROOT = Path(__file__).resolve().parents[1]
PALETTES = {
    "light": {"bg": "#f6f8fc", "ink": "#172b45", "muted": "#50627a",
              "line": "#c8d5e3", "panel": "#ffffff",
              "accents": ("#168571", "#315da7", "#93601d")},
    "dark": {"bg": "#101c2f", "ink": "#f1f5fc", "muted": "#b8c8db",
             "line": "#3c506c", "panel": "#192a42",
             "accents": ("#74d7c4", "#9bbcf6", "#edc179")},
}


def graphic(social=False, theme="light"):
    palette = PALETTES[theme]
    height = 640 if social else 360
    size = 78 if social else 68
    first, second = (244, 336) if social else (156, 232)
    subtitle, footer = (414, 568) if social else (286, 330)
    top = 174 if social else 62
    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="{height}" viewBox="0 0 1280 {height}" role="img" aria-labelledby="title desc">',
        "<title id=\"title\">Awesome AI Co-Scientist</title>",
        "<desc id=\"desc\">A community research toolkit for comparing AI co-scientists, evaluating evidence, and reproducing bounded results. A research question branches to Compare, Evaluate, and Reproduce.</desc>",
        f'<rect width="1280" height="{height}" rx="24" fill="{palette["bg"]}"/>',
        '<rect x="72" y="54" width="34" height="5" rx="2.5" fill="#37b4a0"/>',
    ]

    def text(x, y, value, size, color=None, weight=400, anchor="start", spacing=None):
        tracking = f' letter-spacing="{spacing}"' if spacing is not None else ""
        elements.append(
            f'<text x="{x}" y="{y}" font-family="Arial, Helvetica, sans-serif" '
            f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" '
            f'fill="{color or palette["ink"]}"{tracking}>{escape(value)}</text>'
        )

    text(72, 90, "AWESOME RESEARCH TOOLKIT", 15, palette["muted"], 600, spacing=2.2)
    text(68, first, "AI", size, weight=700)
    text(68, second, "Co-Scientist", size, weight=700)
    text(72, subtitle, "Capabilities · Evidence · Reproducibility", 21, palette["muted"])
    text(72, footer, "duyvuleo / awesome-ai-co-scientist", 15, palette["muted"])
    elements.append(f'<rect x="830" y="{top}" width="300" height="58" rx="14" fill="{palette["panel"]}" stroke="{palette["line"]}"/>')
    text(980, top + 36, "Research question", 21, weight=600, anchor="middle")
    elements.append(
        f'<path d="M 980 {top + 58} V {top + 92} M 840 {top + 118} V {top + 92} '
        f'H 1120 V {top + 118} M 980 {top + 92} V {top + 118}" '
        f'stroke="{palette["line"]}" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    )
    for x, label, color in zip((780, 920, 1060), ("Compare", "Evaluate", "Reproduce"), palette["accents"]):
        elements.append(f'<rect x="{x}" y="{top + 118}" width="120" height="76" rx="14" fill="{palette["panel"]}" stroke="{palette["line"]}"/>')
        elements.append(f'<circle cx="{x + 60}" cy="{top + 140}" r="4" fill="{color}"/>')
        text(x + 60, top + 172, label, 18, color, 600, anchor="middle")
    text(980, top + 241, "Papers · Systems · Tools", 18, palette["muted"], anchor="middle")
    elements.append("</svg>")
    return "\n".join(elements) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check sources and PNG size without writing")
    args = parser.parse_args()
    folder = ROOT / "assets"
    outputs = {f"banner-{theme}.svg": graphic(theme=theme) for theme in PALETTES}
    outputs["social-preview.svg"] = graphic(social=True, theme="dark")
    if args.check:
        for name, expected in outputs.items():
            path = folder / name
            if not path.is_file() or path.read_text(encoding="utf-8") != expected:
                parser.exit(1, f"Regenerate {name} with scripts/build_visuals.py\n")
        png = folder / "social-preview.png"
        if not png.is_file():
            parser.exit(1, "Export assets/social-preview.png from the SVG.\n")
        data = png.read_bytes()
        if (data[:8] != b"\x89PNG\r\n\x1a\n" or len(data) < 24
                or struct.unpack(">II", data[16:24]) != (1280, 640) or len(data) >= 1_000_000):
            parser.exit(1, "Social PNG must be 1280 by 640 pixels and below 1 MB.\n")
        print("Checked three SVG sources and the 1280 × 640 social PNG.")
    else:
        folder.mkdir(exist_ok=True)
        for name, content in outputs.items():
            (folder / name).write_text(content, encoding="utf-8")
        print("Built light/dark banners and social-preview SVG. Export the PNG after artwork changes.")


if __name__ == "__main__":
    main()
