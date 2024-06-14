class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = TreeNode(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = TreeNode(key)
            else:
                self._insert(root.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.val == key:
            return root

        if key < root.val:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.val:
            root.left = self._delete(root.left, key)
        elif key > root.val:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            min_larger_node = self._get_min(root.right)
            root.val = min_larger_node.val
            root.right = self._delete(root.right, min_larger_node.val)

        return root

    def _get_min(self, root):
        while root.left:
            root = root.left
        return root

    def inorder_traversal(self):
        return self._inorder_traversal(self.root, [])

    def _inorder_traversal(self, root, res):
        if root:
            self._inorder_traversal(root.left, res)
            res.append(root.val)
            self._inorder_traversal(root.right, res)
        return res

# Test the BST class
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print("Inorder traversal of the BST:", bst.inorder_traversal())

# Search for a value
print("Search for 40:", bst.search(40) is not None)

# Delete a value
bst.delete(20)
print("Inorder traversal after deleting 20:", bst.inorder_traversal())
bst.delete(30)
print("Inorder traversal after deleting 30:", bst.inorder_traversal())
bst.delete(50)
print("Inorder traversal after deleting 50:", bst.inorder_traversal())
