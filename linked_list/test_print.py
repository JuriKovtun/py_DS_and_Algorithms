import unittest
from l_list import LinkedList
from list_preset import abc_list


class TestContainer(unittest.TestCase):

    def test_1(self):
        lst = abc_list()
        expected = 'a -> b -> c -> '
        result = lst.__str__()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
