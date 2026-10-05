import os
import fitz

base_dir = r'C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\Parcial 1 - Actividad 1'

pdfs = [
    'Benitez et al., 2018.pdf',
    'Figueroa et al., 2019.pdf',
    'Lorca  Angulo, 2018.pdf',
    'Michelini et al., 2015.pdf',
    'Muñoz-Suazo et al., 2019.pdf',
    'Ramírez et al., 2018.pdf'
]

for pdf in pdfs:
    pdf_path = os.path.join(base_dir, pdf)
    md_path = os.path.join(base_dir, pdf.replace('.pdf', '.md'))
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text() + '\n\n'
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Extracted {pdf}")
    except Exception as e:
        print(f"Error on {pdf}: {e}")
