import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance):
    file = txt_importer(path_file)
    file_out = create_file_out(path_file)

    if path_file not in instance.list:
        instance.enqueue(path_file)
        print(file_out, file=sys.stdout)


def remove(instance):
    if instance.__len__() == 0:
        print('Não há elementos', file=sys.stdout)
        return None

    path_file = instance.dequeue()
    print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)    


def file_metadata(instance, position):
    if position < 0 or position > instance.__len__():
        print("Posição inválida", file=sys.stderr)
        return None

    file_element = instance.search(position)
    file_out = create_file_out(file_element)

    print(file_out, file=sys.stdout)


def create_file_out(path_file):
    file = txt_importer(path_file)
    file_out = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file
    }

    return file_out