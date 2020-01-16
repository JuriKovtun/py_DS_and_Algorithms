from l_list import LinkedList


def abc_list():
    lst = LinkedList()
    for e in 'abc':
        lst.append_node(e)
    return lst
