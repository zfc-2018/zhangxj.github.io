import { readFile, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const root = path.dirname(fileURLToPath(import.meta.url));
const profile = JSON.parse(await readFile(path.join(root, 'data/profile.json'), 'utf8'));
const publications = JSON.parse(await readFile(path.join(root, 'data/publications.json'), 'utf8'));
const escape = value => String(value).replace(/[&<>"']/g, char => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[char]);
const list = (items, className = '') => `<ul${className ? ` class="${className}"` : ''}>\n${items.map(item => `          <li>${item}</li>`).join('\n')}\n        </ul>`;
const entries = items => items.map(item => `<div class="entry"><div class="date">${escape(item.dates)}</div><div><p><strong>${escape(item.institution)}</strong></p>${item.details.map(detail => `<p>${escape(detail)}</p>`).join('')}</div></div>`).join('\n        ');
const renderPublication = paper => {
  if (new URL(paper.url).protocol !== 'https:') throw new Error(`Unsupported paper URL: ${paper.url}`);
  if (!paper.authors.includes(profile.name)) throw new Error(`Unrelated publication: ${paper.title}`);
  const authors = paper.authors.map(author => author === profile.name ? `<strong>${escape(author)}</strong>` : escape(author)).join(', ');
  return `<li class="publication">
            <p><a class="paper-title" href="${escape(paper.url)}">${escape(paper.title)}</a></p>
            <p class="authors">${authors}</p>
            <p class="venue"><em>${escape(paper.venue)}</em>, ${escape(paper.citation)}. <a href="${escape(paper.url)}">[${escape(paper.linkLabel)}]</a></p>
            <p class="paper-summary">${escape(paper.summary)}</p>${paper.note ? `\n            <p class="paper-note">${escape(paper.note)}</p>` : ''}
          </li>`;
};
const replacements = {
  ABOUT: `<p>${escape(profile.about).replace('Professor Min Tang', '<a href="https://ins.sjtu.edu.cn/people/mtang/">Professor Min Tang</a>')}</p>`,
  RESEARCH: list(profile.research.map(escape)),
  PUBLICATIONS: publications.map(renderPublication).join('\n          '),
  EMPLOYMENT: entries(profile.employment),
  EDUCATION: entries(profile.education),
  TEACHING: `<p><strong>${escape(profile.university)} (CSU)</strong></p>` + list(profile.teaching.map(course => `<strong>${escape(course.course)}</strong>, ${escape(course.level.toLowerCase())}, ${escape(course.semester)} semester, ${escape(course.year)}.`), 'teaching-list'),
  GRANTS: list(profile.grants.map(grant => `<strong>${escape(grant.title)}</strong><br><span class="small">${escape(grant.role)}${grant.dates ? '; ' + escape(grant.dates) : ''}</span>`), 'project-list'),
  AWARDS: list(profile.awards.map(award => `<span class="date">${escape(award.year)}</span> - ${escape(award.title)}`), 'honors'),
  TALKS: list(profile.talks.map(escape)),
  SERVICE: list(profile.service.map(escape)),
  PATENTS: profile.patents.map(item => `<p>${escape(item)}</p>`).join('\n')
};
let output = await readFile(path.join(root, 'index.template.html'), 'utf8');
for (const [key, value] of Object.entries(replacements)) {
  const marker = `<!-- ${key} -->`;
  if (output.split(marker).length !== 2) throw new Error(`Expected one ${key} marker`);
  output = output.replace(marker, () => value);
}
if (/[\u3400-\u9fff]/.test(output)) throw new Error('Non-English content remains in generated homepage');
await writeFile(path.join(root, 'index.html'), output, 'utf8');
console.log(`Built English Jemdoc-style homepage with ${publications.length} publications.`);
