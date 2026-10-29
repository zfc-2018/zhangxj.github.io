# Jemdoc Visual Reference

Reference: [Jin Shang's academic homepage](https://jshang2.github.io/), inspected October 29, 2026 through HTML, its stylesheet, Firecrawl branding/screenshot capture, and a directly inspected browser screenshot.

## Observed system

- Typography: `Georgia, serif`; browser-default 16px body text. The reference stylesheet specifies 165% h1 and 125% h2.
- Headings: blue `#527bbd`; links `#224b8d`.
- Sidebar: pale gray `#f6f6f6`, border `#dddddd`, compact grouped navigation.
- Main content: white background; title above a double gray rule; section headings above thin gray rules.
- Layout: `table#tlayout`, left `#layout-menu`, right `#layout-content`. Photo is placed beside contact information. Lists and numbered bibliographies carry the academic content.
- No cards, rounded panels, shadows, or large decorative hero graphics were observed.

The reference `jemdoc.css` is included directly. It is supplemented with `site.css` for readable photo sizing, focus indicators, anchor navigation, and mobile layouts. The supplied author's photo replaces the reference person's photo.

## Adaptations

The user's existing content remains on one page with sidebar anchors. On narrow screens the sidebar becomes a wrapped top navigation. This responsive behavior is an implementation choice; it was not inferred from the reference desktop screenshot.

The English CV independently follows the supplied PDF reference: A4, serif text, bold name and horizontal rule, compact labels in a left column, aligned institution/date rows, numbered papers, and two-page numbering. Times is used for a similar serif appearance; it is not the reference PDF's embedded Computer Modern font.
