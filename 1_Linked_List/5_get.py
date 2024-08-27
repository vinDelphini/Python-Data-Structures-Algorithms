class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            pre = self.tail
            while temp.next is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        current_head = self.head
        self.head = new_node
        new_node.next = current_head
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        current_head = self.head
        self.head = self.head.next
        current_head.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        print(temp.value)


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.print_list()
print("------pop-------")
linked_list.pop()
linked_list.print_list()
print("----prepend-----")
linked_list.prepend(3)
linked_list.print_list()
print("----pop_first---")
linked_list.pop_first()
linked_list.print_list()
print("----get---------")
linked_list.get(1)
