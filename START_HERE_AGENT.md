# Starter instruction — clone → understand → edit immediately

## 0. Obtain workspace

If this repository is already open, do not clone again. Otherwise clone `https://github.com/wersoul-source/Skeleton-BOI.git` into a new user-authorized workspace. Inspect current directory, git status and existing files. Do not assume the source repository is the product destination.

## 1. Understand

Read AGENTS.md → MANIFEST.md → docs/SIGNATURE.md → ARCHITECTURE.md → docs/INITIALIZATION.md. Read docs/SOURCES.md only for topics needed by this task. Do not crawl entire sites or load private context by default.

## 2. Ask exactly five initialization questions

Present the five numbered questions in README.md as one questionnaire. Reuse explicit answers already supplied; do not ask the same question again. Wait for user answers before dependent generation. Mark unanswered fields unknown. Do not guess identity, credentials, deployment access or acceptance results.

## 3. Decide and edit

Select the smallest profile that fits. Map eight roles to real paths; adapt names to the OS/framework. Capture assumptions in ADR and unknowns in handoff. Prepare a JSON config with project/profile/answers/paths; dry-run into a fresh destination, inspect the plan, then --apply within the task's authorized scope. Copy AGENTS.md, MANIFEST.md, scripts/usa.py and product-relevant guidance into a NEW product workspace; create its own README with actual commands or NOT_IMPLEMENTED. Do not replace generated ARCHITECTURE.md with this template's architecture.

In an existing codebase: map to current paths, stage documentation changes with reviewable diffs, and leave implementation files where they are. The generator intentionally refuses conflicting files; it is not an in-place migration engine.

## 4. Validate

Run generator tests and validate the output. Inspect role responsibility, dependency direction and input-to-output flow. Replace the generated generic flow with product-specific details in a separate docs/SYSTEM_FLOW.md under the mapped docs role. Record canonical links from the product README. Do not label empty directories as working components.

## 5. Handoff and stop

Deliver path map, five answers, ADR, risks/unknowns, validation evidence and one concrete next action for Dev. Product implementation/build/deploy/security acceptance remains NOT_RUN unless actually tested. Do not expand into a new architecture program or automatically implement features.
