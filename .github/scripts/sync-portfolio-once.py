from pathlib import Path
import re

roadmap_path = Path("docs/repository-portfolio-roadmap-2026.md")
readme_path = Path("README.md")
validator_path = Path(".github/scripts/validate-profile.py")

roadmap = roadmap_path.read_text(encoding="utf-8")
roadmap = roadmap.replace(
    "Snapshot date: 2026-09-15  \nOwner: `Enzopinotti`",
    "Snapshot date: 2026-09-15  \nLast program update: 2026-09-15 — `Web-de-profesores` P1 completed and P2 selected  \nOwner: `Enzopinotti`",
)
old_row = "| `Web-de-profesores` | Public | B | 2023 JavaScript teacher/student simulator with localStorage and JSON | Next full historical modernization; remove credential-like demo behavior from current authority | P1 |"
new_row = "| `Web-de-profesores` | Public | A | Completed 2023 → 2026 teaching-workspace modernization with exact historical archive, local-data recovery and production-qualified Pages delivery | Maintain as fit-for-purpose modernization reference; do not reopen as a generic rewrite | Done |"
if old_row not in roadmap:
    raise SystemExit("expected Web-de-profesores classification row not found")
roadmap = roadmap.replace(old_row, new_row)

p1_pattern = re.compile(
    r"### P1 — `Web-de-profesores`\n.*?(?=### P2 — `Pint\.ar_Ecommerce`)",
    re.S,
)
p1_replacement = """### P1 — `Web-de-profesores` — COMPLETED

This lane is complete and now acts as a second modernization reference with a deliberately different architecture from El Núcleo.

Final evidence:

- historical baseline: `d6a38f5795569131ff4cd0db63640aff8dc09007`;
- exact navigable archive under `historical/2023/`, with 14/14 historical files verified against their original Git blob SHA-1;
- maintained 2026 source under `modern/` using Node 24, pnpm 11.26.0, Vite 8 and TypeScript 6 without React or a backend;
- no current password collection or fake authentication; legacy `Usuarios` storage is purged by the maintained app;
- versioned local persistence, explicit recovery, backup/restore, stable-ID editing, undo, neutral summaries and sorting;
- 5 test files / 41 tests / 41 passed plus lint, typecheck, docs, build and Pages-mirror integrity gates;
- production Pages authority made deterministic even while GitHub's legacy branch publisher remains enabled;
- final main merge: `46bcd66f1a25f5c0879f40dfb924011959368225`;
- final quality run `35016810900`: success;
- custom Pages run `35016810998`: success;
- legacy Pages run `35016808192`: success;
- real-Chrome production smoke `35001016659`: success after validating recovery and 360 / 768 / 1440 responsive contracts.

The important portfolio signal is not the toolchain itself. This repository demonstrates that maturity can mean **choosing a smaller architecture, removing false security semantics, making destructive operations recoverable and turning deployment ambiguity into a tested contract**.

"""
roadmap, count = p1_pattern.subn(p1_replacement, roadmap, count=1)
if count != 1:
    raise SystemExit("P1 section replacement failed")

state_pattern = re.compile(r"## 11\. Current portfolio program state\n\n```text\n.*?```", re.S)
state_replacement = """## 11. Current portfolio program state

```text
COMPLETED MODERNIZATIONS / REFERENCE
El_Nucleo_Web
Web-de-profesores

IMMEDIATE SECURITY TRIAGE
TrackIt_Frontend

NEXT FULL MODERNIZATION
Pint.ar_Ecommerce

FOLLOWING HISTORICAL LANES
App_Agenda_Medico
Web_de_vinos
backend/full-stack lineage
Ecommerce_NestJS
StarWars_App_NextJS

CURRENT / REFERENCE — MAINTAIN, DON'T REWRITE
Plantilla-de-Proyecto
Bitora
portafolio-personal
trenAlSur
TOP
Assetelier-Studio
linkedin-content-ops

CLIENT / DELIVERY — AUDIT BY OWNERSHIP + PRODUCTION NEED
client landing / ecommerce repositories and their paired private services

STUBS — EXPLICIT PRESERVE / ARCHIVE / SUPERSEDE DECISION
empty and near-empty repositories
```"""
roadmap, count = state_pattern.subn(state_replacement, roadmap, count=1)
if count != 1:
    raise SystemExit("current program state replacement failed")

gate_pattern = re.compile(r"## 12\. Next decision gate\n.*\Z", re.S)
gate_replacement = """## 12. Next decision gate

Before implementation begins in `Pint.ar_Ecommerce`, perform a repository-specific audit before choosing migrations or upgrading Firebase/React:

- identify the exact historical baseline, commit chronology and course/project context;
- inventory CRA/React dependencies, routes, cart/order state, Firebase integration, assets and deployment files;
- classify Firebase configuration separately from secrets and never print sensitive values into issues/logs;
- determine what Firestore collections/documents/rules the frontend actually assumes, without inventing missing backend behavior;
- verify cart totals, quantities, checkout/order creation and error/loading states from the existing implementation;
- probe the current public deployment and distinguish historical URLs from maintained authority;
- review accessibility, responsive behavior and current media cost;
- choose the smallest justified migration path only after the runtime/data contracts are understood;
- create the repository umbrella issue from evidence, not from a framework-upgrade checklist;
- preserve the historical learning version and update this roadmap when P2 moves planned → active → completed.

`TrackIt_Frontend` remains a separate P0 security triage and must not be folded into this P2 implementation lane.
"""
roadmap, count = gate_pattern.subn(gate_replacement, roadmap, count=1)
if count != 1:
    raise SystemExit("next decision gate replacement failed")
roadmap_path.write_text(roadmap, encoding="utf-8")

readme = readme_path.read_text(encoding="utf-8")
old_mission = "A completed public example is **[El_Nucleo_Web](https://github.com/Enzopinotti/El_Nucleo_Web)**: a 2022 HTML/SCSS learning project rebuilt into a modern, tested application **without deleting its history or pretending historical content is current**. The 2026 reconstruction is now deployed and publicly smoke-tested under its production security policy, while the original source remains auditable in Git.\n\nI am applying the same evidence-first method across older repositories without forcing the same stack onto every project. The current portfolio-wide plan is versioned in **[Repository portfolio roadmap — 2026](./docs/repository-portfolio-roadmap-2026.md)**."
new_mission = "Two completed public modernization cases now show the method from different angles. **[El_Nucleo_Web](https://github.com/Enzopinotti/El_Nucleo_Web)** rebuilt a 2022 HTML/SCSS project into a production-qualified React application while preserving historical provenance. **[Web-de-profesores](https://github.com/Enzopinotti/Web-de-profesores)** took the opposite architectural lesson: a 2023 JavaScript/localStorage simulator matured into a safe, tested local teaching workspace with Vite + TypeScript **without adding React, backend authentication or a database that the product did not need**.\n\nBoth preserve their historical baselines, qualify real deployments and keep rollback evidence. I am applying the same evidence-first method across older repositories without forcing the same stack onto every project. The next full lane is `Pint.ar_Ecommerce`, tracked in **[Repository portfolio roadmap — 2026](./docs/repository-portfolio-roadmap-2026.md)**."
if old_mission not in readme:
    raise SystemExit("README current-mission paragraph not found")
readme = readme.replace(old_mission, new_mission)

marker = "### 🌐 [Portfolio — enzopinotti.dev](https://enzopinotti.dev)"
modderhouse = """### 🎓 [Modderhouse — 2023 → 2026 teaching workspace](https://github.com/Enzopinotti/Web-de-profesores)
**Fit-for-purpose modernization + recoverable local data + browser-qualified delivery**

A completed JavaScript-learning project that now preserves its exact 2023 baseline while the maintained 2026 workspace uses **Node.js 24, pnpm 11.26.0, Vite 8 and TypeScript 6** with no framework inflation. The current product removes fake password/auth semantics, adds versioned storage recovery, backup/restore, stable-ID editing, undo and neutral classroom summaries, and finishes with **41/41 tests** plus a real Chrome production smoke at 360 / 768 / 1440.

The deployment itself became part of the engineering story: when GitHub's legacy Pages publisher competed with the custom workflow, the repository was changed so both publication paths resolve to a verified equivalent 2026 artifact while the original 14-file project remains byte-for-byte auditable under `historical/2023/`.

"""
if marker not in readme:
    raise SystemExit("README selected-build insertion marker not found")
readme = readme.replace(marker, modderhouse + marker, 1)
readme_path.write_text(readme, encoding="utf-8")

validator = validator_path.read_text(encoding="utf-8")
needle = '        "pnpm 11.26.0",\n'
if needle not in validator:
    raise SystemExit("README validator insertion point not found")
validator = validator.replace(
    needle,
    needle + '        "Web-de-profesores",\n        "Pint.ar_Ecommerce",\n',
    1,
)
needle = '        "One major legacy modernization lane at a time",\n'
if needle not in validator:
    raise SystemExit("roadmap validator insertion point not found")
validator = validator.replace(
    needle,
    needle + '        "COMPLETED MODERNIZATIONS / REFERENCE",\n        "NEXT FULL MODERNIZATION",\n',
    1,
)
validator_path.write_text(validator, encoding="utf-8")
