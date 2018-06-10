import unittest


class AvlNode(object):
    def __init__(self, elem=None, left=None, right=None):
        self.elem = elem
        self.left = left
        self.right = right

    def insert(self, elem):
        if self.elem is None:
            self.elem = elem
        elif elem > self.elem:
            if self.right is None:
                self.right = AvlNode(elem)
            else:
                self.right.insert(elem)
        elif elem <= self.elem:
            if self.left is None:
                self.left = AvlNode(elem)
            else:
                self.left.insert(elem)
        else:
            raise RuntimeError


class AvlTree(object):
    def __init__(self):
        self.root = AvlNode()

    def empty(self):
        return self.root.elem is None

    def insert(self, elem):
        self.root.insert(elem)


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
