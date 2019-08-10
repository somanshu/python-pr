# Diameter of a Binary Tree in O(n)
class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def diameter(node):
    height_left = 0
    d_left = 0
    height_right = 0
    d_right = 0

    if node.right != None:
        (h_right, d_right) = diameter(node.right)
        height_right = 1 + h_right

    if node.left != None:
        (h_left, d_left) = diameter(node.left)
        height_left = 1 + h_left

    return (max(height_left, height_right), max(d_left, d_right, height_left + height_right + 1))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
(height, diaMeter) = diameter(root)
print(f'height -> {height}')
print(f'diameter -> {diaMeter}')
