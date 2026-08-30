# Roadborne asset rights and provenance

Use this reference before acquiring, generating, editing, or integrating a visual asset. It is a
recordkeeping workflow, not legal advice.

## Current authority

Initial Roadborne assets must be original or CC0 with recorded provenance. Do not broaden that
rule to royalty-free, marketplace, attribution-required, AI-generated, or commissioned material
without an explicit owner decision covering the source and rights.

Use the owning repository manifest, currently
src/Roadborne.Client/assets/world-preview/ASSET_PROVENANCE.md for WorldPreview assets. Do not copy
the bundled generic asset-manifest template into Roadborne or create a competing ledger.

## Record each retained source

- stable Roadborne asset ID and repository path;
- creator, original canonical URL, acquisition date, and source file/archive identity;
- exact license/version, saved license evidence, and evidence date;
- source archive/file-set hashes and every retained dependency;
- original resolution, units, formats, and selected subset;
- modifications, conversion/export tool versions, and responsible person/tool;
- explicit exclusions and rejected sources;
- generation model/version, prompt/reference identity, and edit history when generated;
- approval status and the evidence that supports only that status.

Keep purchase, account, or contract evidence outside a public repository when it contains private
information. Never expose credentials or personal data in a manifest.

## Decision rules

1. "Free", "royalty-free", search-visible, or model-generated is not a license.
2. Verify CC0 or other terms at the canonical source, not an aggregator.
3. Preserve license evidence and attribution through renaming, packing, conversion, and edits.
4. A generated concept remains Reference or Candidate; it is not automatically an original
   production mesh or a rights-cleared derivative.
5. Do not imitate or extract protected Silkroad Online assets. Translate only approved mechanical
   or high-level visual relationships into original Roadborne work.
6. Preserve the repository's checksum and Git LFS conventions for retained large sources.
7. Separate source/license proof, import proof, visual acceptance, and player-facing artifact
   proof. None substitutes for another.
8. When terms or ownership are unclear, stop before repository integration and request owner or
   qualified rights review.

Useful primary references:

- Creative Commons CC0: https://creativecommons.org/public-domain/cc0/
- SPDX license list: https://spdx.org/licenses/
