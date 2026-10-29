# Source and Migration Notes

Checked October 29, 2026. Target: `zfc-2018/zhangxj.github.io`, default branch `master`; baseline revision inspected: `de428a422d572991bd26c0bbf766f6951aaeddf8`.

## Scope

This package replaces the previous bilingual homepage with an English homepage in the classic Jemdoc visual style requested by the user. It includes an English two-page CV based on the layout of the user's reference `CV.pdf`.

Employment, education, teaching, publications, interests, grants, awards, talks, service, and the patent application are shared between the CV and homepage through the same JSON source files. The CV omits the longer publication summaries to follow the compact reference layout.

## Sources

- [Central South University faculty profile](https://faculty.csu.edu.cn/zhangxiaojiang/zh_CN/index.htm): current institution, public email, month-level education/employment dates, overview of three grants, and photo.
- [University publication list](https://faculty.csu.edu.cn/zhangxiaojiang/zh_CN/zdylm/221253/list/index.htm): five listed papers.
- [Min Tang's publication list](https://ins.sjtu.edu.cn/people/mtang/Publications.html): papers coauthored by X. J. Zhang / Xiaojiang Zhang and their research descriptions. Other Zhang authors' papers and Min Tang's unrelated research topics were excluded.
- The user's original Chinese CV: degree specializations, doctoral/postdoctoral mentors, project details, historical paper statuses, talks, service, honors, and patent application. Both pages were visually inspected because the PDF's Chinese character mapping affected text extraction.
- [Crossref](https://api.crossref.org/) and primary journal/arXiv records: authors, formal titles, journal names, DOI, volume, and page/article numbers.
- The newly supplied reference `CV.pdf`: layout only. It did not provide additional facts about Xiaojiang Zhang. Its teaching, reviewing, affiliations, awards, and alphabetical-authorship statement were not adopted.
- Teaching details supplied directly by the user: Probability and Statistics (undergraduate, Fall 2025), Linear Algebra (undergraduate, Spring 2025), and Statistical Inverse Problem (graduate, Fall 2025), all at Central South University. The course title Statistical Inverse Problem retains the singular form provided by the user.

## Publication records

Five published papers and one accepted paper are included:

1. Gu and Zhang, Journal of Scientific Computing 108, Article 49 (2026), [DOI](https://doi.org/10.1007/s10915-026-03373-x). The [publisher page](https://link.springer.com/article/10.1007/s10915-026-03373-x) gives June 22, 2026 as the publication date.
2. Zhang, Bai, and Tang, Depth splitting method for the linear Boltzmann model of primary proton distribution. Communications in Computational Physics, accepted in 2025 according to Min Tang's list. The [preprint](https://arxiv.org/abs/2504.00340) has the title A deterministic solver for the linear Boltzmann model of a single mono-directional proton beam, and identifies Xuemin Bai by full name. No unverified journal DOI, volume, or pages were added.
3. Zhang, Song, Shi, and Tang, Journal of Computational Physics 491, 112368 (2023), [DOI](https://doi.org/10.1016/j.jcp.2023.112368).
4. Jin, Tang, and Zhang, Journal of Computational Physics 452, 110895 (2022), [DOI](https://doi.org/10.1016/j.jcp.2021.110895).
5. Tang, Wang, and Zhang, SIAM Journal on Scientific Computing 43(3), B759-B783 (2021), [DOI](https://doi.org/10.1137/20M1318031).
6. Tang and Zhang, Journal of Computational Physics 436, 110290 (2021), [DOI](https://doi.org/10.1016/j.jcp.2021.110290).

Formal publisher/Crossref titles take precedence over title variations or typographical errors in secondary bibliography lists. Research summaries are short paraphrases of the papers' abstracts.

## Decisions and unresolved details

- The university profile inconsistently gives the current rank as assistant researcher and lecturer. Neither title is selected in the English CV or homepage; both identify the verified institution and department.
- Contact details use the current public university email. The personal mobile number and old university email from the Chinese CV are not included in the public version. The original Chinese CV is not redistributed.
- Degree specializations come from the original CV. Month-level dates come from the university profile; the July-August 2022 overlap is retained.
- The postdoctoral mentor's initials H. P. Zhang are used rather than assuming a preferred full-name romanization.
- The 72nd China Postdoctoral Science Foundation award is treated as the same one postdoctoral grant mentioned in the faculty profile, not a fourth principal-investigator grant. No award numbers, amounts, or missing dates were invented.
- English names of awards, workshops, and projects are descriptive translations where an official English label was not supplied. The Chinese names and dates in the user's original CV remain the source for those entries.
- The old CV's submitted proton-therapy title and two in-preparation titles are not separately counted as new publications. Their current status and relationship to later works would require confirmation from the author.
- The patent is identified as an application. No current examination status, authorization, or application number is asserted.
- No teaching appointments, courses, journal refereeing, or other claims were copied from the reference CV.

## Deployment and historical-file cleanup

The repository is owned by `zfc-2018`, so its project URL is `https://zfc-2018.github.io/zhangxj.github.io/`. Local resources and the CV link use relative paths.

This overlay package does not contain the previous owner's roughly 100 MB of unrelated assets. An overlay does not delete existing remote files. Before publishing, check and remove obsolete Yushun Zhang CVs, thesis, talks, and slides under `files/`; unrelated photos and logos under `images/`; `xueyao style.html`; the old Google verification file; and unused old deployment files, equation images, and `package-lock.json`. Preserve any original licenses that remain applicable.

No remote repository files or GitHub Pages settings were modified. The generated site needs neither Ruby nor a Jekyll build.
