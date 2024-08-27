class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack_as_list(self):
        temp = self.top
        values = []
        while temp:
            values.append(temp.value)
            temp = temp.next
        print(values)

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        elif self.height == 1:
            self.top = None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
        self.height -= 1


my_stack = Stack(7)
my_stack.push(23)
my_stack.push(3)
my_stack.push(11)
my_stack.print_stack_as_list()

my_stack.pop()
my_stack.print_stack_as_list()
