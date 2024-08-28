import sys
sys.path.append('/home/vin/DSA/4_Trees')
module = __import__("2_contains")
BinarySearchTree = getattr(module, "BinarySearchTree")


class DFSPostOrder(BinarySearchTree):
    
    def dfs_post_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        
        traverse(self.root)
        return results


if __name__ == "__main__":
    my_tree = DFSPostOrder(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)

    print(my_tree.dfs_post_order())
    # [18, 27, 21, 52, 82, 76, 47]
    