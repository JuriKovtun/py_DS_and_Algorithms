import unittest
from l_list import LinkedList


class TestContainer(unittest.TestCase):
    lst = LinkedList()

    def test_append_1(self):
        self.lst.append_node('a')
        self.assertEqual(self.lst.tail.value, 'a')

    def test_append_2(self):
        self.lst.append_node('b')
        self.assertEqual(self.lst.tail.value, 'a')
        self.assertEqual(self.lst.head.value, 'b')

    def test_append_3(self):
        self.lst.append_node('c')
        self.assertEqual(self.lst.tail.value, 'a')
        self.assertEqual(self.lst.head.value, 'c')


if __name__ == '__main__':
    unittest.main()
