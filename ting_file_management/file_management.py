import os
import sys


def txt_importer(path_file):
    name_arq = os.path.basename(path_file)
    ext = os.path.splitext(name_arq)
    
    if ext[1] != '.txt':
        print('Formato inválido', file=sys.stderr)
    
    try:
        with open(path_file, "r") as file:
            return file.read().split('\n')
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)


pa = 'requirements.txt'
print(txt_importer(pa))