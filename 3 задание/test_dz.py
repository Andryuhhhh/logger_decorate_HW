import os

from logger import logger


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.outer = 0
        self.inner = -1
        return self

    @logger('next_calls.log')
    def __next__(self):
        self.inner += 1

        while self.outer < len(self.list_of_list) and self.inner >= len(self.list_of_list[self.outer]):
            self.outer += 1
            self.inner = 0

        if self.outer >= len(self.list_of_list):
            raise StopIteration

        return self.list_of_list[self.outer][self.inner]


def test_1():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)


    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

if __name__ == '__main__':
    test_1()