from collections import deque


class _EmptyAVLNode:
    def __init__(self):
        self.key = None
        self.height = 0

    def insert(self, key):
        return _AVLNode(key)

    def delete(self, key):
        raise KeyError(key)

    def __bool__(self):
        """Empty node is always Falsy. """
        return False

    def __len__(self):
        return 0

    @property
    def balance_factor(self):
        return 0

    def __eq__(self, other):
        return isinstance(other, self.__class__)


class _AVLNode:
    def __init__(self, key=None):
        self.key = key
        self.left = _EmptyAVLNode()
        self.right = _EmptyAVLNode()
        self.height = 1

    def insert(self, key):
        if key > self.key:
            self.right = self.right.insert(key)
        elif key < self.key:
            self.left = self.left.insert(key)

        return self._balanced_tree()

    def delete(self, key):
        if key > self.key:
            self.right = self.right.delete(key)
        elif key < self.key:
            self.left = self.left.delete(key)
        else:
            if self.is_leaf():
                return _EmptyAVLNode()

            if self.left:
                new_key = self.left.find_max()
                self.key = new_key
                self.left = self.left.delete(new_key)
            else:
                new_key = self.right.key
                self.key = new_key
                self.right = self.right.delete(new_key)

        return self._balanced_tree()

    def clear(self):
        if self.is_leaf():
            return _EmptyAVLNode()
        self.left = self.left.clear()
        self.right = self.right.clear()

        return _EmptyAVLNode()

    def _balanced_tree(self):
        self.update_height()
        return self._balance_tree_if_unbalanced()

    def is_leaf(self):
        return not (bool(self.left) or bool(self.right))

    def find_max(self):
        max_key = self.key
        right_node = self.right
        while right_node:
            max_key = right_node.key
            right_node = right_node.right

        return max_key

    def find_min(self):
        min_key = self.key
        left_node = self.left
        while left_node:
            min_key = left_node.key
            left_node = left_node.left

        return min_key

    def update_height(self):
        self.height = 1 + max(self.left.height, self.right.height)

    def _balance_tree_if_unbalanced(self):
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
        return self.left.height - self.right.height

    def __bool__(self):
        """Returns True if the node is not None"""
        return self.key is not None

    def __len__(self):
        return 1 + len(self.left) + len(self.right)

    def __eq__(self, other):
        return self.key == other.key and self.left == other.left and self.right == other.right


class AVLTree:
    def __init__(self, keys=None):
        """Initialize an AVL Tree. """
        self.root = None
        self._init_tree(keys)

    def _init_tree(self, keys):
        self.root = _EmptyAVLNode()
        if keys is not None:
            try:
                for key in keys:
                    self.insert(key)
            except (ValueError, TypeError) as e:
                raise TypeError('AVLTree constructor called with '
                                f'incompatible data type: {e}')

    def __bool__(self):
        """Returns True if the tree is not empty"""
        return bool(self.root)

    def insert(self, elem):
        """T.insert(elem) -- insert elem"""
        self.root = self.root.insert(elem)

    def delete(self, elem):
        self.root = self.root.delete(elem)

    def __len__(self):
        return len(self.root)

    def __contains__(self, key):
        root = self.root

        while root:
            if key > root.key:
                root = root.right
            elif key < root.key:
                root = root.left
            else:
                return True

        return False

    def traverse(self, order='inorder'):
        """Traverse the tree based on a given strategy.

        order : 'preorder' | 'postorder' | 'bfs' | default 'inorder'
            The traversal of the tree.

            Use 'preorder' to print the root first, then left and right subtree, respectively.
            Use 'postorder' to print the left and right subree first, then the root.
            Use 'bfs' to visit the tree in a breadth-first manner.
            The default is 'inorder' which prints the left subtree, the root and the right subtree.

        """
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
        """Returns the height of the tree. When the tree is empty its height is zero."""
        return self.root.height

    def _inorder(self, root):
        if root:
            yield from self._inorder(root.left)
            yield root.key
            yield from self._inorder(root.right)

    def _preorder(self, root):
        if root:
            yield root.key
            yield from self._preorder(root.left)
            yield from self._preorder(root.right)

    def _postorder(self, root):
        if root:
            yield from self._postorder(root.left)
            yield from self._postorder(root.right)
            yield root.key

    def _bfs(self):
        root = self.root

        if root:
            q = deque()
            q.append(root)

            while q:
                root = q.popleft()
                yield root.key
                left = root.left
                right = root.right

                if left:
                    q.append(left)
                if right:
                    q.append(right)

    def find_max(self):
        return self.root.find_max()

    def find_min(self):
        return self.root.find_min()

    def __repr__(self):
        return f'AVLTree({list(self._bfs())})'

    def __str__(self):
        return repr(self)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.height == other.height and len(self) == len(other):
                return self.root == other.root
        return False

    def clear(self):
        self.root = self.root.clear()
