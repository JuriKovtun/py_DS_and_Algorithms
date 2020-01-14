import unittest
import l_list_v1


class TestLinkedList(unittest.TestCase):

    def abc_list(self):
        lst = l_list_v1.LinkedList()
        for e in 'abc':
            lst.append_node(e)
        return lst

    # pop_case = {
    #     0: 'b -> c -> ',
    #     1: 'a -> c -> ',
    #     2: 'a -> b -> '
    # }

    def test_1_append(self):
        lst = self.abc_list()
        self.assertEqual(lst.tail.value, 'a')
        self.assertEqual(lst.head.value, 'c')

    def test_2_print(self):
        lst = self.abc_list()
        expected = 'a -> b -> c -> '
        result = lst.__str__()
        self.assertEqual(result, expected)

    def test_3_pop0(self):
        lst = self.abc_list()
        lst.pop_node(0)
        expected = 'b -> c -> '
        result = lst.__str__()
        self.assertEqual(result, expected)

    def test_3_pop1(self):
        lst = self.abc_list()
        lst.pop_node(1)
        expected = 'a -> c -> '
        result = lst.__str__()
        self.assertEqual(result, expected)

    def test_3_pop2(self):
        lst = self.abc_list()
        lst.pop_node(2)
        expected = 'a -> b -> '
        result = lst.__str__()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
