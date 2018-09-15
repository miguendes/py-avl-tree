import unittest

from avl_tree import AvlTree


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

    def test_height(self):
        tree = AvlTree()
        tree.insert(9)
        root = tree.root
        self.assertEqual(root.height, 1)

        tree.insert(4)
        self.assertEqual(root.height, 2)
        self.assertEqual(root.left.height, 1)

        tree.insert(14)
        self.assertEqual(root.height, 2)
        self.assertEqual(root.left.height, 1)
        self.assertEqual(root.right.height, 1)

        tree.insert(17)
        self.assertEqual(root.height, 3)
        self.assertEqual(root.left.height, 1)
        self.assertEqual(root.right.height, 2)
        self.assertEqual(root.right.right.height, 1)

        tree.insert(7)
        self.assertEqual(root.height, 3)
        self.assertEqual(root.left.height, 2)
        self.assertEqual(root.left.right.height, 1)

    def test_balance_factor(self):
        tree = AvlTree()
        tree.insert(9)
        root = tree.root
        self.assertEqual(root.balance_factor, 0)

        tree.insert(4)
        self.assertEqual(root.balance_factor, 1)
        self.assertEqual(root.left.balance_factor, 0)

        tree.insert(14)
        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.left.balance_factor, 0)
        self.assertEqual(root.right.balance_factor, 0)

        tree.insert(17)
        self.assertEqual(root.balance_factor, -1)
        self.assertEqual(root.left.balance_factor, 0)
        self.assertEqual(root.right.balance_factor, -1)
        self.assertEqual(root.right.right.balance_factor, 0)

        tree.insert(7)
        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.left.balance_factor, -1)
        self.assertEqual(root.left.right.balance_factor, 0)
        