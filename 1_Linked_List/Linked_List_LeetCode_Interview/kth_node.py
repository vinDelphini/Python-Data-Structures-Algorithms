class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

# for i in range k:
#     if fast pointer is None:
#         return None (list is shorter than k)
#     move fast pointer to the next node
#
# while fast pointer is not None:
#     move slow pointer to the next node
#     move fast pointer to the next node
# return the slow pointer (k-th node from the end)


def find_kth_from_end(ll, k):
    slow = fast = ll.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

k = 1
print(find_kth_from_end(my_linked_list, k).value)
# Output: 4

"""
    EXPECTED OUTPUT:
    ----------------
    4

"""
