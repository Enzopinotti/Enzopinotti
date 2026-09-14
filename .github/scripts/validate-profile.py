#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
SETTINGS = ROOT / ".github" / "profile-3d-settings.json"
BRAND_SCRIPT = ROOT / ".github" / "scripts" / "brand-profile-3d.py"

REQUIRED_SECTIONS = [
    "01 // CURRENT MISSION",
    "02 // SELECTED BUILDS",
    "03 // BUILD SIGNAL LANDSCAPE",
    "04 // HOW I WORK",
    "05 // ENGINEERING MAP",
    "06 // CORE TOOLCHAIN",
    "07 // ENGINEERING PRINCIPLES",
]

REQUIRED_SVGS = [
    ROOT / "assets" / "enzo-engineering-hero.svg",
    ROOT / "assets" / "enzo-engineering-hero-light.svg",
    ROOT / "assets" / "how-i-work.svg",
    ROOT / "assets" / "how-i-work-light.svg",
    ROOT / "profile-3d-contrib" / "profile-enzo-dark.svg",
    ROOT / "profile-3d-contrib" / "profile-enzo-light.svg",
]

HEX_COLOR = re.compile(r"^#[0-9A-Fa-f]{6}$")
LOCAL_IMAGE = re.compile(r'(?:src|srcset)="(\./[^"]+)"')
LANDSCAPE_IMAGE = re.compile(
    r"\./profile-3d-contrib/profile-enzo-(?:dark|light)\.svg\?v=([0-9a-f]{12})"
)


def fail(message: str) -> None:
    print(f"profile validation failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate_readme() -> str:
    if not README.exists():
        fail("README.md is missing")

    text = README.read_text(encoding="utf-8")

    if len(text.encode("utf-8")) > 100_000:
        fail("README.md exceeded the 100 KiB profile budget")

    for section in REQUIRED_SECTIONS:
        if section not in text:
            fail(f"required section missing: {section}")

    for placeholder in ("YOUR-", "TODO", "example.com"):
        if placeholder in text:
            fail(f"placeholder leaked into README: {placeholder}")

    if "```mermaid" in text:
        fail("live Mermaid should not return to the profile; use repository-owned SVG assets")

    if "prefers-color-scheme: dark" not in text or "prefers-color-scheme: light" not in text:
        fail("README must provide adaptive dark/light imagery")

    if "business ↔ technology" not in text:
        fail("V3 delivery narrative is missing the business-to-technology bridge")

    landscape_versions = LANDSCAPE_IMAGE.findall(text)
    if len(landscape_versions) != 3:
        fail("README must version all three 3D landscape references")
    if len(set(landscape_versions)) != 1:
        fail("README 3D landscape references must share one cache version")

    for raw_path in LOCAL_IMAGE.findall(text):
        clean_path = raw_path.split("?", 1)[0].split("#", 1)[0]
        path = ROOT / clean_path.removeprefix("./")
        if not path.exists():
            fail(f"local image referenced by README does not exist: {raw_path}")

    return text


def validate_settings() -> None:
    try:
        settings = json.loads(SETTINGS.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"invalid profile 3D settings: {exc}")

    if not isinstance(settings, list) or len(settings) != 2:
        fail("profile 3D settings must define exactly dark and light themes")

    expected_files = {"profile-enzo-dark.svg", "profile-enzo-light.svg"}
    actual_files = {theme.get("fileName") for theme in settings}
    if actual_files != expected_files:
        fail(f"unexpected generated files: {sorted(actual_files)}")

    for theme in settings:
        if theme.get("type") != "normal":
            fail("V3 themes use deterministic normal color mode before branding")

        for key in ("backgroundColor", "foregroundColor", "strongColor", "weakColor", "radarColor"):
            value = theme.get(key)
            if not isinstance(value, str) or not HEX_COLOR.match(value):
                fail(f"invalid {key} in {theme.get('fileName')}: {value!r}")

        colors = theme.get("contribColors")
        if not isinstance(colors, list) or len(colors) != 5:
            fail(f"{theme.get('fileName')} must define five contribution colors")
        if any(not isinstance(color, str) or not HEX_COLOR.match(color) for color in colors):
            fail(f"invalid contribution color in {theme.get('fileName')}")


def validate_brand_script() -> None:
    if not BRAND_SCRIPT.exists():
        fail("3D branding postprocessor is missing")

    text = BRAND_SCRIPT.read_text(encoding="utf-8")
    for contract in (
        "ENZO_BUILD_SIGNAL_BRAND_START",
        "BUILD SIGNAL // ENZO PINOTTI",
        "profile-enzo-dark.svg",
        "profile-enzo-light.svg",
    ):
        if contract not in text:
            fail(f"3D branding postprocessor lost required contract: {contract}")


def validate_svgs() -> None:
    for svg in REQUIRED_SVGS:
        if not svg.exists():
            fail(f"required SVG is missing: {svg.relative_to(ROOT)}")
        try:
            root = ET.parse(svg).getroot()
        except ET.ParseError as exc:
            fail(f"invalid SVG XML in {svg.relative_to(ROOT)}: {exc}")
        if not root.tag.endswith("svg"):
            fail(f"unexpected root element in {svg.relative_to(ROOT)}")


def main() -> None:
    validate_readme()
    validate_settings()
    validate_brand_script()
    validate_svgs()
    print("profile validation passed")


if __name__ == "__main__":
    main()
