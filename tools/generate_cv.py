"""Build the English CV from the same data used by the website.

Requires reportlab and pypdf. Run: python tools/generate_cv.py [output.pdf]
"""
import json
import sys
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
PROFILE = json.loads((ROOT / 'data/profile.json').read_text(encoding='utf-8'))
PAPERS = json.loads((ROOT / 'data/publications.json').read_text(encoding='utf-8'))
DEST = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / 'files/Xiaojiang_Zhang_CV.pdf'
DEST.parent.mkdir(parents=True, exist_ok=True)

PAGE_W, PAGE_H = A4
MARGIN = 42.5
WIDTH = PAGE_W - 2 * MARGIN
LABEL_W = 73
CONTENT_W = WIDTH - LABEL_W
BODY = ParagraphStyle('Body', fontName='Times-Roman', fontSize=10.2, leading=12.3, spaceAfter=0)
SMALL = ParagraphStyle('Small', parent=BODY, fontSize=9.2, leading=11)
LABEL = ParagraphStyle('Label', parent=BODY, fontSize=8.8, leading=10.5)
DATE = ParagraphStyle('Date', parent=BODY, fontSize=9.6, alignment=TA_RIGHT)
NAME = ParagraphStyle('Name', parent=BODY, fontName='Times-Bold', fontSize=14, leading=17)
LINK_COLOR = '#224b8d'

def ascii_text(value):
    return str(value).replace('\u2013', '-').replace('\u2014', '-').replace('\u2019', "'").replace('\u00a0', ' ')

def safe(value):
    return escape(ascii_text(value))

def para(value, style=BODY):
    return Paragraph(value, style)

def link(url, label):
    return f'<link href="{escape(url, {chr(34): "&quot;"})}" color="{LINK_COLOR}">{safe(label)}</link>'

def section(label, content, gap=11):
    table = Table([[para(label.upper(), LABEL), content]], colWidths=[LABEL_W, CONTENT_W], hAlign='LEFT')
    table.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 0), ('TOPPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 0)]))
    return [table, Spacer(1, gap)]

def entry(item):
    # Keep the institution and date on the same baseline, as in the reference CV.
    header = Table([[para('<b>' + safe(item['institution']) + '</b>'), para(safe(item['dates']), DATE)]], colWidths=[CONTENT_W - 135, 135])
    header.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'), ('LEFTPADDING',(0,0),(-1,-1),0), ('RIGHTPADDING',(0,0),(-1,-1),0), ('TOPPADDING',(0,0),(-1,-1),0), ('BOTTOMPADDING',(0,0),(-1,-1),0)]))
    return [header] + [para(safe(text)) for text in item['details']] + [Spacer(1, 8)]

def bullet(text, number=None):
    marker = str(number) + '.' if number is not None else '\u2022'
    table = Table([[para(marker), para(text)]], colWidths=[14, CONTENT_W - 14])
    table.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'), ('LEFTPADDING',(0,0),(-1,-1),0), ('RIGHTPADDING',(0,0),(-1,-1),0), ('TOPPADDING',(0,0),(-1,-1),0), ('BOTTOMPADDING',(0,0),(-1,-1),0)]))
    return [table, Spacer(1, 6)]

def footer(canvas, document):
    canvas.saveState()
    canvas.setFont('Times-Roman', 9)
    canvas.drawString(MARGIN, 23, f'{document.page} of 2')
    canvas.setFont('Times-Roman', 8)
    canvas.drawRightString(PAGE_W - MARGIN, 23, 'Updated ' + PROFILE['updated'])
    canvas.restoreState()

story = [para(safe(PROFILE['name']), NAME), Spacer(1, 5), HRFlowable(width='100%', thickness=.8, color=colors.black), Spacer(1, 12)]
contact = [
    para(safe(PROFILE['department'])),
    para(safe(PROFILE['university']) + ', ' + safe(PROFILE['location'])),
    para('E-mail: ' + link('mailto:' + PROFILE['email'], PROFILE['email'])),
    para('Website: ' + link(PROFILE['website'], PROFILE['website'].replace('https://', '').rstrip('/')))
]
story += section('Contact<br/>Information', contact, 13)
employment = []
for item in PROFILE['employment']:
    employment += entry(item)
story += section('Employment', employment, 3)
education = []
for item in PROFILE['education']:
    education += entry(item)
story += section('Education', education, 3)
story += section('Research<br/>Interests', [para('; '.join(safe(x).rstrip('.') for x in PROFILE['research']) + '.')], 12)

publications = []
for i, paper in enumerate(PAPERS, 1):
    authors = ', '.join('<b>' + safe(a) + '</b>' if a == PROFILE['name'] else safe(a) for a in paper['authors'])
    citation = f'{authors}. {safe(paper["title"])}. <i>{safe(paper["venue"])}</i>, {safe(paper.get("cvCitation", paper["citation"]))}. '
    citation += link(paper['url'], '[' + paper['linkLabel'] + ']')
    publications += bullet(citation, i)
story += section('Publications<br/>and Accepted<br/>Papers', publications, 0)
story.append(PageBreak())

teaching = [para('<b>' + safe(PROFILE['university']) + ' (CSU)</b>'), Spacer(1, 5)]
for course in PROFILE['teaching']:
    text = '<b>' + safe(course['course']) + '</b>, ' + safe(course['level'].lower()) + ', ' + safe(course['semester']) + ' semester, ' + safe(course['year']) + '.'
    teaching += bullet(text)
story += section('Teaching<br/>Experience', teaching, 11)

grants = []
for grant in PROFILE['grants']:
    text = safe(grant['title']) + '. <i>' + safe(grant['role']) + '</i>'
    if grant['dates']:
        text += ', ' + safe(grant['dates'])
    grants += bullet(text + '.')
story += section('Grants and<br/>Projects', grants, 11)

awards = []
for award in PROFILE['awards']:
    row = Table([[para('\u2022'), para(safe(award['title'])), para(safe(award['year']), DATE)]], colWidths=[14, CONTENT_W - 49, 35])
    row.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)]))
    awards += [row, Spacer(1,5)]
story += section('Honors and<br/>Awards', awards, 11)

talks = []
for talk in PROFILE['talks']:
    talks += bullet(safe(talk))
story += section('Talks', talks, 11)
service = []
for item in PROFILE['service']:
    service += bullet(safe(item))
story += section('Professional<br/>Service', service, 11)
story += section('Patent<br/>Application', [para(safe(PROFILE['patents'][0]))], 0)

document = SimpleDocTemplate(str(DEST), pagesize=A4, rightMargin=MARGIN - 6, leftMargin=MARGIN - 6, topMargin=34, bottomMargin=43, title='Xiaojiang Zhang - Curriculum Vitae', author='Xiaojiang Zhang', pageCompression=1)
document.build(story, onFirstPage=footer, onLaterPages=footer)
reader = PdfReader(str(DEST))
assert len(reader.pages) == 2, f'Expected two CV pages, got {len(reader.pages)}'
assert all(page.extract_text().strip() for page in reader.pages)
print(f'Created two-page English CV: {DEST}')
