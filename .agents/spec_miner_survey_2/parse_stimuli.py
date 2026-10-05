import zipfile
import xml.etree.ElementTree as ET
import json
import os
import sys

docx_path = r"C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\Noticias\NOTICIAS TRADUCIDAS.docx"
img_dir = r"C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\Noticias\noticias imagenes"

with zipfile.ZipFile(docx_path) as docx:
    tree = ET.fromstring(docx.read('word/document.xml'))

ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
body = tree.find('.//w:body', ns)

sections = []
current_section = None

for child in body:
    tag = child.tag.split('}')[-1]
    if tag == 'p':
        text = ''.join(child.itertext()).strip()
        if text:
            current_section = text
    elif tag == 'tbl':
        rows = child.findall('.//w:tr', ns)
        table_data = []
        for r in rows:
            cells = [''.join(c.itertext()).strip() for c in r.findall('.//w:tc', ns)]
            table_data.append(cells)
        sections.append((current_section, table_data))

items = []
for sec_title, tbl in sections:
    headers = tbl[0]
    for row in tbl[1:]:
        sec_num, eng, esp, internal_num = row
        int_id = int(internal_num)
        
        # image filename check
        jpg_name = f"Noticia_{int_id:02d}.jpg"
        png_name = f"Noticia_{int_id:02d}.png"
        if os.path.exists(os.path.join(img_dir, jpg_name)):
            img_file = jpg_name
        elif os.path.exists(os.path.join(img_dir, png_name)):
            img_file = png_name
        else:
            img_file = "MISSING"
            
        items.append({
            'id': int_id,
            'sec_num': int(sec_num),
            'section': sec_title,
            'english': eng,
            'spanish': esp,
            'image_file': img_file
        })

items.sort(key=lambda x: x['id'])

with open('stimuli_parsed.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, indent=2, ensure_ascii=False)

print(f"Extracted {len(items)} stimuli to stimuli_parsed.json successfully.")
