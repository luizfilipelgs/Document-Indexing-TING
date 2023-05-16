import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue



def process(path_file, instance):
    file = txt_importer(path_file)
    file_out = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file
    }

    if path_file not in instance.list:
        instance.enqueue(path_file)
        sys.stdout.write(str(file_out))



def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
