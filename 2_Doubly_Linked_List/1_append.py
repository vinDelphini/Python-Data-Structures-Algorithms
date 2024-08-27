class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_dll_as_list(self):
        temp = self.head
        values = []
        while temp:
            values.append(temp.value)
            temp = temp.next
        print(values)

    def append(self, value):
        new_node = Node(value)
        temp = self.head
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1


dll = DoublyLinkedList(1)
dll.append(2)
dll.print_dll_as_list()
