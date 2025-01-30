'''
JARILLA, ANGELO CHRISTIENE M.
4) Trees:
In Trees, there is a primary node which is called a root and, in those roots, there are branches. Trees are a unique kind of graph. Although a tree's nodes can have several children, there is only one path connecting any two of them. Trees are frequently found in organization charts, file systems, and search techniques like binary search trees.
'''


class TreeNode:
    def __init__(self, DataVal):
        self.data = DataVal
        self.Kaliwa = None
        self.Kanan = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, DataVal):
        if not self.root:
            self.root = TreeNode(DataVal)
        else:
            self.add(self.root, DataVal)

    def add(self, node, DataVal):
        if DataVal < node.data:
            if node.Kaliwa is None:
                node.Kaliwa = TreeNode(DataVal)
            else:
                self.add(node.Kaliwa, DataVal)
        else:
            if node.Kanan is None:
                node.Kanan = TreeNode(DataVal)
            else:
                self.add(node.Kanan, DataVal)

    def show(self, node):
        if node:
            self.show(node.Kaliwa)
            print(node.data, end=" ")
            self.show(node.Kanan)


trees = BinaryTree()
trees.insert(50)
trees.insert(30)
trees.insert(70)
trees.insert(20)
trees.insert(40)
trees.show(trees.root)
print()

#Sorry for the CamelCase