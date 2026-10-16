# Cross-Session Protocol

## Source of truth and workspace

- GitHub repository `lin2mm/LockPCB` is authoritative for KiCad source, scripts and design decisions. Drive is for handoff/reference/feedback/backups; do not treat a Drive ZIP as newer than committed GitHub source without comparison.
- Arena session branch is `arena/3b84c22f-lockpcb`; continue on this branch only. Do not merge `main` during this session. Commit/push only this branch when requested/authorized.
- In this environment the checkout path is `/home/user/LockPCB`. `/home/user/smart-lock-pcb/` was not present at the start of the 2026-10-16 work; do not create a duplicate workspace or silently copy over files.

## Decision handling

- Keep confirmed user constraints separate from soft preferences, working assumptions, and TBD inputs.
- Compare options for size, power, reliability, sourcing and manufacturing risk. Record recommendation and rationale in `decisions/` and `docs/DESIGN_DECISIONS.md`.
- Only request the six blocking inputs listed in `decisions/0002-candidate-components-and-open-items.md`; if unavailable, maintain explicit placeholders.
- Never declare fit, electrical closure, hardware validation, or manufacturing readiness without supporting data/checks.

## CAD and CI

- `.kicad_pro`, `.kicad_sch`, `.kicad_pcb` are project source. KiCad source is authoritative; Gerbers are later exports only.
- CI is pinned to KiCad major version 8 and must preserve CLI exit codes, ERC/DRC reports and custom-check results. Upload diagnostic artifacts even on failure.
- Text-only schematic/net intent checks must be called intent parity, not electrical connectivity parity. No components means the unconnected-net result is explicitly N/A, not a fabricated pass.
- At session end update `PROJECT_STATE.md` and `SESSION_HANDOFF.md` with branch, current commit, dirty/clean status, files changed, actual checks/results, blockers and next actions. Do not claim a CI result until Actions actually ran.
