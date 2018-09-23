from collections import deque


class _EmptyAVLNode:
    def __init__(self):
        self.entry = None
        self.height = 0

    def insert(self, entry):
        return _AVLNode(entry)

    def delete(self, entry):
        raise KeyError(entry)

    @property
    def balance_factor(self):
        return 0

    def __bool__(self):
        """Empty node is always Falsy. """
        return False

    def __len__(self):
        return 0

    def __eq__(self, other):
        return isinstance(other, self.__class__)


class _AVLNode:
    def __init__(self, entry=None):
        self.entry = entry
        self.left = _EmptyAVLNode()
        self.right = _EmptyAVLNode()
        self.height = 1

    def insert(self, entry):
        if entry > self.entry:
            self.right = self.right.insert(entry)
        elif entry < self.entry:
            self.left = self.left.insert(entry)

        return self._balanced_tree()

    def delete(self, entry):
        if entry > self.entry:
            self.right = self.right.delete(entry)
        elif entry < self.entry:
            self.left = self.left.delete(entry)
        else:
            if self.is_leaf():
                return _EmptyAVLNode()

            if self.left:
                new_entry = self.left.max()
                self.entry = new_entry
                self.left = self.left.delete(new_entry)
            else:
                new_entry = self.right.entry
                self.entry = new_entry
                self.right = self.right.delete(new_entry)

        return self._balanced_tree()

    def clear(self):
        if self.is_leaf():
            return _EmptyAVLNode()
        self.left = self.left.clear()
        self.right = self.right.clear()

        return _EmptyAVLNode()

    def is_leaf(self):
        return not (bool(self.left) or bool(self.right))

    def max(self):
        max_entry = self.entry
        right_node = self.right
        while right_node:
            max_entry = right_node.entry
            right_node = right_node.right

        return max_entry

    def min(self):
        min_entry = self.entry
        left_node = self.left
        while left_node:
            min_entry = left_node.entry
            left_node = left_node.left

        return min_entry

    @property
    def balance_factor(self):
        return self.left.height - self.right.height

    def __bool__(self):
        """Returns True if the node is not None"""
        return self.entry is not None

    def __len__(self):
        return 1 + len(self.left) + len(self.right)

    def __eq__(self, other):
        return self.entry == other.entry and self.left == other.left and self.right == other.right

    def _balanced_tree(self):
        self._update_height()
        return self._balance_tree_if_unbalanced()

    def _update_height(self):
        self.height = 1 + max(self.left.height, self.right.height)

    def _balance_tree_if_unbalanced(self):
        if self.balance_factor == 2 and self.left.balance_factor == -1:
            return self._rotate_left_right()
        elif self.balance_factor == -2 and self.right.balance_factor == 1:
            return self._rotate_right_left()
        elif self.balance_factor == -2:
            return self._rotate_left()
        elif self.balance_factor == 2:
            return self._rotate_right()
        else:
            return self

    def _rotate_left(self):
        right_tree = self.right
        self.right = right_tree.left
        right_tree.left = self

        self._update_height()
        right_tree._update_height()

        return right_tree

    def _rotate_right(self):
        left_tree = self.left
        self.left = left_tree.right
        left_tree.right = self

        self._update_height()
        left_tree._update_height()

        return left_tree

    def _rotate_left_right(self):
        self.left = self.left._rotate_left()
        return self._rotate_right()

    def _rotate_right_left(self):
        self.right = self.right._rotate_right()
        return self._rotate_left()


class AVLTree:
    def __init__(self, args=None):
        """Initialize an AVL Tree. """
        self.root = None
        self._init_tree(args)

    def insert(self, entry):
        """T.insert(elem) -- insert elem"""
        self.root = self.root.insert(entry)

    def delete(self, entry):
        self.root = self.root.delete(entry)

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

    def __len__(self):
        return len(self.root)

    def __contains__(self, entry):
        root = self.root

        while root:
            if entry > root.entry:
                root = root.right
            elif entry < root.entry:
                root = root.left
            else:
                return True

        return False

    def max(self):
        return self.root.max()

    def min(self):
        return self.root.min()

    def clear(self):
        self.root = self.root.clear()

    def __repr__(self):
        return f'{self.__class__.__name__}({list(self._bfs())})'

    def __str__(self):
        return repr(self)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.height == other.height and len(self) == len(other):
                return self.root == other.root
        return False

    def __bool__(self):
        """Returns True if the tree is not empty"""
        return bool(self.root)

    def _init_tree(self, args):
        self.root = _EmptyAVLNode()

        if args is not None:
            if isinstance(args, self.__class__):
                args = args.traverse('bfs')

            try:
                for entry in args:
                    self.insert(entry)
            except (ValueError, TypeError) as e:
                raise TypeError('AVLTree constructor called with '
                                f'incompatible data type: {e}')

    def _inorder(self, root):
        if root:
            yield from self._inorder(root.left)
            yield root.entry
            yield from self._inorder(root.right)

    def _preorder(self, root):
        if root:
            yield root.entry
            yield from self._preorder(root.left)
            yield from self._preorder(root.right)

    def _postorder(self, root):
        if root:
            yield from self._postorder(root.left)
            yield from self._postorder(root.right)
            yield root.entry

    def _bfs(self):
        root = self.root

        if root:
            q = deque()
            q.append(root)

            while q:
                root = q.popleft()
                yield root.entry
                left = root.left
                right = root.right

                if left:
                    q.append(left)
                if right:
                    q.append(right)
