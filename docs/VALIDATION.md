# Validation contract

## Required evidence

| Gate | Passing evidence | Does not establish |
|---|---|---|
| Tool tests | unittest exits 0 | application behavior |
| Structure | validate exits 0 | framework build |
| Map review | every role/path/flow explained | dependency enforcement |
| Dev acceptance | real stack build/tests and criteria from q5 | production unless actually exercised |

Tool regression tests cover profiles, path overrides, missing answers, traversal/absolute paths, case collisions, nested roles, conflict preflight, idempotence, stale files and symlinks where available. Generator checks managed documents; new application files are allowed and require their own checks.

Handoff must name check, command, environment, result (PASS / FAIL / NOT_RUN), limitations and next action. A directory and README are scaffold evidence only. Do not claim authentication, secure storage, live providers, device compatibility or deploy success from these tests.

Credit: [Skeleton-BOI](https://github.com/wersoul-source/Skeleton-BOI)
