from ting_file_management.priority_queue import PriorityQueue
import pytest

mock = [
    {
        "nome_do_arquivo": "file1.txt",
        "qtd_linhas": 10,
    },
    {
        "nome_do_arquivo": "file2.txt",
        "qtd_linhas": 4,
    },
    {
        "nome_do_arquivo": "file3.txt",
        "qtd_linhas": 7,
    },
    {
        "nome_do_arquivo": "file3.txt",
        "qtd_linhas": 3,
    }
]


def test_basic_priority_queueing():
    instance = PriorityQueue()

    assert instance.is_priority(mock[0]) is False
    assert instance.is_priority(mock[1]) is True
    assert instance.is_priority(mock[2]) is False
    assert instance.is_priority(mock[3]) is True

    instance.enqueue(mock[0])
    instance.enqueue(mock[1])
    instance.enqueue(mock[2])
    instance.enqueue(mock[3])
        
    assert len(instance.high_priority) == 2
    assert len(instance.regular_priority) == 2

    assert instance.search(0) == mock[1]

    instance.dequeue()
    assert len(instance.high_priority) == 1
    assert len(instance.regular_priority) == 2

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        instance.search(99)
