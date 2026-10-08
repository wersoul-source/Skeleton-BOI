# Contributing

Keep changes scoped. Describe the problem, final behavior, validation and limitations. Update role semantics in docs/SIGNATURE.md first when the signature changes, then generator/architecture/examples together. Run `python -m unittest discover -s tests -v`. Do not add a framework dependency merely for scaffolding.

For generated products: preserve usa.project.json as canonical mapping; add product docs under its mapped docs role. Generated documents are reproducible views. Product-specific runtime detail belongs in separate documents so regeneration does not overwrite it.

Credit: [Skeleton-BOI](https://github.com/wersoul-source/Skeleton-BOI)
