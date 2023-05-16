from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def enqueue(self, value):
        self.list.append(value)

    def dequeue(self):
        if self.__len__() != 0:
            return self.list.pop(0)
        raise Exception("Lista Vazia")

    def search(self, index):
        if len(self.list) > index >= 0:
            return self.list[index]
        raise IndexError('Índice Inválido ou Inexistente')
