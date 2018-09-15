class _AvlNode:
    def __init__(self, elem=None, left=None, right=None):
        self.elem = elem
        self.left = left
        self.right = right
        self.height = 1
        self.balance_factor = 0

    def insert(self, elem):
        if self.elem is None:
            self.elem = elem
        elif elem > self.elem:
            if self.right is None:
                self.right = _AvlNode(elem)
            else:
                self.right.insert(elem)
        elif elem <= self.elem:
            if self.left is None:
                self.left = _AvlNode(elem)
            else:
                self.left.insert(elem)
        else:
            raise RuntimeError

        self._fix_height()
        self._check_imbalance()

    def _check_imbalance(self):
        if self.balance_factor == 2 and self.left.balance_factor == -1:
            self.rotate_left_right()
        elif self.balance_factor == -2:
            self.rotate_left()
        elif self.balance_factor == 2:
            self.rotate_right()

    def rotate_left(self):
        old_elem = self.elem
        self.elem = self.right.elem
        self.insert(old_elem)
        self.right = self.right.right

        self._fix_height()

    def _fix_height(self):
        left_height = self.left.height if self.left is not None else 0
        right_height = self.right.height if self.right is not None else 0
        self.height = 1 + max(left_height, right_height)
        self.balance_factor = left_height - right_height

    def rotate_right(self):
        old_elem = self.elem
        self.elem = self.left.elem
        self.insert(old_elem)
        self.left = self.left.left

        self._fix_height()

    def rotate_left_right(self):
        self.left.rotate_left()
        self.rotate_right()


class AvlTree:
    def __init__(self):
        self.root = _AvlNode()

    def empty(self):
        return self.root.elem is None

    def insert(self, elem):
        self.root.insert(elem)
