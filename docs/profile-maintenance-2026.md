# Profile maintenance runbook — 2026

## Purpose

This document is the operational handoff for the public GitHub profile repository.

It exists so the profile, repository portfolio roadmap and 3D contribution landscape can be maintained without reconstructing the 2026 modernization context from old issues or chat history.

## Current authority

Profile repository:

`Enzopinotti/Enzopinotti`

Operational baseline before the final 2026 closeout:

`f1d3b58079d1d383cb3d2f23a6cbd12b9aa3ebcd`

Current `main` is the runtime authority; do not treat this historical baseline as a branch target.

Portfolio inventory:

**46 repositories**

Latest completed general modernization lane:

**P8 — `2024-UTN-GRUPO-2`**

P8 final documented main:

`5bca5199db7de80b7ab2f2a75d8d55bab0e27408`

Next general portfolio lane:

**selection pending**

Do not preselect P9 merely to keep the sequence moving.

## Profile quality authority

Workflow:

`.github/workflows/profile-quality.yml`

It validates:

- README structure and required narrative contracts;
- portfolio roadmap contracts;
- dark/light image references;
- 3D settings;
- branding postprocessor;
- 3D publish-safety workflow;
- required SVG validity;
- cache-version consistency.

Current last green push evidence before this runbook:

- Profile quality #43
- run `35638074628`
- head `f1d3b58079d1d383cb3d2f23a6cbd12b9aa3ebcd`

## 3D build-signal landscape

Generated assets:

- `profile-3d-contrib/profile-enzo-dark.svg`
- `profile-3d-contrib/profile-enzo-light.svg`

Generator workflow:

`.github/workflows/profile-3d.yml`

### Triggers

The workflow intentionally supports two triggers only:

1. manual `workflow_dispatch`;
2. a push to `main` that changes:

   `docs/repository-portfolio-roadmap-2026.md`

There is deliberately **no schedule/cron**.

This avoids meaningless daily generated commits while still refreshing the graph whenever the central portfolio state materially changes.

### Generation pipeline

The workflow:

1. checks out full history;
2. runs the pinned `github-profile-3d-contrib` generator;
3. applies Enzo-specific branding;
4. recalculates a content-derived cache key;
5. rewrites all three README SVG references with the new `?v=<hash>`;
6. runs the profile validator against the generated output;
7. commits only if README/SVG output changed;
8. fetches and rebases against latest `origin/main`;
9. retries the push up to three times without force.

If a rebase conflict occurs, the workflow aborts rather than overwriting newer profile work.

### Last proven refresh

Automatic roadmap-driven refresh:

- workflow run: `35637769393`
- conclusion: success
- generated commit:
  `3156b1264b973c8b5f727b9138baece2b790602e`

Generated window:

**2025-09-21 → 2026-09-21**

README cache key:

`8dc8e7b6988c`

Generated radar at that refresh:

- commits: **1155**
- issues: **68**
- pull requests: **117**

Both generated themes contain:

`BUILD SIGNAL // ENZO PINOTTI`

## How to verify a refresh

After a successful refresh:

1. confirm the workflow completed successfully;
2. confirm a generated commit exists only when output changed;
3. open README and verify all three landscape references share one new 12-character cache key;
4. inspect both SVG files and confirm the date window ends at the expected current date;
5. verify the branding marker still exists;
6. ensure Profile quality remains green for any human-authored workflow/config change.

Generated pushes made with GitHub's workflow token do not recursively trigger another workflow. That is why the 3D workflow validates generated output **before publishing it**.

## If the graph appears stale in GitHub UI

Check in this order:

1. README cache key changed;
2. generated SVG blob SHA changed;
3. SVG date range is current;
4. browser/profile rendering is not showing an old cache.

Do not add timestamp-only README commits to force refresh.

The content-derived `?v=<hash>` is the cache-busting authority.

## If the graph workflow fails

### Generator or branding failure

Inspect:

- pinned generator action;
- `.github/profile-3d-settings.json`;
- `.github/scripts/brand-profile-3d.py`.

Do not edit generated SVGs by hand as the primary fix.

### Validator failure

Run/inspect:

`python3 .github/scripts/validate-profile.py`

Fix the source contract, not the validator output artifact.

### Push/rebase failure

The workflow already retries three times.

If it still fails:

- inspect concurrent `main` changes;
- never force-push generated output over newer profile work;
- rerun after reconciling the source change.

## Portfolio synchronization rule

The 2026 portfolio-modernization program is closed after P8.

If a future repository lane is activated:

1. fetch current `main`;
2. re-evaluate the 46-repository inventory;
3. open a **new scoped issue** for that lane or for a new portfolio program;
4. update `docs/repository-portfolio-roadmap-2026.md`;
5. update README only when the public story materially changes.

Because roadmap changes trigger the 3D refresh, the graph will refresh as a side effect of a meaningful portfolio change.

Do **not** reopen old coordination issues merely to start P9.

## Coordination issue status

All profile-repository coordination issues from the 2026 program are closed.

- #1 — engineering maturity program: completed for the 2026 profile/portfolio scope;
- #3 — maturity baseline: completed;
- #6 — manual profile finish: closed as an optional/manual checklist, not repository-blocking work;
- #7 — open-source visibility V1: closed without adoption in this program;
- #12 — old one-shot hardening rollout: superseded by #19;
- #13 — 3D refresh follow-up: completed;
- #14 — profile bio follow-up: consolidated into #6;
- #19 — repository portfolio modernization program — 2026: completed after P8.

There are no intentionally open coordination issues in this repository.

## Optional manual profile polish

Some GitHub account/repository metadata settings are outside repository-content automation:

- profile bio;
- profile website;
- curated pins;
- repository descriptions/homepages/topics.

The recommendations remain preserved in closed issue #6 for reference.

These are optional profile-polish tasks and are not blockers for the repository closeout.

## Rules for future maintenance

- preserve historical and collaborative provenance;
- do not manufacture activity;
- do not split trivial work into artificial commits;
- do not schedule graph churn;
- prefer exact-head validation before publication;
- keep private/client material out of public documentation;
- do not rewrite active private products as legacy portfolio exercises;
- update the central roadmap only for material state changes;
- keep the graph as evidence of activity, not as the activity goal.
