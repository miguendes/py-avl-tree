from collections import deque


class _EmptyAVLNode:
    def __init__(self):
        self.height = 0

    def insert(self, key):
        return _AVLNode(key)

    @property
    def empty(self):
        return True

    @property
    def balance_factor(self):
        return 0


class _AVLNode:
    def __init__(self, key=None):
        self.key = key
        self.left = _EmptyAVLNode()
        self.right = _EmptyAVLNode()
        self.height = 1

    def insert(self, key):
        if self.key is None:
            self.key = key
        elif key > self.key:
            self.right = self.right.insert(key)
        elif key < self.key:
            self.left = self.left.insert(key)

        self.update_height()
        return self._new_root_if_unbalanced()

    def _left_right_heights(self):
        return self.left.height, self.right.height

    def update_height(self):
        left_height, right_height = self._left_right_heights()
        self.height = 1 + max(left_height, right_height)

    def _new_root_if_unbalanced(self):
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
        left_height, right_height = self._left_right_heights()
        return left_height - right_height

    @property
    def empty(self):
        return self.key is None


class AVLTree:
    def __init__(self):
        self.root = _AVLNode()

    def empty(self):
        return self.root.key is None

    def insert(self, elem):
        self.root = self.root.insert(elem)

    def traverse(self, order='inorder'):
        if order == 'preorder':
            return self._preorder(self.root)
        elif order == 'postorder':
            return self._postorder(self.root)
        elif order == 'bfs':
            return self._bfs()
        else:
            return self._inorder(self.root)

    @property
    def height(self):
        return self.root.height

    def _inorder(self, root):
        if not root.empty:
            yield from self._inorder(root.left)
            yield root.key
            yield from self._inorder(root.right)

    def _preorder(self, root):
        if not root.empty:
            yield root.key
            yield from self._preorder(root.left)
            yield from self._preorder(root.right)

    def _postorder(self, root):
        if not root.empty:
            yield from self._postorder(root.left)
            yield from self._postorder(root.right)
            yield root.key

    def _bfs(self):
        root = self.root

        if not root.empty:
            q = deque()
            q.append(root)

            while q:
                root = q.popleft()
                yield root.key
                left = root.left
                right = root.right

                if not left.empty:
                    q.append(left)
                if not right.empty:
                    q.append(right)
