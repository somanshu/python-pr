class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_right_subtree_index(arr):
    for i in range(1, len(arr)):
        if arr[i] > arr[0]:
            return i


def make_bst(inorder):
    if len(inorder) == 0:
        return None

    node = Node(inorder[0])

    if len(inorder) == 1:
        return node

    index = find_right_subtree_index(inorder)
    node.left = make_bst(inorder[1:index])
    node.right = make_bst(inorder[index:])
    return node


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return not len(self.items) > 0

    def top(self):
        return self.items[len(self.items) - 1]


def make_bst_using_stack(arr):
    root = Node(arr[0])

    stack = Stack()
    stack.push(root)

    for i in range(1, len(arr)):
        if arr[i] < stack.top().data:
            stack.top().left = Node(arr[i])
            stack.push(stack.top().left)
            continue

        item = None
        while (not stack.isEmpty() and stack.top().data < arr[i]):
            item = stack.pop()

        if item:
            item.right = Node(arr[i])
            stack.push(item.right)

    return root


arr = [10, 5, 1, 7, 40, 50]
# root = make_bst(arr)
root = make_bst_using_stack(arr)
print(root)
