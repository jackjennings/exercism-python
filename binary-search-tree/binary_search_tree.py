class TreeNode(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)

    def insert(self, value):
        if self.data is None:
            self.data = value
        elif int(value) <= int(self.data):
            if self.left is None:
                self.left = TreeNode(value, None, None)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value, None, None)
            else:
                self.right.insert(value)

    def sorted_data(self):
        parts = []

        if self.left:
            parts.extend(self.left.sorted_data())

        if self.data:
            parts.append(self.data)

        if self.right:
            parts.extend(self.right.sorted_data())

        return parts

class BinarySearchTree(object):
    def __init__(self, tree_data):
        self.root = TreeNode(None, None, None)
        for value in tree_data:
            self.root.insert(value)

    def data(self):
        return self.root

    def sorted_data(self):
        return self.root.sorted_data()
