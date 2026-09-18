# Repository portfolio roadmap — 2026

Snapshot date: 2026-09-17  
Last program update: 2026-09-18 — `ejercicioDjango` completed and post-merge verified; `2024-UTN-GRUPO-2` selected as the next authorship-first academic discovery lane  
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
| `App_Agenda_Medico` | Public | A/C | 2023 Python TAD exercise with separate 2026 typed authority | **Completed**: FIFO fix, 11 tests, Python 3.12/3.13/3.14 CI |
| `Web_de_vinos` | Public | A/B | Nicolas Dadario 2023 HTML/SCSS baseline with 2026 maintenance lane | **Completed**: Dart Sass, portable HTML, truthful demo forms, CI + Pages |
| `Proyecto_Backend` | Public | D/B | Historical Express/Mongo ecommerce lineage | Lineage resolved toward Meow; preserve/audit rather than duplicate |
| `Chat_En_Vivo` | Public | F | Near-empty/stub | Verify successor; document/archive rather than invent |
| `GIUCT-SQL-v1` | Public | F | Empty/stub | Preserve/archive decision |
| `Plantilla-de-Proyecto` | Public | A/G | Reusable Node/TS/Fastify starter | Maintain/reference |
| `Ecommerce_NestJS` | Public | C/D | NestJS ecommerce learning backend; 2026 modernization complete | **Completed**: Node 24, Nest 12, secure auth/recovery boundaries, 38 unit + 3 integration + 5 E2E tests, permanent CI |
| `Meow-Matrix---Frontend` | Public | A/D | Maintained frontend authority for Meow Matrix | B7 engineering carrier complete; provider cutover external |
| `MeowMatrix---Backend-2v` | Public | A/D | Maintained backend/release authority for Meow Matrix | B7 engineering carrier complete; provider cutover external |
| `StarWars_App_NextJS` | Public | C/B | Next.js learning app; 2026 modernization complete | **Completed**: Next 16 + React 19, portable i18n/SWAPI contracts, permanent CI, zero npm audit findings, Vercel-qualified delivery |
| `Portfolio_Backend` | Public | F/C | Small backend scaffold | Determine supersession vs `portafolio-personal` |
| `luciano-legnoverde` | Public | E | Client/person landing | Ownership/deploy/content/privacy audit only |
| `centuryLanding` | Public | E | Client landing | Audit with `centuryBackend` |
| `centuryBackend` | Public | E/D | Small backend/upload surface | Audit with landing, focus data/upload security |
| `2024-UTN-GRUPO-2` | Public | C | Collaborative academic project with multiple authors | **Next discovery lane**: provenance/authorship first; preserve team contributions before any docs/tests maintenance |
| `odoo-practice` | Public | F | Empty practice stub | Keep/archive; do not manufacture project |
| `portafolio-personal` | Public | G | Current portfolio/product infrastructure | Active maintenance only |
| `AntigalBackend` | Public | F/E | Empty paired backend | Verify intentional supersession |
| `Vicky-Pellegrino-Landing` | Public | E | Client landing | Production/content/accessibility audit only |
| `Antigal_Frontend_Enzo` | Public | E | Client frontend | Audit with paired history/ownership |
| `TrackIt_Backend` | Public | F/D | Empty backend repository | Determine intended successor/authority |
| `TrackIt_Frontend` | Public | D/B | React 18 CRA prototype | Current-tree security hygiene done; historical secret review still open |
| `ejercicioDjango` | Public | A/C | Small Django exercise with completed 2026 maintenance lane | **Completed**: Python 3.12.14, Django 5.2.17 LTS, 25 tests, clean migration rebuild, HTTP smoke, permanent CI |
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

### P3 — `App_Agenda_Medico` — COMPLETED

The 2023 collaborative TAD/data-structure exercise remains auditable at baseline `390ac3591b089e0aefd6dc5f971c3e8d22e57794`, including original collaborator history. The maintained 2026 authority is deliberately separate under `modern/` and uses standard-library-first Python rather than turning the exercise into a web product.

Completed evidence:

- `Paciente` / `Cita` immutable dataclasses and an encapsulated `Agenda`;
- real FIFO `ColaCitas` via `deque.popleft()`, fixing the historical `list.pop()` LIFO behavior;
- date/time represented by Python standard types;
- maintained console interface with no external runtime dependencies;
- eight tracked `.pyc`/`__pycache__` artifacts removed from current authority;
- **11/11 behavior tests** across Python 3.12, 3.13 and 3.14;
- PR #5 merged with exact-head guard;
- final `main`: `d6a335738eb0c9b4dc8751049faa3c21a97bad00`;
- post-merge `Python quality` run `35229223343` succeeded on all three Python versions.

### P4 — `Web_de_vinos` — COMPLETED

The repository now preserves its actual provenance: the historical baseline `c95ca4bad1b11f0c946a3c04764c63ca18e6d7c6` was authored by Nicodadario / Nicolas Dadario, while Enzo's contribution is explicitly the 2026 modernization/maintenance lane.

Completed evidence:

- thousands of generated `node_modules/` files removed from current Git authority while history remains intact;
- `node-sass` + `nodemon` replaced by exact Dart Sass `1.104.1` with lockfile-v3 reproducibility;
- legacy Sass `@import` entrypoint migrated to module-based `@use`;
- committed `css/style.css` is verified as a deterministic build artifact;
- language, viewport, favicon/local paths and navigation semantics corrected;
- unnecessary remote Bootstrap JavaScript/jQuery/Popper removed;
- contact/subscription forms are now visibly non-submitting demos and do not transmit data;
- custom validator checks five pages, assets, alt text, local references, demo-form truth boundaries and dependency hygiene;
- permanent CI runs exact install, high-severity audit, site validation, CSS reproducibility and HTTP smoke;
- PR #3 merged with exact-head guard;
- final `main`: `cadedaa822e87f7a2131625d2acc197efb6e184f`;
- post-merge `Static quality` run `35234556753` succeeded;
- GitHub Pages build/deploy run `35234554578` succeeded for `https://enzopinotti.github.io/Web_de_vinos/`.

### P5 — `Ecommerce_NestJS` — COMPLETED

The 2024 NestJS/Mongo learning backend is now a completed framework-maintenance case rather than a future lane.

Completed evidence:

- contextual baseline on `main`: `d3313889bf6a774e5cddf2b34685d789c9eecf00`;
- complete B0–B8 modernization reviewed in PR #3;
- exact PR head before merge: `ff89607cf70784b32085e36799c184f22f83b84f`;
- squash-merged final `main`: `e47d27899fd775b06399be6cb128fdeeab624ff0`;
- exact-head PR Quality run `35301362232` succeeded after explicitly verifying the checked-out SHA equals the PR head;
- post-merge Quality run `35301527433` succeeded on final `main`;
- Node 24 / npm 11 reproducibility;
- NestJS 12 + TypeScript 5.9.3 maintenance baseline;
- fail-fast configuration and production asset/build contract;
- one cookie-session auth authority with no JWT returned in auth JSON;
- password recovery uses opaque tokens, digest-at-rest, expiry and one-use consumption;
- truthful read-only product/category surface with ObjectId and bounded-query validation;
- lint 0 / formatting clean / production high audit blocking;
- **14 unit suites / 38 unit tests + 3 integration tests + 5 E2E tests**;
- permanent two-job CI plus weekly Dependabot;
- no payments, transactional cart/checkout, invented roles or production infrastructure added.

### P6 — `StarWars_App_NextJS` — COMPLETED

The Next.js learning application is now a completed framework-maintenance case with its historical scope preserved.

Final evidence:

- repository issue: `Enzopinotti/StarWars_App_NextJS#2` — closed;
- integration PR: `Enzopinotti/StarWars_App_NextJS#3` — squash merged;
- reviewed PR head: `9b5b857e9016a80f03ebf3591b2fd725d239d48b`;
- final `main`: `2b3b1ca9c699757b793b35e418d851fda7f47002`;
- branch Quality run: `35357837618` — success;
- pull-request Quality run: `35357842513` — success;
- post-merge `main` Quality run: `35358011800` — success;
- Vercel preview and post-merge production status: success;
- Next `16.3.5` + React `19.3.0`;
- deterministic EN/ES localization and SWAPI failure contracts;
- route/data and accessibility/responsive contracts;
- production audit: 0;
- complete dependency-tree audit: 0;
- Pages Router and Tailwind 3 deliberately retained;
- no backend/auth/database/product rewrite invented.

The lane also caught and repaired a real deployment portability regression: local/CI versions remain exactly pinned, while deployment-facing engines now express the supported Node 24.x / npm 11 major contract rather than a platform-hostile minor/patch floor.

### P7 — `ejercicioDjango` — COMPLETED

The small Django learning exercise is now a completed framework-maintenance case with its academic scope preserved.

Final evidence:

- repository issue: `Enzopinotti/ejercicioDjango#1` — closed as completed;
- integration PR: `Enzopinotti/ejercicioDjango#2` — squash merged;
- reviewed branch head: `1a28aecf2e5d33afd6126d11f18f9561f4baa9dd`;
- final squash-merged `main`: `d85ae524973cacfef3f9fb418a092e8dcc37c0c4`;
- branch Quality run: `35364889681` — success;
- pull-request Quality run: `35373406247` — success;
- post-merge `main` Quality run: `35373621002` — success;
- historical runtime reconstructed as Python 3.12 + Django 5.0 before maintenance changes;
- maintained runtime: Python `3.12.14` + Django `5.2.17` LTS;
- tracked SQLite runtime state and 12 tracked `.pyc` files removed from maintained Git authority;
- database is rebuilt from migrations on clean CI;
- behavior/accessibility/admin suite expanded from 0 to **25 tests**;
- future-question visibility/voting defects and hidden vote-error feedback were fixed;
- local configuration is explicit through optional environment overrides without inventing production HTTPS infrastructure;
- real `runserver` HTTP smoke verifies polls index/detail/results/static/admin behavior;
- maintained dependency audit reports no known vulnerabilities;
- SHA-pinned Actions, evidence artifacts and monthly Dependabot are permanent.

This repository remains intentionally small: no REST rewrite, React frontend, PostgreSQL, Docker or custom auth was added.

### P8 — `2024-UTN-GRUPO-2` — NEXT AUTHORSHIP-FIRST DISCOVERY LANE

This repository is a collaborative 2024 academic project, so provenance is the first constraint rather than framework novelty.

Initial inspection already proves multiple authors in the mainline history, including Enzo Pinotti, Matias Rau Bekerman, Patricio and Natasha Cadabon. The current `main` authority is `b63af0a8092ae4ce69aad4013affc6159cf7fafa`.

The first block must remain discovery-only:

- map authorship and branch/merge history before attributing work;
- identify the academic assignment/course context from repository evidence;
- inventory `Frontend/` and `Backend/` stacks, package/runtime authority and deployment assumptions;
- inspect authentication/data/API boundaries without reproducing secrets or private values;
- run existing build/test commands before dependency changes;
- distinguish team-authored behavior from Enzo-authored contributions;
- preserve team history rather than rewriting the project into an individual portfolio artifact;
- choose docs/tests/maintenance only after the provenance boundary is explicit.

No behavior modernization is authorized merely by selecting the lane.

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

COMPLETED HISTORICAL / ACADEMIC LANES
App_Agenda_Medico
Web_de_vinos

COMPLETED FRAMEWORK-SPECIFIC LANES
Ecommerce_NestJS
StarWars_App_NextJS
ejercicioDjango

NEXT AUTHORSHIP-FIRST ACADEMIC DISCOVERY LANE
2024-UTN-GRUPO-2

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

The next implementation gate is **discovery-only** for `2024-UTN-GRUPO-2`.

Before changing behavior:

- pin current `main` and inspect the complete authorship/merge history;
- identify the academic assignment and team context from repository evidence;
- inventory the frontend/backend stacks, package managers, runtime versions, routes/APIs, persistence and deployment assumptions;
- run existing build/test commands before changing dependencies;
- inspect public configuration and secret-handling boundaries without reproducing historical values;
- separate Enzo-authored contributions from work authored by collaborators;
- decide whether the correct treatment is maintenance, documentation/testing only, or preservation;
- do not rewrite collaborative history into an individual-origin story.

Current discovery authority:

- repository: `Enzopinotti/2024-UTN-GRUPO-2`;
- `main`: `b63af0a8092ae4ce69aad4013affc6159cf7fafa`;
- visible top-level structure: `Frontend/`, `Backend/`, `.gitignore`, `README.md`;
- history already shows multiple authors, so provenance is a hard gate.

The target story is not “modernize everything.” It is: **understand the collaborative academic artifact accurately, then make only the smallest maintenance changes that can be attributed and justified.**
