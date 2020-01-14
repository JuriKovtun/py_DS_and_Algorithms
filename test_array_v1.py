import unittest
import array_v1


class TestLinkedList(unittest.TestCase):

    def test_initail(self):
        lst = array_v1.LinkedList()
        self.assertIsNone(lst.head)
        self.assertIsNone(lst.tail)
        self.assertEqual(lst.length, 0)

    def test_append(self):
        lst = array_v1.LinkedList()
        lst.append_node(1)
        lst.append_node(2)
        lst.append_node('a')

        self.assertEqual(lst.tail.value, 1)
        self.assertEqual(lst.head.value, 'a')


if __name__ == '__main__':
    unittest.main()
