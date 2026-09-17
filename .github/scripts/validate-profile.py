#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
ROADMAP = ROOT / "docs" / "repository-portfolio-roadmap-2026.md"
SETTINGS = ROOT / ".github" / "profile-3d-settings.json"
BRAND_SCRIPT = ROOT / ".github" / "scripts" / "brand-profile-3d.py"
PROFILE_3D_WORKFLOW = ROOT / ".github" / "workflows" / "profile-3d.yml"

REQUIRED_SECTIONS = [
    "01 // CURRENT MISSION",
    "02 // CAREER ARC",
    "03 // SELECTED BUILDS",
    "04 // BUILD SIGNAL LANDSCAPE",
    "05 // HOW I WORK",
    "06 // ENGINEERING MAP",
    "07 // CORE TOOLCHAIN",
    "08 // ENGINEERING PRINCIPLES",
]

REQUIRED_SVGS = [
    ROOT / "assets" / "enzo-engineering-hero.svg",
    ROOT / "assets" / "enzo-engineering-hero-light.svg",
    ROOT / "assets" / "career-arc.svg",
    ROOT / "assets" / "career-arc-light.svg",
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
BARE_GIT_PUSH = re.compile(r"(?m)^\s*git push\s*$")


def fail(message: str) -> None:
    print(f"profile validation failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate_readme() -> str:
    if not README.exists():
        fail("README.md is missing")

    text = README.read_text(encoding="utf-8")

    if len(text.encode("utf-8")) > 100_000:
        fail("README.md exceeded the 100 KiB profile budget")

    previous_index = -1
    for section in REQUIRED_SECTIONS:
        index = text.find(section)
        if index < 0:
            fail(f"required section missing: {section}")
        if index <= previous_index:
            fail(f"profile sections are out of order at: {section}")
        previous_index = index

    for placeholder in ("YOUR-", "TODO", "example.com"):
        if placeholder in text:
            fail(f"placeholder leaked into README: {placeholder}")

    if "```mermaid" in text:
        fail("live Mermaid should not return to the profile; use repository-owned SVG assets")

    if "prefers-color-scheme: dark" not in text or "prefers-color-scheme: light" not in text:
        fail("README must provide adaptive dark/light imagery")

    required_story = (
        "Systems Analyst / Technical Lead",
        "Industrial Engineer",
        "GIDAS",
        "AS-IS / TO-BE",
        "BPMN",
        "business ↔ technology",
        "QA/UAT",
        "English B2",
        "Repository portfolio roadmap — 2026",
        "pnpm 11.26.0",
        "Web-de-profesores",
        "Pint.ar_Ecommerce",
        "Meow Matrix",
        "App_Agenda_Medico",
        "Web_de_vinos",
        "Ecommerce_NestJS",
        "20/20 tests",
        "182071b3e8148196861ee2f38e99a1ebfd0e1294",
    )
    for contract in required_story:
        if contract not in text:
            fail(f"career/profile narrative lost required contract: {contract}")

    stale_story = (
        "The next ecommerce showcase is the paired",
        "The next general historical-modernization lane is now **`App_Agenda_Medico`**",
        "Three completed public modernization cases",
    )
    for stale in stale_story:
        if stale in text:
            fail(f"stale portfolio state leaked into README: {stale}")

    inflated_claims = (
        "SAP expert",
        "Dynamics expert",
        "certified project manager",
        "PMP certified",
    )
    for claim in inflated_claims:
        if claim.lower() in text.lower():
            fail(f"inflated/unverified career claim leaked into README: {claim}")

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


def validate_roadmap() -> None:
    if not ROADMAP.exists():
        fail("repository portfolio roadmap is missing")

    text = ROADMAP.read_text(encoding="utf-8")

    if len(text.encode("utf-8")) > 100_000:
        fail("repository portfolio roadmap exceeded the 100 KiB documentation budget")

    required_contracts = (
        "46 repositories",
        "## 5. Complete repository classification",
        "## 6. Recommended execution order",
        "TrackIt_Frontend",
        "Web-de-profesores",
        "Pint.ar_Ecommerce",
        "App_Agenda_Medico",
        "Web_de_vinos",
        "El_Nucleo_Web",
        "Security beats aesthetics",
        "One major legacy modernization lane at a time",
        "COMPLETED MODERNIZATIONS / REFERENCE",
        "NEXT GENERAL PORTFOLIO LANE",
        "Meow-Matrix---Frontend + MeowMatrix---Backend-2v",
        "PROVIDER-NEUTRAL RELEASE CARRIER COMPLETED",
        "811b223aeea0568d4eae0422fc5ad673e6b10c01",
        "182071b3e8148196861ee2f38e99a1ebfd0e1294",
        "390ac3591b089e0aefd6dc5f971c3e8d22e57794",
        "d6a335738eb0c9b4dc8751049faa3c21a97bad00",
        "c95ca4bad1b11f0c946a3c04764c63ca18e6d7c6",
        "cadedaa822e87f7a2131625d2acc197efb6e184f",
    )
    for contract in required_contracts:
        if contract not in text:
            fail(f"portfolio roadmap lost required contract: {contract}")

    stale_contracts = (
        "NEXT ECOMMERCE SHOWCASE",
        "Before implementation begins in the Meow Matrix lineage",
    )
    for stale in stale_contracts:
        if stale in text:
            fail(f"stale portfolio roadmap state leaked into current authority: {stale}")

    for placeholder in ("YOUR-", "TODO", "example.com"):
        if placeholder in text:
            fail(f"placeholder leaked into portfolio roadmap: {placeholder}")


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


def validate_profile_3d_workflow() -> None:
    if not PROFILE_3D_WORKFLOW.exists():
        fail("profile 3D refresh workflow is missing")

    text = PROFILE_3D_WORKFLOW.read_text(encoding="utf-8")
    for contract in (
        "git status --porcelain -- README.md profile-3d-contrib",
        "git add README.md profile-3d-contrib",
        "for attempt in 1 2 3; do",
        "git fetch --no-tags origin main",
        "git rebase origin/main",
        "git push origin HEAD:main",
        "main kept advancing while publishing generated profile assets; giving up safely after 3 attempts.",
    ):
        if contract not in text:
            fail(f"profile 3D workflow lost required publish safety contract: {contract}")

    if BARE_GIT_PUSH.search(text):
        fail("profile 3D workflow must not use a bare git push during generated asset publishing")


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
    validate_roadmap()
    validate_settings()
    validate_brand_script()
    validate_profile_3d_workflow()
    validate_svgs()
    print("profile validation passed")


if __name__ == "__main__":
    main()
