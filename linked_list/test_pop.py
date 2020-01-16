import unittest
from list_preset import abc_list

testmap_pop = {
    0: 'b -> c -> ',
    1: 'a -> c -> ',
    2: 'a -> b -> '
}


class TestContainer(unittest.TestCase):
    pass


def test_pop(index, expected):
    def test(self):
        lst = abc_list()
        lst.pop_node(index)
        result = lst.__str__()
        self.assertEqual(result, expected)
    return test


if __name__ == '__main__':

    for index, expected in testmap_pop.items():
        test_func = test_pop(index, expected)
        setattr(TestContainer, f'test_{index}', test_func)

    unittest.main()
