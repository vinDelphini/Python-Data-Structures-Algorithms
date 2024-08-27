from hmac import new
from os import curdir
from re import S


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
        temp = self.root
        while temp:
            if value == temp.value:
                return False
            if value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            if value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def _contains(self, value):
        """This method search for value and returns True if value exists in
          the Tree, using a WHILE LOOP!!!"""
        temp = self.root
        if value == temp.value:
            return True
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def __r_contains(self, temp, value):
        """Helper function recursively moves left or right throgh the tree, 
        returns True if a match is found, else False"""
        if temp == None:
            return False
        if value == temp.value:
            return True
        if value < temp.value:
            return self.__r_contains(temp.left, value)
        if value > temp.value:
            return self.__r_contains(temp.right, value)
        
    def r_contains(self, value):
        """Takes a value to search through the tree and return True if contains
        else False, using RECURSIVE ALGORITHM!!!"""
        return self.__r_contains(self.root, value)


new_tree = BinarySearchTree(47)
new_tree.insert(21)
new_tree.insert(76)
new_tree.insert(18)
new_tree.insert(27)
new_tree.insert(52)
new_tree.insert(82)

print(new_tree._contains(23))
print(new_tree.r_contains(18))
