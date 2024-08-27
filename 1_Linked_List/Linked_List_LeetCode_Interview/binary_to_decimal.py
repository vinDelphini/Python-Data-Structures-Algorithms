class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1

    def print_list(self):
        if self.head is None:
            print("empty list")
        else:
            temp = self.head
            values = []
            while temp is not None:
                values.append(str(temp.value))
                temp = temp.next
            print(" -> ".join(values))

    def binary_to_decimal(self):
        decimal = 0
        counter = self.length - 1
        temp = self.head
        for _ in range(self.length):
            decimal += temp.value * (2 ** counter)
            temp = temp.next
            counter -= 1
        return decimal

    def getDecimalValue(self):
        decimal = 0
        temp = self.head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        print(length)

# Test case 1: Binary number 110 = Decimal number 6
linked_list = LinkedList(1)
linked_list.append(1)
linked_list.append(0)
result = linked_list.getDecimalValue()
