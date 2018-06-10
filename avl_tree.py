import unittest


class AvlNode(object):
    def __init__(self, elem, left=None, right=None):
        self.elem = elem
        self.left = left
        self.right = right


class AvlTree(object):
    def __init__(self):
        self.root = None

    def empty(self):
        return self.root is None

    def insert(self, elem):
        self.root = self._insert(self.root, elem)

    def _insert(self, root, elem):
        if root is None:
            return AvlNode(elem)
        else:
            if elem > root.elem:
                root.right = self._insert(root.right, elem)
            else:
                root.left = self._insert(root.left, elem)
        return root


class AvlTreeTest(unittest.TestCase):
    def test_empty_tree(self):
        tree = AvlTree()
        self.assertTrue(tree.empty())

    def test_insert_on_empty_tree(self):
        tree = AvlTree()
        tree.insert(9)

        self.assertEqual(tree.root.elem, 9)
        self.assertFalse(tree.empty())

    def test_smaller_elem_on_the_left_of_root(self):
        tree = AvlTree()
        tree.insert(9)
        tree.insert(4)

        self.assertEqual(tree.root.elem, 9)
        self.assertEqual(tree.root.left.elem, 4)

    def test_greater_elem_on_the_right_of_root(self):
        tree = AvlTree()
        tree.insert(9)
        tree.insert(14)

        self.assertEqual(tree.root.elem, 9)
        self.assertEqual(tree.root.right.elem, 14)

    def test_recursive_insertion(self):
        tree = AvlTree()
        tree.insert(9)
        tree.insert(4)
        tree.insert(14)
        tree.insert(17)
        tree.insert(7)

        root = tree.root
        self.assertEqual(root.elem, 9)
        self.assertEqual(root.left.elem, 4)
        self.assertEqual(root.right.elem, 14)
        self.assertEqual(root.right.right.elem, 17)
        self.assertEqual(root.left.right.elem, 7)

