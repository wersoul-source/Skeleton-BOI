# Context manifest

## Load by task

| Level | Read | Use |
|---|---|---|
| 0 | README.md | orientation |
| 1 | AGENTS.md, START_HERE_AGENT.md, ARCHITECTURE.md | initialization / editing |
| 2 | docs/SIGNATURE.md, INITIALIZATION.md, VALIDATION.md, relevant source tag | technical decisions |
| Private | local ignored overlays only with explicit need and user authority | sensitive context |

## Canonical ownership

- docs/SIGNATURE.md owns role semantics.
- Generated usa.project.json owns five answers and physical path mapping.
- Generated ARCHITECTURE.md / PROJECT_BRIEF.md are derived, not independent authorities.
- ADR owns rationale and alternatives; handoff owns open work and evidence.
- README links to authoritative files instead of duplicating changing details.

When sources disagree, surface the contradiction and follow the user's direct correction within higher-priority operating constraints. Preserve provenance: reported requirement, inferred decision, observed evidence. Never promote an assumption to a verified fact. This is project context, not a copy of the user's personal memory.
