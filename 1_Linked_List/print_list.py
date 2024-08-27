# to print all of the values in a linked list
from constructor import LinkedList

my_linked_list_2 = LinkedList(8)

def print_list():
    temp = my_linked_list_2.head

    while temp is not None:
        print(temp.value)
        temp = temp.next


if __name__=="__main__":
    print_list()
