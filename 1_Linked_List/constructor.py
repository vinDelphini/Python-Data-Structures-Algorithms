class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self, value):
        """initialize new linked list"""
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        """create new node 
        and then add node to end"""

    def prepend(self, value):
        """create new node
        and then add that node to the beginning"""

    def insert(self, value):
        """create new node
        and insert node"""


if __name__=="__main__":
    my_linked_list = LinkedList(4)
    print(my_linked_list.head.value)