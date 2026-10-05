import os
import shutil
import fitz

base_dir = r'C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental'
bib_dir = os.path.join(base_dir, '1_Bibliografia_Original')
txt_dir = os.path.join(base_dir, '2_Textos_Extraidos')

os.makedirs(bib_dir, exist_ok=True)
os.makedirs(txt_dir, exist_ok=True)

files_to_process = [
    ('Unidad 1 - Metodología de la investigación Cap. 7 (Hernández Sampieri, et al, 2008).pdf', 'U01_Sampieri_Cap7_Crudo.md'),
    ('Unidad 2 - Martin, 2008 Cap. 2.pdf', 'U02_Martin_Cap2_Crudo.md'),
    ('Unidad 2 - Martin, 2008 Cap. 7.pdf', 'U02_Martin_Cap7_Crudo.md'),
    ('Unidad 3 - Metodología de la investigación Cap. 9 (Hernández Sampieri, et al, 2008).pdf', 'U03_Sampieri_Cap9_Crudo.md'),
    ('Unidad 3 - Palencia  Ben, 2013.pdf', 'U03_Palencia-Ben_Crudo.md'),
    ('Unidad 4 - Metodología de la investigación Cap. 4 (Hernández Sampieri, et al, 2008).pdf', 'U04_Sampieri_Cap4_Crudo.md')
]

for pdf_name, md_name in files_to_process:
    pdf_path = os.path.join(base_dir, pdf_name)
    if not os.path.exists(pdf_path):
        print(f"Skipping {pdf_name}, not found.")
        continue
    
    new_pdf_path = os.path.join(bib_dir, pdf_name)
    shutil.move(pdf_path, new_pdf_path)
    print(f"Moved {pdf_name} to 1_Bibliografia_Original")
    
    md_path = os.path.join(txt_dir, md_name)
    
    try:
        doc = fitz.open(new_pdf_path)
        text = ""
        for page in doc:
            text += page.get_text() + '\n\n'
        
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Extracted text to {md_name}")
    except Exception as e:
        print(f"Failed to extract {pdf_name}: {e}")
