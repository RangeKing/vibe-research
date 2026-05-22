# Submission Cleanliness Audit

Use this audit for near-submission, journal-targeted, package-readiness, editor/reviewer-style, cover-letter, figure-legend, Methods, Supplementary Information and Word/PDF package work.

## Purpose

Editor- and reviewer-facing text must read like a manuscript, not a workspace log. Internal traces are submission blockers because they signal that the draft has not been cleaned for peer review.

## Hard Blockers

Flag and remove or formalize:

- local paths, repository paths and workspace names, including slash-separated paths and filenames in backticks
- raw filenames and extensions used as provenance, such as `.shp`, `.csv`, `.docx`, `.md`, `.py`, `.geojson` or `.zip`, unless the journal-facing data availability statement explicitly names a deposited file
- code variables, column names and implementation tokens used as prose evidence, unless they are deliberately defined as formal equations or SI variables
- commands, scripts, tools, notebook names, generated-asset folders and pipeline names
- project-management notes such as "current workspace materials", "source audit", "latest pass", "this package", "author-side completion", or "recommended manuscript file"
- draft or agent residue, including "the supplied result text", "the current figure-generation pipeline", "we rebuilt", "review package", "checkpoint", or "placeholder pass"

## Rewrite Patterns

- Replace a local file path with a formal data noun: "the source geospatial polygon layer", "the processed country-level area table", "the figure source data" or "available validation information".
- Replace implementation-specific fields with analytical descriptions: "country-specific area attributes" rather than a raw field or file name.
- Replace workspace provenance with citable provenance: "remote-sensing validation information", "official statistical comparison" or "processed geospatial baseline".
- Keep deposited dataset names only in Data availability, Code availability, SI data descriptions, or repository metadata, and only when those names are stable public artifacts.

## Availability statements

For Data Availability, Code Availability, materials, protocols, or source-data statements:

- Inventory every dataset behind main and supplementary results: raw data, processed data, figure source data, model outputs, images, tables, and statistical-analysis files.
- Classify each access route: public repository, controlled access, within paper/SI, reused public source, third-party restricted, justified request, or not applicable.
- Prefer stable identifiers such as DOI, accession number, repository record, Handle, or ARK when the user provides them.
- Treat "available upon reasonable request" as weak unless the statement names the restriction, controller, review route, and available metadata.
- Separate data, code, materials, and protocols unless the target journal requires a combined statement.
- Never invent DOIs, accession numbers, repositories, licences, embargo dates, access committees, or approvals.

## Audit Procedure

1. Scan main text, Methods, figure legends, tables, SI, cover letter and availability statements.
2. Search for backticks, slashes, file extensions, code-like identifiers, commands and local folder names.
3. Decide whether each instance is a formal public artifact or internal residue.
4. Rewrite internal residue before polishing style or judging submission readiness.
5. Re-run the scan after rebuilding any Word/PDF package, because build scripts and captions can reintroduce hidden strings.

## Output Contract

When reporting this audit, include:

- `Internal trace status`: clear / blockers found / not checked
- `Blockers fixed`: concise list of manuscript-facing strings removed or formalized
- `Residual allowed technical terms`: terms kept deliberately, such as formal variables or public repository file names
- `Follow-up scan`: whether a text/package scan was rerun after edits
