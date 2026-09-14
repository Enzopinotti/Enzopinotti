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

REQUIRED_SECTIONS = [
    "01 // CURRENT MISSION",
    "02 // ENGINEERING MAP",
    "03 // SELECTED BUILDS",
    "04 // HOW I BUILD",
    "05 // ACTIVITY LANDSCAPE",
    "06 // CORE TOOLCHAIN",
    "07 // ENGINEERING PRINCIPLES",
]

REQUIRED_SVGS = [
    ROOT / "assets" / "enzo-engineering-hero.svg",
    ROOT / "assets" / "enzo-engineering-hero-light.svg",
    ROOT / "profile-3d-contrib" / "profile-enzo-dark.svg",
    ROOT / "profile-3d-contrib" / "profile-enzo-light.svg",
]

HEX_COLOR = re.compile(r"^#[0-9A-Fa-f]{6}$")
LOCAL_IMAGE = re.compile(r"(?:src|srcset)=\"(\./[^\"]+)\"")
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

    if "prefers-color-scheme: dark" not in text or "prefers-color-scheme: light" not in text:
        fail("README must provide adaptive dark/light imagery")

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
            fail("V1 themes must use the deterministic normal color mode")

        for key in ("backgroundColor", "foregroundColor", "strongColor", "weakColor", "radarColor"):
            value = theme.get(key)
            if not isinstance(value, str) or not HEX_COLOR.match(value):
                fail(f"invalid {key} in {theme.get('fileName')}: {value!r}")

        colors = theme.get("contribColors")
        if not isinstance(colors, list) or len(colors) != 5:
            fail(f"{theme.get('fileName')} must define five contribution colors")
        if any(not isinstance(color, str) or not HEX_COLOR.match(color) for color in colors):
            fail(f"invalid contribution color in {theme.get('fileName')}")


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
    validate_svgs()
    print("profile validation passed")


if __name__ == "__main__":
    main()
