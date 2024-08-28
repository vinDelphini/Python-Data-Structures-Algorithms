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


new_stack = Stack(1)
new_stack.push(2)

new_stack.print_stack_as_list()
