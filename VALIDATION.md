# English Delivery Validation

Date: October 29, 2026.

- Node homepage build succeeded without dependencies.
- Chromium loaded the site under `/zhangxj.github.io/` with both stylesheets and the local photo.
- The generated page declares `lang="en"` and contains no Chinese characters.
- Verified Georgia typography and the reference Jemdoc heading color `#527bbd`.
- Verified six publication entries, six highlighted author names, seven honors, and valid internal anchor targets.
- Verified three user-supplied teaching entries on the homepage and in the CV, with matching course levels, semesters, year, and institution.
- The CV download returned HTTP 200 with a PDF content type and valid PDF header.
- Desktop, 390px, and 320px layouts were checked. No horizontal mobile overflow, page errors, or failed local resources were found.
- The final CV contains exactly two English A4 pages and six numbered papers. Its text lies within the intended page bounds; both pages were rendered and visually reviewed.
- The reference person's identity and unrelated employment, teaching, and reviewing claims are absent.
- The separately delivered PDF and the website download are byte-identical.
- ZIP integrity and required-file presence are checked during packaging.

No changes were pushed to GitHub, and GitHub Pages settings were not modified. See `MIGRATION.md` for source decisions, translation limits, and old-file cleanup guidance.
