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
            self.head = None
            self.tail = None

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        temp = self.head
        self.head = new_node
        new_node.next = temp
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None

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
        return temp

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index >= self.length or not isinstance(value, int):
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length - 1:
            return self.append(value)
        before_node = self.get(index - 1)
        new_node.next = before_node.next
        before_node.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index - 1)
        current_node = temp.next
        temp.next = current_node.next
        current_node.next = None
        self.length -= 1

    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head  # The head will become the new tail after reversal
        while current is not None:
            next_node = current.next  # Store the next node
            current.next = prev  # Reverse the current node's pointer
            prev = current  # Move prev to this node
            current = next_node  # Move to the next node in the original list
        self.head = prev  # After the loop, prev will be the new head


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.get_values_as_list()
linked_list.pop()
linked_list.get_values_as_list()
linked_list.prepend(0)
linked_list.get_values_as_list()
linked_list.pop_first()
linked_list.get_values_as_list()
print(linked_list.get(2).value)
# linked_list.set_value(2, 8)
linked_list.get_values_as_list()
linked_list.insert(1, 9)
linked_list.get_values_as_list()
linked_list.remove(1)
linked_list.get_values_as_list()
linked_list.reverse()
linked_list.get_values_as_list()
