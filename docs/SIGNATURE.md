# Structural Signature v1

## Outcome → Structure → Mechanism → Risk → Execution

Outcome comes from q1/q5. Structure maps logical roles to physical paths. Mechanism describes input → validation → use case → rules → port/adapter → output. Risks derive from q4 and missing evidence. Execution ends at a reproducible scaffold plus Dev handoff.

| Role | Owns | Must avoid |
|---|---|---|
| interface | input/output, transport/UI validation | business rules hidden in UI |
| application | use-case orchestration, ports | framework/vendor coupling |
| domain | invariants, policies, entities | imports from outer layers |
| infrastructure | persistence, OS/network adapters | redefining domain rules |
| contracts | boundary schemas, interfaces, compatibility | duplicated conflicting schemas |
| tests | behavior and acceptance evidence | treating mocks as live acceptance |
| operations | delivery/recovery/config guidance | committed secrets |
| docs | map, decisions, provenance, handoff | stale duplicate truth |

Roles do not require eight services or packages. In a small framework project, use its native modules and map them in project config; do not create layers with no responsibility. The starter generator uses separate folders for visibility only.

Invariant: change path names without changing responsibilities or dependency direction. Path changes must update canonical config and derived documentation together. Schema/version or external contract changes require explicit compatibility decisions.

Credit: [Skeleton-BOI](https://github.com/wersoul-source/Skeleton-BOI)
