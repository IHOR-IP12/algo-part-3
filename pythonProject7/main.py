class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None                                                                                                #дерево є ще пустим

def invert_binary_tree(tree) -> BinaryTree:
    if tree is None:
        return None

    tree.left, tree.right = tree.right, tree.left                                                                             #інверсія

    invert_binary_tree(tree.right)
    invert_binary_tree(tree.left)                                                                                             #рекурсія


    return tree
root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)

inverted_tree = invert_binary_tree(root)
def print_tree(tree):
    if tree:
        print(tree.value)
        print_tree(tree.left)
        print_tree(tree.right)

print_tree(inverted_tree)



