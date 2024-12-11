import nbformat

# Odczyt pliku .ipynb
with open('ZSŁ_NAI_lab2_huggingface_2024.ipynb', 'r', encoding='utf-8') as f:
    notebook = nbformat.read(f, as_version=4)

# Zapis zawartości komórek notebooka do pliku .txt
with open('output.txt', 'w', encoding='utf-8') as f:
    for cell in notebook['cells']:
        if cell['cell_type'] == 'markdown':
            f.write(cell['source'] + '\n\n')
        elif cell['cell_type'] == 'code':
            f.write(cell['source'] + '\n\n')