# Public integration interface — proposed for lead acceptance

Public repository: `majieddd/new-ai`. Builder worktree: `REPOS/new-ai-release`; branch `feat/public-release-foundation`. This is a fresh release history, not a republished private research tree. Existing `majieddd/new-ai-dashboard` and its URLs/history are not replaced.

## Path ownership

| Path | Owner | Interface / current disposition |
|---|---|---|
| `src/new_ai/model/` | Cloud AI Generalist; existing mechanism owners retain implementation | Reviewed actual prototype and checkpoint loader only; currently absent |
| `examples/` | Model lead | Original synthetic CPU config and one-command example; awaiting actual exercised prototype |
| `tests/model/` | Model lead / independent evaluator | Paired boundary/normal regressions, no final material |
| `evidence/receipts/` | Model lead integrates reviewed records | Safe immutable developmental JSON with producing SHA, command, metrics, artifacts/hash, limitations |
| `research/paper/versions/<version>/` | Researcher through lead | `paper.md`, `bibliography.bib`, `CHANGELOG.md`; previous versions retained |
| `research/paper/manifest.json` | Lead | Ordered accepted versions and producing/source hashes |
| `site/`, `src/new_ai/publication.py`, `schemas/`, `.github/workflows/` | Builder | Dashboard, typed update pipeline, CI and reviewed Pages publication |
| `diagrams/` | Builder | Native Archify inputs/outputs/evidence and source/status anchors |
| `status/project.json` | Lead integration; Builder schema/UI | Exact current states, owners and dependencies; never inferred success |

## Model command — interface proposal, not implemented

Reserve `python -m new_ai.model --config examples/cpu_development.json --out .runs/development` for the lead's actual train/load/freeze/energy-inference/growth/rollback prototype. The lead may specify a smaller actual API before integration. Builder does not create placeholder heads, fabricated model traces, a fake checkpoint or substitute LoRA routing.

## Publication and review

Builder submits scaffold/site PRs. Lead reviews and integrates accepted model/paper bytes on its own branch/worktree, then approves publication. Pages deploys accepted `main` only. Feature-branch previews never claim production or model completion. Never write the lead's active hub/model worktrees.

The milestone update rule is: accepted safe receipt + status + versioned paper -> schema/consistency/source-link tests -> dashboard plots/diagram status/paper -> reviewed PR -> Pages -> deployed-byte verification. CI performs CPU-only software checks, not model training.
