# Profile maintenance runbook — 2026

## Purpose

This document is the operational handoff for the public GitHub profile repository.

It exists so the profile, repository portfolio roadmap and 3D contribution landscape can be maintained without reconstructing the 2026 modernization context from old issues or chat history.

## Current authority

Profile repository:

`Enzopinotti/Enzopinotti`

Current maintained state before this runbook:

`f1d3b58079d1d383cb3d2f23a6cbd12b9aa3ebcd`

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

Whenever a repository lane changes state:

`planned → active → completed`

update:

1. the repository-specific issue/PR;
2. `docs/repository-portfolio-roadmap-2026.md`;
3. README only when the public story materially changes;
4. central coordination issue #19.

Because roadmap changes trigger the 3D refresh, the graph then refreshes as a side effect of a meaningful portfolio change.

## Open coordination issues that are intentionally still active

### #1 — Engineering maturity program

Broad umbrella for meaningful engineering/public portfolio work.

Keep open while the broader program continues.

### #6 — Manual profile finish

The single remaining manual-profile checklist.

It contains:

- account bio;
- profile website;
- curated pins;
- repository descriptions/homepages/topics.

These settings are not repository-content changes.

### #7 — Open-source visibility

Keep open until there is at least one meaningful upstream contribution based on a real problem encountered in work.

Do not use typo spam or synthetic contribution farming.

### #19 — Repository portfolio modernization program

Central sequencing authority.

P8 is complete and P9 is intentionally unselected.

## Closed/superseded coordination issues

- #3 — maturity baseline: completed;
- #12 — old one-shot hardening rollout: superseded by #19;
- #13 — 3D refresh follow-up: completed;
- #14 — profile bio follow-up: consolidated into #6.

## Manual profile work still outstanding

Repository/API tooling available to this maintenance lane does not expose account-profile editing or repository metadata mutation.

Therefore the remaining manual GitHub UI work is deliberately tracked in #6 rather than represented as completed.

Do not close #6 until those profile-level settings are actually changed.

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
