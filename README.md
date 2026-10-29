# Xiaojiang Zhang - English Academic Homepage

An English homepage and English academic CV for [zfc-2018/zhangxj.github.io](https://github.com/zfc-2018/zhangxj.github.io).

The visual style follows the classic [Jemdoc academic homepage](https://jshang2.github.io/): Georgia/serif text, blue section headings, thin gray rules, and a pale gray navigation sidebar. The original reference stylesheet is included as `jemdoc.css`, with a small responsive layer in `site.css`.

Expected project URL: <https://zfc-2018.github.io/zhangxj.github.io/>. The generated homepage and the CV are already included, so deployment does not require installing any tools.

## Publish

Copy the contents of this folder into the target repository root, including `.nojekyll`, and commit them. In GitHub Settings > Pages, select Deploy from a branch, `master`, `/ (root)`.

This is an overlay package. It does not delete old files already in the remote repository. Remove the previous owner's unrelated CVs, talks, photos, verification file, and alternate HTML pages after checking the cleanup notes in `MIGRATION.md`.

## Edit the content

| Content | File |
| --- | --- |
| Biography, employment, education, teaching, interests, grants, awards, talks, service, patent | `data/profile.json` |
| Publications and English research summaries | `data/publications.json` |
| Page layout and static contact header | `index.template.html` |
| Classic Jemdoc stylesheet | `jemdoc.css` |
| Responsive adjustments | `site.css` |
| Photo | `images/zhang-xiaojiang.png` |
| English CV | `files/Xiaojiang_Zhang_CV.pdf` |
| Reproducible CV source | `tools/generate_cv.py` |

Build the homepage with Node.js 18 or later:

```sh
node build.mjs
```

Rebuild the CV with Python after installing its two dependencies:

```sh
python -m pip install -r requirements.txt
python tools/generate_cv.py
```

The default CV destination is `files/Xiaojiang_Zhang_CV.pdf`. Commit both the regenerated HTML and PDF after changing the data. Keep the contact header in `index.template.html` consistent if changing the name, institution, or email.

The HTML is generated with a small local Node script using the Jemdoc visual system; it is not compiled by the historical jemdoc Python generator. `index.jemdoc` points to the maintained sources so an old build command does not silently restore the previous owner's profile.

The English CV follows the supplied reference PDF's two-page academic layout: name and horizontal rule, left-column section labels, serif body text, numbered publications, and page numbering. The reference person's biography and claims have not been reused.

Source decisions and limits are documented in `MIGRATION.md`; design evidence is in `DESIGN.md`. This delivery has not been pushed to GitHub and has not changed Pages settings.
