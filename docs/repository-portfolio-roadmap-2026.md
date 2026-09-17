# Repository portfolio roadmap — 2026

Snapshot date: 2026-09-17  
Last program update: 2026-09-17 — Meow Matrix provider-neutral B7 carrier completed; `App_Agenda_Medico` selected as next general legacy lane  
Owner: `Enzopinotti`  
Scope: repositories accessible under the owner's GitHub installation at this audit point

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

The reusable method is now demonstrated by several different projects: preserve history, define authority, make installs reproducible, test real risk, document truth boundaries, qualify deployments/releases where applicable and keep rollback possible.

## 2. Inventory boundary

The current snapshot contains **46 repositories** accessible under `Enzopinotti`.

This count is a snapshot, not a permanent account invariant. Visibility matters: public repositories affect portfolio truth and possible secret exposure, while private repositories can contain active product/client material that must not be made public merely to improve the portfolio.

The modernization program therefore distinguishes four different actions:

1. **modernize** historical work where engineering progression is valuable;
2. **maintain** current/reference projects without rewriting them;
3. **audit** client/product repositories according to ownership, privacy and production need;
4. **preserve/archive/supersede** empty or obsolete stubs rather than inventing code.

## 3. Classification model

### A — Completed modernization / reference implementation

Controlled modernization is complete. These repositories should receive focused maintenance, not another generic rewrite.

### B — Historical learning repository worth modernizing

Meaningful historical/product behavior can demonstrate progression. Preserve the original context and improve reproducibility, safety, testing, accessibility and deployment where relevant.

### C — Academic / algorithmic artifact

The exercise itself is the value. Improve packaging, tests, typing and documentation without turning it into unrelated SaaS.

### D — Product / full-stack lineage requiring dedicated architecture/security treatment

Enough auth/data/infrastructure surface exists that changes must be evidence-led and related repositories may need to be treated as one lineage.

### E — Client / landing / delivery repository

Ownership, current deployment, privacy, integrations, content truth and maintainability matter more than framework novelty.

### F — Empty, near-empty, superseded or experimental stub

Do not manufacture implementation. Determine successor/history and preserve, archive, privatize or remove only with explicit reasoning.

### G — Active / current engineering system

Current product, tooling or portfolio infrastructure. Apply normal product evolution rather than legacy-modernization treatment.

## 4. Program findings and decisions

### 4.1 Completed public modernization references

The completed reference set now covers different architectural lessons:

- `El_Nucleo_Web` — historical HTML/SCSS → production-qualified React/Vite/TypeScript reconstruction with provenance and rollback;
- `Web-de-profesores` — JavaScript/localStorage learning app → safer Vite/TypeScript workspace **without** unnecessary React/backend/database complexity;
- `Pint.ar_Ecommerce` — React/Firebase learning storefront → typed ecommerce demo with honest trust boundaries, hardened Docker and qualified Pages delivery;
- `Meow-Matrix---Frontend` + `MeowMatrix---Backend-2v` — full-stack ecommerce lineage brought through backend-owned auth, Mongo persistence, transactional/idempotent commerce, private files, durable side effects, Docker/recovery qualification and immutable no-rebuild registry-promotion rehearsal.

Meow Matrix is different from the first three: **the provider-neutral engineering carrier is complete through B7, while the final production cutover remains external-provider work**. It must not be described as publicly deployed until real registry/provider credentials, production services, deploy-by-digest and public qualification exist.

Current Meow authorities:

- backend `main`: `182071b3e8148196861ee2f38e99a1ebfd0e1294`;
- frontend pin: `9d64c48d2324703cb594acad8e1bb0c9a3d6191c`;
- backend post-merge quality: `35224512304` success;
- backend full-stack/release-chain run: `35224512258` success;
- backend recovery rehearsal: `35224512305` success;
- retained release bundle and registry-rehearsal artifacts were published from that full-stack run.

### 4.2 The profile repository is an authority, not decoration

`Enzopinotti/Enzopinotti` must move with proven repository state. A project cannot remain described as “next” after it has already been integrated and qualified.

The profile should stay selective; this roadmap carries the full inventory and sequencing.

### 4.3 Security beats aesthetics

`TrackIt_Frontend` entered P0 because a public root `.env` was tracked. The maintained tree hygiene is now corrected by PR #2 / merge `185d6a99239349566421b45483ff57b79d08e3b8`:

- root `.env` removed from current authority;
- `.env` files ignored;
- value-free `.env.example` retained;
- README now documents that `REACT_APP_*` variables are browser-public.

This does **not** prove historical values were revoked/rotated. The issue remains open only for that external/historical determination.

### 4.4 Repository presentation is part of portfolio hygiene

Several older repositories contained useful code but presented only framework starter text or no README. A documentation-only pass corrected that without pretending the code itself had been modernized:

- `Web_de_vinos` — first project-specific README merged at `c6e6add18cf8bd081689d8b3403f1e835500400c`;
- `Ecommerce_NestJS` — Nest starter README replaced at `d3313889bf6a774e5cddf2b34685d789c9eecf00`;
- `StarWars_App_NextJS` — create-next-app README replaced at `95a8372019faab3306ef1ddd87467959526c37ec`;
- `Proyecto_Backend` — historical Meow/ecommerce lineage clarified at `089e133b47a40a323be94492d1c9077134e38bfb`.

These merges are **documentation/hygiene**, not completion of their future code-maintenance lanes.

### 4.5 Not every separate repository is a separate product

Known pairs/lineages continue to be treated together where appropriate:

- `Meow-Matrix---Frontend` + `MeowMatrix---Backend-2v`; historical context also includes `Proyecto_Backend`;
- `centuryLanding` + `centuryBackend`;
- `Antigal_Frontend_Enzo` + `AntigalBackend`;
- `TrackIt_Frontend` + `TrackIt_Backend`;
- `Landing_Branko` + private `Landing_Branko_CMS`;
- `portafolio-personal` + historical/experimental `Portfolio_Backend` require supersession review rather than assumed parallel maintenance.

## 5. Complete repository classification

| Repository | Visibility | Class | Current interpretation | Treatment / status |
| --- | --- | --- | --- | --- |
| `El_Nucleo_Web` | Public | A | Completed 2022 → 2026 reconstruction | Maintain as reference |
| `Web-de-profesores` | Public | A | Completed 2023 → 2026 teaching-workspace modernization | Maintain as fit-for-purpose reference |
| `Pint.ar_Ecommerce` | Public | A | Completed storefront modernization | Maintain as ecommerce frontend reference |
| `App_Agenda_Medico` | Public | C/B | 2023 Python TAD/data-structure medical agenda | **Next active general lane**: preserve baseline, typing/tests/CI/hygiene |
| `Web_de_vinos` | Public | B | Historical HTML/SCSS learning site; README now contextualized | Following lane: Sass/build/repo hygiene, no framework inflation |
| `Proyecto_Backend` | Public | D/B | Historical Express/Mongo ecommerce lineage | Lineage resolved toward Meow; preserve/audit rather than duplicate |
| `Chat_En_Vivo` | Public | F | Near-empty/stub | Verify successor; document/archive rather than invent |
| `GIUCT-SQL-v1` | Public | F | Empty/stub | Preserve/archive decision |
| `Plantilla-de-Proyecto` | Public | A/G | Reusable Node/TS/Fastify starter | Maintain/reference |
| `Ecommerce_NestJS` | Public | C/D | NestJS ecommerce learning backend; README contextualized | Future framework-specific maintenance |
| `Meow-Matrix---Frontend` | Public | A/D | Maintained frontend authority for Meow Matrix | B7 engineering carrier complete; provider cutover external |
| `MeowMatrix---Backend-2v` | Public | A/D | Maintained backend/release authority for Meow Matrix | B7 engineering carrier complete; provider cutover external |
| `StarWars_App_NextJS` | Public | C/B | Next.js 14 learning app; README contextualized | Future framework-maintenance lane |
| `Portfolio_Backend` | Public | F/C | Small backend scaffold | Determine supersession vs `portafolio-personal` |
| `luciano-legnoverde` | Public | E | Client/person landing | Ownership/deploy/content/privacy audit only |
| `centuryLanding` | Public | E | Client landing | Audit with `centuryBackend` |
| `centuryBackend` | Public | E/D | Small backend/upload surface | Audit with landing, focus data/upload security |
| `2024-UTN-GRUPO-2` | Public | C | Collaborative academic project | Preserve authorship; docs/tests only with context |
| `odoo-practice` | Public | F | Empty practice stub | Keep/archive; do not manufacture project |
| `portafolio-personal` | Public | G | Current portfolio/product infrastructure | Active maintenance only |
| `AntigalBackend` | Public | F/E | Empty paired backend | Verify intentional supersession |
| `Vicky-Pellegrino-Landing` | Public | E | Client landing | Production/content/accessibility audit only |
| `Antigal_Frontend_Enzo` | Public | E | Client frontend | Audit with paired history/ownership |
| `TrackIt_Backend` | Public | F/D | Empty backend repository | Determine intended successor/authority |
| `TrackIt_Frontend` | Public | D/B | React 18 CRA prototype | Current-tree security hygiene done; historical secret review still open |
| `ejercicioDjango` | Public | C | Small Django exercise | Preserve; packaging/tests/docs if retained |
| `PortfolioAndreCoronel` | Public | E | Large portfolio/client repository | Ownership/media/deploy audit before changes |
| `marina_landing` | Private | E | Private landing/client work | Keep private; maintenance by real need |
| `odontApp` | Private | G/E | Private healthcare/odontology app | Security/privacy/data review; no public exposure |
| `losApuntes` | Public | F/C | Tiny current tree with larger history | Inspect history/supersession first |
| `diezy90-bot-presupuestos` | Private | G | Private automation/bot | Active/private maintenance |
| `trenAlSur` | Public | G/C | Current Vite/TS project with tests/docs | Focused current audit; no legacy rewrite |
| `Podometro` | Private | G/C | Private app/prototype | Assess when product work resumes |
| `SolarCasares_Landing` | Public | E | Public landing | Client/deploy/content audit |
| `C21dosil_Landing` | Public | E | Large public landing/media repo | Performance/media/deploy/ownership audit |
| `Muelle85_Landing` | Public | E | Public landing/media repo | Performance/media/deploy/ownership audit |
| `Messina_Landing` | Public | E | Public landing/media repo | Client/deploy/content audit |
| `Landing_Branko` | Public | E | Public client landing | Audit with private CMS; preserve boundary |
| `Ecommerce_Alejandra` | Public | E/B | Public ecommerce project | Determine client vs learning ownership first |
| `Enzopinotti` | Public | G | Profile/portfolio index + roadmap | Continuous synchronization authority |
| `Bitora` | Public | A/G | Modern educational algorithms lab | Maintain/reference |
| `Mora-Petraglia-Landing` | Public | E/G | Current client/portfolio landing | Focused production/content maintenance |
| `TOP` | Private | G | Active private SaaS/product | Product roadmap; never mix with legacy lane |
| `Landing_Branko_CMS` | Private | E/G | Private CMS paired with public landing | Keep operational details private |
| `Assetelier-Studio` | Private | G | Active private product/tooling | Normal product evolution |
| `linkedin-content-ops` | Private | G | Active private content tooling | Normal product evolution |

## 6. Recommended execution order

### P0 — `TrackIt_Frontend` security triage — CURRENT TREE FIXED / EXTERNAL REVIEW OPEN

The maintained tree is now hygienic after PR #2. Remaining work is only to determine whether any historically committed value represented a privileged live credential and, if so, verify rotation/revocation outside the public repository. Do not reproduce old values in issues/logs/docs.

A CRA→Vite migration or product redesign is a **separate future decision** and must not be used to hide this security boundary.

### P1 — `Web-de-profesores` — COMPLETED

Historical baseline preserved, maintained Vite/TypeScript authority, 41/41 tests, recovery/backup behavior and qualified Pages publishing. Final `main`: `46bcd66f1a25f5c0879f40dfb924011959368225`.

### P2 — `Pint.ar_Ecommerce` — COMPLETED

Historical CRA/Firebase context remains auditable; maintained React/Vite/TypeScript storefront has typed demo-order boundaries, **20/20 tests**, hardened Docker and qualified Pages deployment. Final `main`: `811b223aeea0568d4eae0422fc5ad673e6b10c01`.

### Full-stack ecommerce showcase — Meow Matrix — PROVIDER-NEUTRAL RELEASE CARRIER COMPLETED

The paired `Meow-Matrix---Frontend + MeowMatrix---Backend-2v` lane has completed the engineering work that can be verified without inventing production infrastructure.

Completed scope includes:

- Node/TypeScript modernization and typed `/api/v1` contracts;
- backend-owned opaque sessions and password recovery;
- Mongo identity/catalog/cart/order persistence;
- transactional/idempotent checkout and stock invariants;
- private upload authorization/lifecycle;
- durable outbox/retry delivery;
- full-stack Compose with replica-set Mongo and dev SMTP;
- restart persistence and target-data preflight;
- recovery/restore rehearsal;
- immutable release evidence and retained API/web image bundle;
- isolated registry rehearsal proving **no rebuild**, pull-by-digest, exact image-ID preservation and hardened smoke;
- cutover manifest v3 binding bundle → promotion evidence → registry digest → deploy/public qualification.

External B7 cutover still requires real provider choices and credentials. Do not simulate those merely to mark a checkbox green.

### P3 — `App_Agenda_Medico` — NEXT GENERAL PORTFOLIO LANE

This is the next major legacy implementation lane.

Historical truth:

- 2023 collaborative Python project;
- TADs for Paciente, Cita, Cola and Agenda;
- interactive menu/application code;
- list-based data structures and a committed `__pycache__/`;
- lower-case `readme.md` is primarily a long TAD specification rather than a project landing page.

Modernization goals:

1. preserve the exact 2023 baseline and collaborator authorship;
2. make the maintained authority explicit instead of silently rewriting original modules;
3. remove generated Python cache artifacts from current authority;
4. add modern typed Python domain structures without database/web/SaaS invention;
5. fix behavior only with tests — including the historical queue implementation that currently removes from the end (`pop()`) rather than FIFO;
6. add deterministic tests and GitHub Actions;
7. turn the root README into useful project/history/run documentation while retaining the original TAD specification as historical documentation;
8. finish with a clear completion SHA and central-profile synchronization.

### P4 — `Web_de_vinos` — FOLLOWING HISTORICAL LANE

The README/context pass is already done. The dedicated code lane should remove committed `node_modules` from current authority, replace `node-sass` with maintained Sass tooling, make the build reproducible and review paths/accessibility/responsive behavior. Avoid another React rewrite unless a genuine product requirement appears.

### Later framework-specific learning lanes

- `Ecommerce_NestJS` — README fixed; later dependency/runtime/auth/test maintenance.
- `StarWars_App_NextJS` — README fixed; later Next/React/i18n/test maintenance.

### Historical backend lineage

`Proyecto_Backend` now explicitly points to Meow Matrix as the current full-stack authority. Future work is preservation/security/hygiene only unless a concrete historical-study need appears.

## 7. Client repository strategy

For client/landing work, first determine:

1. ownership and whether client relationship/content is still public;
2. current production URL/provider;
3. whether forms, email, CMS or upload endpoints still operate;
4. whether personal/client data exists in Git history or runtime storage;
5. whether large media is intentional and optimized;
6. accessibility/responsive/SEO baseline;
7. whether the repository is portfolio evidence, operational production, or both;
8. rollback and maintainer expectations.

Do not migrate a client landing to a fashionable framework without a real need, and never expose private CMS/product material to improve the public portfolio.

## 8. Empty/stub strategy

```text
identify purpose -> identify successor -> decide preserve / archive / private / delete
```

Empty repositories are not failures that need artificial code. Archiving plus an honest short README is generally better than manufacturing implementation.

## 9. Cross-portfolio standards to reuse

Every lane should evaluate what is relevant from this set:

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
- security headers where hosting supports them;
- docs-as-code;
- post-merge verification for infrastructure/release changes;
- explicit non-adoptions to avoid stack inflation.

## 10. Portfolio-level rules

1. **Do not rewrite history to look more senior.** Progression is more valuable when old limitations remain contextualized.
2. **Do not use one stack everywhere.** React, Next, Nest, Docker and databases are choices, not maturity badges.
3. **Security beats aesthetics.** Potential secrets, credential collection and privacy issues come first.
4. **Do not invent backends for prototypes.** A safe local demo can stay local.
5. **Do not invent current client relationships.** Historical public work must be labeled honestly.
6. **Do not expose private client/product material to improve the public portfolio.**
7. **Do not duplicate active products.** Resolve lineage/supersession first.
8. **Keep the profile repository synchronized.** Completed work must not stay described as future work.
9. **One major legacy modernization lane at a time.** Small documentation/security hygiene may run separately.
10. **Close each lane completely.** Code, CI, docs, evidence and central roadmap move together.

## 11. Current portfolio program state

```text
COMPLETED MODERNIZATIONS / REFERENCE
El_Nucleo_Web
Web-de-profesores
Pint.ar_Ecommerce
Meow Matrix — provider-neutral full-stack/release carrier through B7

IMMEDIATE SECURITY TRIAGE
TrackIt_Frontend — current-tree hygiene merged; historical/external credential classification remains

NEXT GENERAL PORTFOLIO LANE
App_Agenda_Medico

FOLLOWING HISTORICAL LANE
Web_de_vinos

LATER FRAMEWORK-SPECIFIC LANES
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

The next implementation gate is `App_Agenda_Medico`.

Before changing behavior:

- pin the historical 2023 authority (`390ac3591b089e0aefd6dc5f971c3e8d22e57794`) and preserve collaborator authorship;
- inspect the interactive menu and all TAD operations against the documented specification;
- inventory behavior worth preserving vs. correctness bugs worth fixing;
- create a separate maintained Python authority rather than rewriting the original exercise in place;
- choose standard-library-first packaging/testing unless a dependency is justified;
- qualify FIFO queue behavior, patient/citation semantics, agenda deletion/filtering and rescheduling through tests;
- add CI and repository hygiene;
- synchronize this roadmap/profile only after the repository lane is actually integrated.

The target story is explicit: **the project should still look like a data-structures/algorithm exercise, but one that a 2026 engineer can install, understand, test and safely evolve.**
