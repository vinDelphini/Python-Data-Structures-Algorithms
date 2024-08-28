import sys
sys.path.append('/home/vin/DSA/4_Trees')
module = __import__("2_contains")
BinarySearchTree = getattr(module, "BinarySearchTree")

# from 2_contains import BinarySearchTree #type: ignore

class EBFS(BinarySearchTree):

    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results


if __name__ == "__main__":
    my_tree = EBFS(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)

    print(my_tree.BFS())
    # [47, 21, 76, 18, 27, 52, 82]
    