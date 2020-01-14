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
        if self.tail:
            if self.head:
                self.head.next_node = new_node
                self.head = new_node
            else:
                self.tail.next_node = new_node
                self.head = new_node

        else:
            self.tail = new_node

    def get_node(self, index):
        node = self.tail
        if index == 0:
            return node.value
        elif index >= self.length:
            print('index out of range')
            return None
        else:
            for _ in range(index):
                node = node.next_node
            return node.value

    def pop_node(self, index):
        if index == 0:
            self.tail = self.tail.next_node
        elif index >= self.length:
            print('index out of range')
            return None
        else:
            node = self.tail
            for _ in range(index - 1):
                node = node.next_node
            node.next_node = node.next_node.next_node
            # node.next_node.next_node = None
        self.length -= 1

    def print_list(self):
        node = self.tail
        for _ in range(self.length):
            print(node.value)
            node = node.next_node


foo = LinkedList()
foo.append_node(1)
foo.append_node(2)
foo.append_node("a")
foo.append_node(4)
foo.append_node(5)


foo.print_list()
foo.pop_node(5)
print('new list:')
foo.print_list()
