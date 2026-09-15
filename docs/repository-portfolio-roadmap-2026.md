# Repository portfolio roadmap — 2026

Snapshot date: 2026-09-15  
Last program update: 2026-09-15 — `Web-de-profesores` P1 completed and P2 selected  
Owner: `Enzopinotti`  
Scope: repositories accessible under the owner's GitHub installation at the time of this audit

## 1. Purpose

This document is the portfolio-level authority for deciding **what should be modernized, what should be preserved, what should be audited, and what should deliberately remain small or historical**.

The goal is not to make every repository look like the same 2026 stack. The goal is to make the portfolio tell a truthful engineering story:

```text
learning artifact -> explicit historical context
prototype         -> explicit prototype boundaries
client work       -> ownership / deployment / privacy review
active product    -> focused maintenance and production hardening
reference repo    -> reusable engineering baseline
empty/stub repo   -> archive/supersession decision, not invented code
```

The reusable method comes from the completed `El_Nucleo_Web` modernization and its standards issue #6: preserve history, define authority, make installs reproducible, test real risk, document truth boundaries, qualify deployments and keep rollback possible.

## 2. Inventory boundary

The current snapshot contains **46 repositories**.

This count is a snapshot, not a permanent account invariant. New repositories may be created after this document and should be classified when they become materially relevant.

Visibility is important because public repositories affect portfolio truth and possible secret exposure, while private repositories can contain active client/product work that should not automatically be made public.

## 3. Classification model

### A — Completed modernization / reference implementation

A repository already demonstrates the target method or has recently completed a controlled modernization. These repositories should receive focused maintenance, not another rewrite.

### B — Historical learning repository worth modernizing

A repository has meaningful historical/product behavior and can demonstrate engineering progression. Modernization should preserve the original learning context and improve reproducibility, safety, testing, accessibility and deployment without inventing present-day product claims.

### C — Academic / algorithmic artifact

The learning objective is the core value. Modernization should improve packaging, tests, typing, documentation and reproducibility without turning the exercise into an unrelated SaaS product.

### D — Product / full-stack lineage requiring a dedicated audit

The repository has enough backend/auth/data/infrastructure surface that it needs a security and architecture audit before framework upgrades. Related frontend/backend repositories should be evaluated as one product lineage where appropriate.

### E — Client / landing / delivery repository

The main questions are ownership, current deployment, privacy, integrations, content truth and maintainability. These repositories should not receive blanket rewrites merely to increase stack complexity.

### F — Empty, near-empty, superseded or experimental stub

Do not manufacture implementation to make these repositories appear mature. Determine whether the repository should be documented, linked to a successor, archived, kept private or deleted only after explicit ownership/history review.

### G — Active / current engineering system

These repositories are current products, operations tooling or portfolio infrastructure. They need normal product maintenance and targeted audits, not legacy modernization treatment.

## 4. Immediate cross-portfolio findings

### 4.1 `El_Nucleo_Web` is the completed reference case

The 2022 HTML/SCSS project is now a completed 2026 reconstruction with:

- historical root preserved;
- `modern/src` as current source authority;
- React 19 + Vite 8 + TypeScript 6;
- Node 24 + pnpm 11.26.0;
- frozen install and pnpm supply-chain policy;
- 30/30 permanent tests;
- accessibility / provenance / truth-boundary contracts;
- versioned Netlify deployment policy;
- public production smoke under enforced CSP;
- production authority at `https://el-nucleo-producciones.netlify.app/`.

Cutover merge: `c3342e111ba4d7bbe88f04407c0510bfe0fcd1da`.

This repository should now be treated as a reference implementation, not reopened as a generic modernization lane.

### 4.2 The profile repository is a portfolio authority and must stay synchronized

`Enzopinotti/Enzopinotti` is not just decorative README content. It is the public index that explains which repositories represent current engineering ability.

At the start of this audit its README was stale in two material ways:

- it still described El Núcleo as an in-progress Home/Nosotros reconstruction;
- it still cited pnpm 9.15.9 for El Núcleo even though the completed repository uses pnpm 11.26.0.

The profile should remain concise, while this document carries the full portfolio roadmap.

### 4.3 Security triage must outrank cosmetic modernization

`TrackIt_Frontend` currently contains a committed `.env` file in the public repository tree.

The file contents were deliberately **not** inspected or reproduced during this portfolio audit. The correct next action for that lineage is exposure review / credential rotation if applicable, followed by repository hygiene. Visual modernization comes later.

### 4.4 Generated/vendor artifacts exist in historical repositories

Examples found during discovery:

- `Web_de_vinos` versions `node_modules/` and uses `node-sass`;
- `App_Agenda_Medico` versions `__pycache__/`;
- `Proyecto_Backend` versions a large `kubectl.exe` binary and a warning log.

These are useful historical signals. They should normally be removed from current authority through explicit hygiene work, while Git history remains intact.

### 4.5 Not every separate repository is a separate product

Several names clearly form lineages or pairs and should be audited together before deciding their future:

- `Meow-Matrix---Frontend` + `MeowMatrix---Backend-2v`;
- `centuryLanding` + `centuryBackend`;
- `Antigal_Frontend_Enzo` + `AntigalBackend`;
- `TrackIt_Frontend` + `TrackIt_Backend`;
- `Landing_Branko` + private `Landing_Branko_CMS`;
- `portafolio-personal` + historical/experimental `Portfolio_Backend` must be checked for supersession rather than assumed to be one active system.

## 5. Complete repository classification

| Repository | Visibility | Class | Current interpretation | Recommended treatment | Priority |
| --- | --- | --- | --- | --- | --- |
| `El_Nucleo_Web` | Public | A | Completed historical reconstruction | Maintain; use as modernization reference | Done |
| `Web-de-profesores` | Public | A | Completed 2023 → 2026 teaching-workspace modernization with exact historical archive, local-data recovery and production-qualified Pages delivery | Maintain as fit-for-purpose modernization reference; do not reopen as a generic rewrite | Done |
| `Pint.ar_Ecommerce` | Public | B | 2023 React 18 / CRA / Firebase ecommerce learning project | Platform migration + Firebase/data/security audit while preserving course context | P2 |
| `App_Agenda_Medico` | Public | C | Python TAD/data-structure medical agenda exercise | Preserve academic purpose; add packaging, typing, tests, CLI quality and repo hygiene | P3 |
| `Web_de_vinos` | Public | B | HTML/SCSS learning site with `node-sass` and committed `node_modules` | Repository hygiene + modern Sass/tooling; avoid duplicating El Núcleo rewrite for appearance | P4 |
| `Proyecto_Backend` | Public | D | Express/Mongo/Auth/Swagger/tests/Docker/Kubernetes learning backend | Deep backend/security/runtime audit; remove repo artifacts; determine lineage with Meow backend | P5 |
| `Chat_En_Vivo` | Public | F | Near-empty/stub repository | Verify intent/successor; document or archive rather than invent implementation | Later |
| `GIUCT-SQL-v1` | Public | F | Empty/stub repository | Verify history; archive/supersede if appropriate | Later |
| `Plantilla-de-Proyecto` | Public | A | Current reusable Node/TypeScript/Fastify service starter | Maintain as reference; periodic compatibility/security audit only | Reference |
| `Ecommerce_NestJS` | Public | C/D | NestJS TypeScript ecommerce exercise with tests/config | Audit as backend learning artifact; modernize only after earlier lineage | P6 |
| `Meow-Matrix---Frontend` | Public | D | React 18 CRA frontend | Audit with Meow backend as one full-stack product lineage | P5 |
| `MeowMatrix---Backend-2v` | Public | D | Express/Mongo/Auth backend similar to Proyecto_Backend | Compare lineage/supersession first; then one consolidated hardening plan | P5 |
| `StarWars_App_NextJS` | Public | C/B | Next.js 14 + React 18 + i18n learning app | Framework-maintenance audit; preserve API/content-learning purpose | P7 |
| `Portfolio_Backend` | Public | F/C | Small NestJS-style backend scaffold | Determine whether superseded by `portafolio-personal`; avoid parallel fake maintenance | Later |
| `luciano-legnoverde` | Public | E | Client/person landing by naming/context | Ownership/deploy/content/privacy audit before technical changes | Client lane |
| `centuryLanding` | Public | E | React landing with server-related deployment files | Audit together with `centuryBackend` | Client lane |
| `centuryBackend` | Public | E/D | Small Node backend with uploads directory | Audit data/upload/security contract with `centuryLanding` | Client lane |
| `2024-UTN-GRUPO-2` | Public | C | Collaborative academic frontend/backend project | Preserve collaboration/history; improve docs/tests only with authorship context | Academic lane |
| `odoo-practice` | Public | F | Empty Odoo practice stub | Keep as practice marker or archive; do not manufacture an Odoo project | Later |
| `portafolio-personal` | Public | G | Current full-stack portfolio/product infrastructure | Active maintenance, production/security/performance audits only | Active |
| `AntigalBackend` | Public | F/E | Empty backend repository paired by name with Antigal frontend | Verify whether intentionally unused/superseded before archive | Client lane |
| `Vicky-Pellegrino-Landing` | Public | E | Public client landing | Deployment/content/privacy/accessibility audit, not blanket rewrite | Client lane |
| `Antigal_Frontend_Enzo` | Public | E | Client frontend under `antigal.client` | Audit with backend/history and ownership context | Client lane |
| `TrackIt_Backend` | Public | F/D | Empty backend repository | Verify intended backend/successor | Security lane |
| `TrackIt_Frontend` | Public | D | React 18 CRA product prototype; committed `.env` detected | **Security triage first**, then architecture/hygiene | P0 security |
| `ejercicioDjango` | Public | C | Small Django exercise | Preserve as learning artifact; packaging/tests/docs if retained | Later |
| `PortfolioAndreCoronel` | Public | E | Large portfolio/client repository | Ownership/media/deploy review before changes | Client lane |
| `marina_landing` | Private | E | Private landing/client work | Keep private; maintenance only with client/deployment need | Private client |
| `odontApp` | Private | G/E | Private application in healthcare/odontology domain | Keep private; security/privacy/data review before any publication | Private product |
| `losApuntes` | Public | F/C | Current tree contains only a tiny README despite large repository size/history | Inspect history/supersession before deciding whether to archive | Later |
| `diezy90-bot-presupuestos` | Private | G | Private automation/bot | Active/private maintenance according to real use | Private active |
| `trenAlSur` | Public | G/C | Modern Vite/TypeScript project with tests/docs/agent guidance | Focused current audit; not legacy rewrite | Current |
| `Podometro` | Private | G/C | Private application/prototype | Keep private; assess only when product work resumes | Private |
| `SolarCasares_Landing` | Public | E | Public landing | Client/deploy/content audit | Client lane |
| `C21dosil_Landing` | Public | E | Large public landing/media repository | Performance/media/deploy/ownership audit | Client lane |
| `Muelle85_Landing` | Public | E | Large public landing/media repository | Performance/media/deploy/ownership audit | Client lane |
| `Messina_Landing` | Public | E | Public landing/media repository | Client/deploy/content audit | Client lane |
| `Landing_Branko` | Public | E | Public client landing | Audit together with private CMS; preserve public/private boundary | Client lane |
| `Ecommerce_Alejandra` | Public | E/B | Public ecommerce project | Determine client vs learning ownership, then choose maintenance strategy | Discovery |
| `Enzopinotti` | Public | G | GitHub profile and portfolio index | Keep synchronized with proven repository state; host this roadmap | Continuous |
| `Bitora` | Public | A/G | Modern educational full-stack algorithms lab with CI/Docker/docs | Maintain as reference/current build | Reference |
| `Mora-Petraglia-Landing` | Public | E/G | Current portfolio/client landing with CMS/integrations context | Focused production/content audit only | Current client |
| `TOP` | Private | G | Active private SaaS/product engineering repository | Continue product roadmap; do not mix with legacy modernization | Active |
| `Landing_Branko_CMS` | Private | E/G | Private CMS paired with public Branko landing | Audit with landing; never expose private operational details by default | Private client |
| `Assetelier-Studio` | Private | G | Active private asset/product tooling | Normal product evolution | Active |
| `linkedin-content-ops` | Private | G | Active private content-operations tooling | Normal product evolution | Active |

## 6. Recommended execution order

### P0 — security triage before modernization

`TrackIt_Frontend`

Reason: a public committed `.env` is a potential exposure boundary. Determine whether it contains only non-secret public build variables or anything that must be rotated. Do not print secrets into issues, logs or documentation. Review Git history only as needed for exposure remediation.

This is intentionally a small security lane, not a full product rewrite.

### P1 — `Web-de-profesores` — COMPLETED

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

### P2 — `Pint.ar_Ecommerce`

This is the first substantial React/Firebase modernization candidate.

Primary questions:

- CRA → current build platform;
- Firebase configuration and rules/data contract;
- order/cart correctness;
- routing and loading/error states;
- dependency/runtime authority;
- testing and deployment;
- current Vercel endpoint validity;
- historical course claims vs any present-day product claims.

### P3 — `App_Agenda_Medico`

Use this repo to show that modernization does **not** always mean web UI.

A strong target would be:

- modern Python packaging;
- supported Python version contract;
- type hints;
- pytest unit tests for TAD invariants;
- deterministic CLI separation from domain logic;
- removal of generated caches from current authority;
- clear academic README and examples.

### P4 — `Web_de_vinos`

Focus on hygiene and build modernization:

- remove tracked vendor output from current authority;
- replace `node-sass` with supported Sass tooling;
- define runtime/package manager;
- preserve original HTML/SCSS design history;
- add minimal validation/CI;
- decide whether public deployment still has value.

Avoid another large React rewrite unless a product requirement appears.

### P5 — backend/full-stack lineage audit

Audit together before changing code:

- `Proyecto_Backend`;
- `MeowMatrix---Backend-2v`;
- `Meow-Matrix---Frontend`.

Questions:

- are the two backends ancestors/successors/copies?
- which repository contains the authoritative final product behavior?
- which auth/session flows are real vs course exercises?
- are secrets/configuration safely excluded?
- what tests genuinely pass?
- are Docker/Kubernetes assets operational or learning artifacts?
- can large committed binaries be removed from current authority?

Only after lineage is resolved should dependency/framework upgrades begin.

### P6/P7 — framework-specific learning repos

- `Ecommerce_NestJS`;
- `StarWars_App_NextJS`.

These should demonstrate framework maintenance, not speculative feature expansion.

## 7. Client repository strategy

Client/landing work should use a different Definition of Done from learning repositories.

For each client lane, first determine:

1. ownership and whether the client relationship/content is still public;
2. current production URL and provider;
3. whether forms, email, CMS or upload endpoints still operate;
4. whether personal/client data is present in Git history or runtime storage;
5. whether large media is intentional and optimized;
6. accessibility/responsive/SEO baseline;
7. whether the repo is portfolio evidence, operational production, or both;
8. rollback and current maintainer expectations.

Do not migrate a client landing to a new framework simply because an old framework is no longer fashionable.

## 8. Empty/stub strategy

Empty or near-empty repositories are not failures that need artificial code.

For each stub:

```text
identify purpose -> identify successor -> decide preserve / archive / private / delete
```

Deletion should be rare and explicit because Git history can still be useful evidence. Archiving plus a short README is often the better outcome when the repository has historical meaning.

## 9. Cross-portfolio standards to reuse

Each modernization/audit should evaluate the following, but adopt implementation only where relevant:

- historical baseline and rollback;
- source vs generated authority;
- runtime/package-manager authority;
- deterministic dependency install;
- supply-chain policy appropriate to the ecosystem;
- secrets/configuration hygiene;
- tests mapped to actual risk;
- lint/type/static analysis appropriate to the language;
- accessibility for user-facing surfaces;
- provenance for promoted historical/client media;
- privacy and data-collection boundaries;
- deployment/public-origin truth;
- security headers where a web host supports them;
- docs-as-code;
- post-merge verification for infrastructure/release changes;
- explicit non-adoptions to avoid stack inflation.

## 10. Portfolio-level rules

1. **Do not rewrite history to look more senior.** The progression is more valuable when the old limitations remain visible and contextualized.
2. **Do not use one stack everywhere.** React, Next, Nest, Docker and databases are choices, not maturity badges.
3. **Security beats aesthetics.** Potential secrets, credential collection and privacy issues are addressed before visual polish.
4. **Do not invent backends for prototypes.** If the historical product was local/demo-only, the modern version may remain a safe local demo.
5. **Do not invent current client relationships.** Public historical work must be labeled honestly.
6. **Do not expose private client/product material to improve the public portfolio.**
7. **Do not duplicate active products.** Resolve lineage/supersession before maintaining multiple copies.
8. **Keep the profile repository synchronized.** A completed project must not remain described as in-progress in the profile.
9. **One major legacy modernization lane at a time.** Small security triage can run separately when needed.
10. **Close each lane completely.** Code, CI, docs, production evidence and central roadmap all move together.

## 11. Current portfolio program state

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
```

## 12. Next decision gate

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
