# Initialization workflow

1. Inspect destination and existing architecture without mutating it.
2. Ask the five questions from README once; reuse known answers.
3. Record answers in q1–q5. Explicit unknown is acceptable for scaffold planning, not authorization to invent behavior.
4. Choose minimal profile and physical paths. For Mobile use desktop + overrides. Record selection and alternatives in ADR.
5. Run preview; resolve path/conflict errors by selecting a fresh directory, never by deleting user work.
6. Apply, validate and inspect output. Copy starter guidance/tooling into a new product only; add product README and SYSTEM_FLOW.md.
7. Fill handoff with unknowns and exact evidence. Stop at STRUCTURE_READY.

Config schema: exactly project (lowercase slug), profile (web/desktop/cli/service/data), answers (five nonempty strings q1–q5), paths (zero or more known role overrides). Resolved config contains all eight paths. UTF-8 Thai text is supported. Role paths are portable ASCII relative paths, distinct, not nested, and cannot overlap template tooling.

Reinitialization: identical output is unchanged. Config edits require a fresh output plus reviewed migration; no --force switch exists. Existing projects are documentation mapping work, not generator overwrite targets.
