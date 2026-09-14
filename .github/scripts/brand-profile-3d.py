#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / "profile-3d-contrib"

FILES = {
    "profile-enzo-dark.svg": {
        "panel": "#020617",
        "stroke": "#1E293B",
        "title": "#F8FAFC",
        "muted": "#94A3B8",
        "violet": "#8B5CF6",
        "cyan": "#22D3EE",
        "amber": "#F59E0B",
    },
    "profile-enzo-light.svg": {
        "panel": "#FFFFFF",
        "stroke": "#CBD5E1",
        "title": "#0F172A",
        "muted": "#64748B",
        "violet": "#7C3AED",
        "cyan": "#0891B2",
        "amber": "#D97706",
    },
}

START = "<!-- ENZO_BUILD_SIGNAL_BRAND_START -->"
END = "<!-- ENZO_BUILD_SIGNAL_BRAND_END -->"
EXISTING_BRAND = re.compile(
    re.escape(START) + r".*?" + re.escape(END),
    re.DOTALL,
)


def brand(svg_path: Path, colors: dict[str, str]) -> None:
    text = svg_path.read_text(encoding="utf-8")
    text = EXISTING_BRAND.sub("", text)

    block = f"""
{START}
<g id="enzo-build-signal-brand" aria-label="Enzo Pinotti build signal landscape">
  <rect x="34" y="28" width="430" height="86" rx="18"
        fill="{colors['panel']}" fill-opacity="0.86"
        stroke="{colors['stroke']}" stroke-width="1.5"/>
  <circle cx="58" cy="52" r="5" fill="{colors['cyan']}"/>
  <text x="74" y="57"
        fill="{colors['muted']}"
        font-family="ui-monospace,SFMono-Regular,Menlo,monospace"
        font-size="12" font-weight="700" letter-spacing="1.1">
    BUILD SIGNAL // ENZO PINOTTI
  </text>
  <text x="58" y="82"
        fill="{colors['title']}"
        font-family="Ubuntu,Helvetica,Arial,sans-serif"
        font-size="15" font-weight="700">
    public engineering activity
  </text>
  <text x="58" y="101"
        fill="{colors['muted']}"
        font-family="ui-monospace,SFMono-Regular,Menlo,monospace"
        font-size="10">
    issues · commits · reviews · shipped iterations
  </text>
  <rect x="352" y="48" width="24" height="4" rx="2" fill="{colors['violet']}"/>
  <rect x="382" y="48" width="24" height="4" rx="2" fill="{colors['cyan']}"/>
  <rect x="412" y="48" width="24" height="4" rx="2" fill="{colors['amber']}"/>
</g>
{END}
"""

    if "</style>" not in text:
        raise SystemExit(f"{svg_path.name}: expected generator style block")

    updated = text.replace("</style>", f"</style>{block}", 1)
    svg_path.write_text(updated, encoding="utf-8")
    print(f"branded {svg_path.relative_to(ROOT)}")


def main() -> None:
    for filename, colors in FILES.items():
        path = OUTPUT_DIR / filename
        if not path.exists():
            raise SystemExit(f"missing generated landscape: {path}")
        brand(path, colors)


if __name__ == "__main__":
    main()
