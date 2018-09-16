class _AvlNode:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

    def insert(self, key):
        if self.key is None:
            self.key = key
            return self
        elif key > self.key:
            if self.right is None:
                self.right = _AvlNode(key)
            else:
                self.right = self.right.insert(key)
        elif key <= self.key:
            if self.left is None:
                self.left = _AvlNode(key)
            else:
                self.left = self.left.insert(key)
        else:
            raise RuntimeError

        self.update_height()
        return self._new_root_if_umbalanced()

    def update_height(self):
        left_height = self.left.height if self.left is not None else 0
        right_height = self.right.height if self.right is not None else 0
        self.height = 1 + max(left_height, right_height)

    def _new_root_if_umbalanced(self):
        if self.balance_factor == 2 and self.left.balance_factor == -1:
            return self.rotate_left_right()
        elif self.balance_factor == -2 and self.right.balance_factor == 1:
            return self.rotate_right_left()
        elif self.balance_factor == -2:
            return self.rotate_left()
        elif self.balance_factor == 2:
            return self.rotate_right()
        else:
            return self

    def rotate_left(self):
        right_tree = self.right
        self.right = right_tree.left
        right_tree.left = self

        self.update_height()
        right_tree.update_height()

        return right_tree

    def rotate_right(self):
        left_tree = self.left
        self.left = left_tree.right
        left_tree.right = self

        self.update_height()
        left_tree.update_height()

        return left_tree

    def rotate_left_right(self):
        self.left = self.left.rotate_left()
        return self.rotate_right()

    def rotate_right_left(self):
        self.right = self.right.rotate_right()
        return self.rotate_left()

    @property
    def balance_factor(self):
        left_height = self.left.height if self.left is not None else 0
        right_height = self.right.height if self.right is not None else 0
        return left_height - right_height


class AVLTree:
    def __init__(self):
        self.root = _AvlNode()

    def empty(self):
        return self.root.key is None

    def insert(self, elem):
        self.root = self.root.insert(elem)

    def traverse(self, order='inorder'):
        if order == 'preorder':
            return self._preorder(self.root)
        elif order == 'postorder':
            return self._postorder(self.root)
        else:
            return self._inorder(self.root)

    def _inorder(self, root):
        if root is not None:
            yield from self._inorder(root.left)
            yield root.key
            yield from self._inorder(root.right)

    def _preorder(self, root):
        if root is not None:
            yield root.key
            yield from self._preorder(root.left)
            yield from self._preorder(root.right)

    def _postorder(self, root):
        if root is not None:
            yield from self._postorder(root.left)
            yield from self._postorder(root.right)
            yield root.key

