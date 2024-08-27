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

    def get_values_as_list(self):
        temp = self.head
        values = []
        while temp is not None:
            values.append(temp.value)
            temp = temp.next
        print(values)

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        current_head = self.head
        self.head = new_node
        new_node.next = current_head
        self.length += 1
        return self.get_values_as_list()

    def pop_first(self):
        if self.length == 0:
            return None
        current_head = self.head
        self.head = self.head.next
        current_head.next = None
        return self.get_values_as_list()

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        if index < 0 or index >= self.length or not isinstance(value, int):
            return None
        temp = self.get(index)
        if temp:
            temp.value = value
        return self.get_values_as_list()

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index >= self.length or not isinstance(value, int):
            return None
        if index == 0:
            self.prepend(value)
        if index == self.length:
            self.append(value)
        else:
            before_node = self.get(index - 1)
            new_node.next = before_node.next
            before_node.next = new_node

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        before_node = self.get(index - 1)
        current_node = before_node.next
        before_node.next = current_node.next
        current_node.next = None
        self.length -= 1


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.get_values_as_list()
linked_list.prepend(0)
linked_list.pop_first()
print(linked_list.get(2).value)
linked_list.set_value(2, 8)
linked_list.insert(3, 9)
linked_list.get_values_as_list()
linked_list.remove(3)
linked_list.get_values_as_list()
