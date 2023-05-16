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
        print(file_out, file=sys.stdout)



def remove(instance):
    if instance.__len__() == 0:
        print('Não há elementos', file=sys.stdout)
        return None

    file_process = instance.dequeue()
    path_file = file_process['nome_do_arquivo']
    print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)
    


def file_metadata(instance, position):
    
