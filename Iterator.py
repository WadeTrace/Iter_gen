class FlatIterator:

    def __init__(self, list_of_list):
        self.result_list = []
        [[self.result_list.append(x) for x in list_] for list_ in list_of_list]

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n == len(self.result_list):
            raise StopIteration
        self.n += 1
        return self.result_list[self.n-1]

def test_1():

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