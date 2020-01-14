class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append_node(self, value):
        self.length += 1
        new_node = Node(value)

        if not self.tail:
            self.tail = new_node
            return

        if self.head:
            self.head.next_node = new_node
            self.head = new_node
        else:
            self.tail.next_node = new_node
            self.head = new_node

    def get_node(self, index):
        self._check_index(index)
        return self._select_node(index).value

    def pop_node(self, index):
        self._check_index(index)

        self.length -= 1
        node = self._select_node(index - 1)
        if node.next_node:
            node.next_node = node.next_node.next_node
        else:
            self.tail = self.tail.next_node

    def _select_node(self, index):
        node = self.tail
        while index > 0:
            node = node.next_node
            index -= 1
        return node

    def _check_index(self, index):
        error = index >= self.length
        if error:
            raise IndexError('index out of range')

    def __str__(self):
        s = ""
        node = self.tail
        while node:
            s += str(node.value) + ' -> '
            node = node.next_node
        return s


lst = LinkedList()
lst.append_node(1)
lst.append_node(2)
lst.append_node("a")

print(lst.head.value)

# foo.pop_node(0)
# print(foo)
# foo.pop_node(0)
# print(foo)
# foo.pop_node(0)
# print(foo)
