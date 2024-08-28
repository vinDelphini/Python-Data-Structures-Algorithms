import sys
sys.path.append("/home/vin/DSA/4_Trees")
module = __import__("2_contains")
BinarySearchTree = getattr(module, "BinarySearchTree")


class DFSInOrder(BinarySearchTree):

    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
            
        traverse(self.root)
        return results


if __name__ == "__main__":
    my_tree = DFSInOrder(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)

    print(my_tree.dfs_in_order())
    # [18, 21, 27, 47, 52, 76, 82]
    