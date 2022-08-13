# Binary Tree
class Tree:
    def __init__(self, data):
        self.data = data

        # Pointers left and right for storing address
        self.left = None
        self.right = None

    # Method for inserting Node
    def insert(self, val):
        # Checks if data is not None
        if self.data:

            # checks if data value is greater than argument
            if self.data > val:

                # checks if left pointer is not None
                if self.left is None:

                    # Assigns a left pointer with Node
                    self.left = Tree(val)

                else:
                    # Inserts into left pointers // Recursion
                    self.left.insert(val)

            # checks if data value is less than argument
            if self.data < val:

                # checks if right pointer is not None
                if self.right is None:
                    # Assigns a left pointer with Node
                    self.right = Tree(val)
                else:
                    # inserts into right Node // Recursion
                    self.right.insert(val)

        # if there is no root node
        else:
            self.data = val

    # displaying data
    def printTree(self):
        res = []
        # checks if data exist
        if self.data:
            # checks if left pointer is not None
            if self.left is not None:
                res = res + self.left.printTree()

            res.append(self.data)

            # checks if right pointer is not None
            if self.right is not None:
                res = res + self.right.printTree()

        return res

    # Traversal Method 1
    def inorder(self, root):
        # Init empty array
        res = []

        # if root exists
        if root:
            res = self.inorder(root.left)
            res.append(root.data)
            res = res + self.inorder(root.right)
        return res

    def postorder(self, root):
        res = []

        if root:
            res = res + self.preorder(root.left)
            res = res + self.preorder(root.right)
            res.append(root.data)
        return res

    def preorder(self, root):
        res = []

        if root:
            res.append(root.data)
            res = res + self.preorder(root.left)
            res = res + self.preorder(root.right)
        return res

    def dictTraverse(self, root):
        dt = {}

        dt["Normal"] = self.printTree()
        dt["In Order"] = self.inorder(root)
        dt["Post Order"] = self.postorder(root)
        dt["Pre Order"] = self.preorder(root)

        return dt

    def search_node(self, root, val):
        if root is None or root.data == val:
            return root

        if root.data < val:
            return self.search_node(root.right, val)

        return self.search_node(root.left, val)

    def left_most_node(self, root):
        current = root

        while current.left is not None:
            current = current.left

        return current

    def right_most_node(self, root):
        current = root

        while current.right is not None:
            current = current.right
        return current



tree = Tree(10)

tree.insert(45)
tree.insert(2)
tree.insert(3)
tree.insert(46)
tree.insert(1)
tree.insert(70)

print(tree.dictTraverse(tree))
