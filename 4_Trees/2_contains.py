class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self, value):
        new_node = Node(value)
        self.root = new_node

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while temp:
            if new_node.value == temp.value:
                return False
            if value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False


if __name__ == "__main__":
    new_tree = BinarySearchTree(47)
    new_tree.insert(21)
    new_tree.insert(76)
    new_tree.insert(18)
    new_tree.insert(27)
    new_tree.insert(52)
    new_tree.insert(82)

    print(new_tree.contains(27))
    print(new_tree.contains(17))
