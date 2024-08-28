class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:

    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        values = []
        while temp:
            values.append(temp.value)
            temp = temp.next
        print(values)

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1


my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.print_queue()
