import unittest

from avl_tree import AVLTree


class AvlTreeTest(unittest.TestCase):
    def test_empty_tree(self):
        tree = AVLTree()
        self.assertTrue(tree.empty())

    def test_insert_on_empty_tree(self):
        tree = AVLTree()
        tree.insert(9)

        self.assertEqual(tree.root.key, 9)
        self.assertFalse(tree.empty())

    def test_smaller_key_on_the_left_of_root(self):
        tree = AVLTree()
        tree.insert(9)
        tree.insert(4)

        self.assertEqual(tree.root.key, 9)
        self.assertEqual(tree.root.left.key, 4)

    def test_greater_key_on_the_right_of_root(self):
        tree = AVLTree()
        tree.insert(9)
        tree.insert(14)

        self.assertEqual(tree.root.key, 9)
        self.assertEqual(tree.root.right.key, 14)

    def test_recursive_insertion(self):
        tree = AVLTree()
        tree.insert(9)
        tree.insert(4)
        tree.insert(14)
        tree.insert(17)
        tree.insert(7)

        root = tree.root
        self.assertEqual(root.key, 9)
        self.assertEqual(root.left.key, 4)
        self.assertEqual(root.right.key, 14)
        self.assertEqual(root.right.right.key, 17)
        self.assertEqual(root.left.right.key, 7)

    def test_height(self):
        tree = AVLTree()
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
        tree = AVLTree()
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

    def test_single_left_rotation(self):
        tree = AVLTree()
        tree.insert(1)
        root = tree.root
        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.height, 1)

        tree.insert(2)
        root = tree.root
        self.assertEqual(root.balance_factor, -1)
        self.assertEqual(root.height, 2)

        tree.insert(3)
        root = tree.root
        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.left.balance_factor, 0)
        self.assertEqual(root.right.balance_factor, 0)
        self.assertEqual(root.height, 2)

    def test_single_right_rotation(self):
        tree = AVLTree()
        tree.insert(3)
        root = tree.root
        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.height, 1)

        tree.insert(2)
        root = tree.root
        self.assertEqual(root.balance_factor, 1)
        self.assertEqual(root.height, 2)

        tree.insert(1)
        root = tree.root
        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.left.balance_factor, 0)
        self.assertEqual(root.right.balance_factor, 0)
        self.assertEqual(root.height, 2)

    def test_left_right_rotation(self):
        tree = AVLTree()
        tree.insert(3)
        root = tree.root
        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.height, 1)

        tree.insert(1)
        root = tree.root
        self.assertEqual(root.balance_factor, 1)
        self.assertEqual(root.height, 2)

        tree.insert(2)
        root = tree.root
        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.left.balance_factor, 0)
        self.assertEqual(root.right.balance_factor, 0)
        self.assertEqual(root.height, 2)

    def test_right_left_rotation(self):
        tree = AVLTree()
        tree.insert(1)
        root = tree.root
        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.height, 1)
        self.assertEqual(root.key, 1)

        tree.insert(3)
        root = tree.root
        self.assertEqual(root.balance_factor, -1)
        self.assertEqual(root.height, 2)
        self.assertEqual(root.key, 1)
        self.assertEqual(root.right.key, 3)

        tree.insert(2)
        root = tree.root
        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.left.balance_factor, 0)
        self.assertEqual(root.right.balance_factor, 0)
        self.assertEqual(root.height, 2)

        self.assertEqual(root.key, 2)
        self.assertEqual(root.left.key, 1)
        self.assertEqual(root.right.key, 3)

    def test_advanced_right_rotation(self):
        tree = AVLTree()
        tree.insert(8)
        root = tree.root
        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.height, 1)
        self.assertEqual(root.key, 8)

        tree.insert(5)
        root = tree.root

        self.assertEqual(root.balance_factor, 1)
        self.assertEqual(root.height, 2)
        self.assertEqual(root.key, 8)
        self.assertEqual(root.left.key, 5)

        tree.insert(11)
        root = tree.root

        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.height, 2)
        self.assertEqual(root.key, 8)
        self.assertEqual(root.right.key, 11)

        tree.insert(4)
        root = tree.root

        self.assertEqual(root.balance_factor, 1)
        self.assertEqual(root.height, 3)
        self.assertEqual(root.key, 8)
        self.assertEqual(root.left.left.key, 4)

        tree.insert(7)
        root = tree.root

        self.assertEqual(root.balance_factor, 1)
        self.assertEqual(root.height, 3)
        self.assertEqual(root.key, 8)
        self.assertEqual(root.left.right.key, 7)

        tree.insert(2)
        root = tree.root

        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.height, 3)
        self.assertEqual(root.key, 5)
        self.assertEqual(root.left.key, 4)
        self.assertEqual(root.right.key, 8)
        self.assertEqual(root.left.left.key, 2)
        self.assertEqual(root.right.right.key, 11)
        self.assertEqual(root.right.left.key, 7)

    def test_advanced_left_rotation(self):
        tree = AVLTree()
        tree.insert(20)
        root = tree.root
        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.height, 1)
        self.assertEqual(root.key, 20)

        tree.insert(10)
        root = tree.root

        self.assertEqual(root.balance_factor, 1)
        self.assertEqual(root.height, 2)
        self.assertEqual(root.key, 20)
        self.assertEqual(root.left.key, 10)

        tree.insert(25)
        root = tree.root

        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.height, 2)
        self.assertEqual(root.key, 20)
        self.assertEqual(root.right.key, 25)

        tree.insert(23)
        root = tree.root

        self.assertEqual(root.balance_factor, -1)
        self.assertEqual(root.height, 3)
        self.assertEqual(root.key, 20)
        self.assertEqual(root.right.left.key, 23)

        tree.insert(29)
        root = tree.root

        self.assertEqual(root.balance_factor, -1)
        self.assertEqual(root.height, 3)
        self.assertEqual(root.key, 20)
        self.assertEqual(root.right.right.key, 29)

        tree.insert(30)
        root = tree.root

        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.height, 3)
        self.assertEqual(root.key, 25)
        self.assertEqual(root.left.key, 20)
        self.assertEqual(root.right.key, 29)
        self.assertEqual(root.left.left.key, 10)
        self.assertEqual(root.right.right.key, 30)
        self.assertEqual(root.left.right.key, 23)

    def test_traversal(self):
        tree = AVLTree()

        tree.insert(20)
        tree.insert(10)
        tree.insert(25)
        tree.insert(23)
        tree.insert(29)
        tree.insert(30)

        self.assertListEqual(list(tree.traverse('preorder')), [25, 20, 10, 23, 29, 30])
        self.assertListEqual(list(tree.traverse()), [10, 20, 23, 25, 29, 30])
        self.assertListEqual(list(tree.traverse('postorder')), [10, 23, 20, 30, 29, 25])
