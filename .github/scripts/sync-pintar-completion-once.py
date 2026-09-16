#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
ROADMAP = ROOT / "docs" / "repository-portfolio-roadmap-2026.md"
VALIDATOR = ROOT / ".github" / "scripts" / "validate-profile.py"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


def replace_section(text: str, start: str, end: str, body: str, label: str) -> str:
    start_index = text.find(start)
    if start_index < 0:
        raise SystemExit(f"{label}: start marker missing")
    end_index = text.find(end, start_index + len(start))
    if end_index < 0:
        raise SystemExit(f"{label}: end marker missing")
    return text[:start_index] + body.rstrip() + "\n\n" + text[end_index:]


readme = README.read_text(encoding="utf-8")
readme = replace_once(
    readme,
    "Two completed public modernization cases now show the method from different angles. **[El_Nucleo_Web](https://github.com/Enzopinotti/El_Nucleo_Web)** rebuilt a 2022 HTML/SCSS project into a production-qualified React application while preserving historical provenance. **[Web-de-profesores](https://github.com/Enzopinotti/Web-de-profesores)** took the opposite architectural lesson: a 2023 JavaScript/localStorage simulator matured into a safe, tested local teaching workspace with Vite + TypeScript **without adding React, backend authentication or a database that the product did not need**.\n\nBoth preserve their historical baselines, qualify real deployments and keep rollback evidence. I am applying the same evidence-first method across older repositories without forcing the same stack onto every project. The next full lane is `Pint.ar_Ecommerce`, tracked in **[Repository portfolio roadmap — 2026](./docs/repository-portfolio-roadmap-2026.md)**.",
    "Three completed public modernization cases now show the method from different angles. **[El_Nucleo_Web](https://github.com/Enzopinotti/El_Nucleo_Web)** rebuilt a 2022 HTML/SCSS project into a production-qualified React application while preserving historical provenance. **[Web-de-profesores](https://github.com/Enzopinotti/Web-de-profesores)** took the opposite architectural lesson: a 2023 JavaScript/localStorage simulator matured into a safe, tested local teaching workspace with Vite + TypeScript **without adding React, backend authentication or a database that the product did not need**. **[Pint.ar_Ecommerce](https://github.com/Enzopinotti/Pint.ar_Ecommerce)** keeps React because the ecommerce problem justifies it, but replaces browser-trusted Firebase order semantics with an explicit demo boundary, typed domain contracts, hardened Docker delivery and production-qualified Pages.\n\nAll three preserve their historical baselines, qualify real deployments and keep rollback evidence. I am applying the same evidence-first method across older repositories without forcing the same stack onto every project. The next ecommerce showcase is the paired **Meow Matrix frontend/backend** lineage, while `App_Agenda_Medico` remains the following general historical-modernization lane; both are tracked in **[Repository portfolio roadmap — 2026](./docs/repository-portfolio-roadmap-2026.md)**.",
    "README mission modernization story",
)

pintar_build = """### 🛒 [Pint.ar — 2023 → 2026 storefront](https://github.com/Enzopinotti/Pint.ar_Ecommerce)
**Ecommerce product engineering + typed domain contracts + hardened delivery**

A completed React/Firebase learning ecommerce that now preserves its exact 2023 Coderhouse + UTN context while the maintained `modern/` authority uses **Node.js 24, pnpm 11.26.0, React 19.3, Vite 8, TypeScript 6 and Sass**. The storefront adds deterministic search/filter/sort, immutable cart behavior, versioned recovery, a truthful guest checkout demo and **20/20 tests** without inventing payments, authentication or a backend the product does not need.

Delivery is part of the case: a multi-stage Docker image serves through non-root Nginx with read-only/capability-reduced runtime controls, while GitHub Pages uses an explicit repository-subpath build. A real race between the custom Pages workflow and GitHub's legacy branch publisher was neutralized with a **byte-for-byte verified generated mirror**, and the final public workflow runs an Internet-facing Chrome smoke over the home, assets, metadata and direct `/carrito` navigation. Production: **[enzopinotti.github.io/Pint.ar_Ecommerce](https://enzopinotti.github.io/Pint.ar_Ecommerce/)**.

"""
readme = replace_once(
    readme,
    "### 🌐 [Portfolio — enzopinotti.dev](https://enzopinotti.dev)",
    pintar_build + "### 🌐 [Portfolio — enzopinotti.dev](https://enzopinotti.dev)",
    "README Pint.ar selected build",
)
README.write_text(readme, encoding="utf-8")

roadmap = ROADMAP.read_text(encoding="utf-8")
roadmap = replace_once(
    roadmap,
    "Last program update: 2026-09-15 — `Web-de-profesores` P1 completed and P2 selected",
    "Last program update: 2026-09-15 — `Pint.ar_Ecommerce` P2 completed; Meow Matrix selected as next ecommerce showcase",
    "roadmap program update",
)
roadmap = replace_once(
    roadmap,
    "| `Pint.ar_Ecommerce` | Public | B | 2023 React 18 / CRA / Firebase ecommerce learning project | Platform migration + Firebase/data/security audit while preserving course context | P2 |",
    "| `Pint.ar_Ecommerce` | Public | A | Completed 2023 → 2026 React ecommerce modernization with typed domain contracts, hardened Docker runtime and production-qualified Pages | Maintain as storefront/product-engineering reference; historical CRA/Firebase source remains auditable | Done |",
    "roadmap Pint.ar classification",
)
roadmap = replace_once(
    roadmap,
    "| `Meow-Matrix---Frontend` | Public | D | React 18 CRA frontend | Audit with Meow backend as one full-stack product lineage | P5 |",
    "| `Meow-Matrix---Frontend` | Public | D | React 18 CRA ecommerce frontend paired with Meow backend | Audit with backend as the next full-stack ecommerce showcase; preserve historical course/product lineage | Next ecommerce |",
    "roadmap Meow frontend classification",
)
roadmap = replace_once(
    roadmap,
    "| `MeowMatrix---Backend-2v` | Public | D | Express/Mongo/Auth backend similar to Proyecto_Backend | Compare lineage/supersession first; then one consolidated hardening plan | P5 |",
    "| `MeowMatrix---Backend-2v` | Public | D | Express/Mongo/Auth ecommerce backend paired with Meow frontend | Deep security/runtime/data audit, then one consolidated full-stack modernization plan | Next ecommerce |",
    "roadmap Meow backend classification",
)

p2_section = """### P2 — `Pint.ar_Ecommerce` — COMPLETED

Pint.ar is complete and now acts as the portfolio's storefront/product-engineering ecommerce reference while keeping its 2023 learning context explicit.

Final evidence:

- exact historical baseline: `3224d89c0c512b3509cea25f1c49a119d371e338`;
- maintained authority: `modern/`;
- final main: `811b223aeea0568d4eae0422fc5ad673e6b10c01`;
- Node 24 + pnpm 11.26.0 + React 19.3 + React Router 7.18 + Vite 8.2 + TypeScript 6 strict + Sass 1.104;
- typed catalogue/cart/checkout boundaries, deterministic search/filter/sort and truthful local demo-order semantics;
- no runtime dependency on the historical Firebase project and no unsupported payment/email/auth claims;
- 6 test files / 20 tests / 20 passed;
- multi-stage Docker Node → Nginx runtime qualified as non-root, read-only, capability-dropped and `no-new-privileges`;
- public authority: `https://enzopinotti.github.io/Pint.ar_Ecommerce/`;
- a real custom-vs-branch Pages publication race was reproduced, then neutralized with a repository-root compatibility mirror verified byte-for-byte against the maintained Pages artifact;
- final permanent quality run `35049775048`: success;
- final custom Pages run `35049775023`: build + deploy + public-smoke success;
- final dynamic branch/Jekyll Pages run `35049772400`: success;
- public smoke verifies the live HTML/canonical/assets/robots/sitemap and direct `/carrito` navigation in Chrome.

The portfolio signal is deliberately different from Web-de-profesores: here React, state and Docker are justified by the ecommerce workflow, while backend/auth/payment infrastructure is still omitted because the storefront demo does not need to pretend to be a commercial transaction platform.
"""
roadmap = replace_section(
    roadmap,
    "### P2 — `Pint.ar_Ecommerce`",
    "### P3 — `App_Agenda_Medico`",
    p2_section,
    "roadmap P2 section",
)

roadmap = replace_once(
    roadmap,
    "COMPLETED MODERNIZATIONS / REFERENCE\nEl_Nucleo_Web\nWeb-de-profesores\n\nIMMEDIATE SECURITY TRIAGE\nTrackIt_Frontend\n\nNEXT FULL MODERNIZATION\nPint.ar_Ecommerce\n\nFOLLOWING HISTORICAL LANES\nApp_Agenda_Medico\nWeb_de_vinos",
    "COMPLETED MODERNIZATIONS / REFERENCE\nEl_Nucleo_Web\nWeb-de-profesores\nPint.ar_Ecommerce\n\nIMMEDIATE SECURITY TRIAGE\nTrackIt_Frontend\n\nNEXT ECOMMERCE SHOWCASE\nMeow-Matrix---Frontend + MeowMatrix---Backend-2v\n\nFOLLOWING GENERAL PORTFOLIO LANE\nApp_Agenda_Medico\n\nFOLLOWING HISTORICAL LANES\nWeb_de_vinos",
    "roadmap program state",
)

next_gate = """## 12. Next decision gate

Before implementation begins in the Meow Matrix lineage, perform a paired frontend/backend audit and decide architecture from evidence rather than copying TOP wholesale:

- identify the exact historical baseline and chronology of both `Meow-Matrix---Frontend` and `MeowMatrix---Backend-2v`;
- establish whether `Proyecto_Backend` is an ancestor, sibling or superseded backend before moving code between repositories;
- inventory frontend routes, catalogue/cart/checkout/auth state, API assumptions, environment variables, assets, tests and deployment files;
- inventory backend routes/controllers/models, Mongo/Mongoose contracts, sessions/JWT/OAuth, password handling, mail/uploads, Swagger/tests and runtime configuration;
- inspect Docker/Kubernetes history and remove current-authority vendor/binary artifacts such as committed `kubectl.exe` without rewriting Git history;
- classify every environment/config value without reproducing secrets or credentials in issues/logs/docs;
- determine which authentication/session flows are actually safe and which are only historical learning implementations;
- map the real frontend ↔ backend API contract, error/loading states and checkout/order ownership before framework upgrades;
- choose the smallest justified 2026 full-stack architecture, borrowing TOP practices for typing, boundaries, CI, Docker, security and documentation without importing multi-tenant SaaS complexity;
- create or update the Meow Matrix umbrella modernization issue from evidence before implementation;
- keep `App_Agenda_Medico` as the following general portfolio lane once the ecommerce pair is closed.

The target distinction is explicit: **Pint.ar demonstrates a mature storefront; Meow Matrix should demonstrate a mature full-stack ecommerce system**. The two repositories should complement each other rather than converge into the same architecture.
"""
roadmap = replace_section(
    roadmap,
    "## 12. Next decision gate",
    "## 13.",
    next_gate,
    "roadmap next decision gate",
)
ROADMAP.write_text(roadmap, encoding="utf-8")

validator = VALIDATOR.read_text(encoding="utf-8")
validator = replace_once(
    validator,
    '        "Pint.ar_Ecommerce",\n',
    '        "Pint.ar_Ecommerce",\n        "Meow Matrix",\n        "20/20 tests",\n',
    "validator README story",
)
validator = replace_once(
    validator,
    '        "NEXT FULL MODERNIZATION",\n',
    '        "NEXT ECOMMERCE SHOWCASE",\n        "Meow-Matrix---Frontend + MeowMatrix---Backend-2v",\n        "811b223aeea0568d4eae0422fc5ad673e6b10c01",\n',
    "validator roadmap state",
)
VALIDATOR.write_text(validator, encoding="utf-8")

print("Pint.ar completion and Meow Matrix next-lane state synchronized")
