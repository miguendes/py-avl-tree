import unittest

from avl_tree import AVLTree


class AvlTreeTest(unittest.TestCase):
    def test_empty_tree(self):
        tree = AVLTree()
        self.assertFalse(tree)

    def test_insert_on_empty_tree(self):
        tree = AVLTree()
        tree.insert(9)

        self.assertEqual(tree.root.key, 9)
        self.assertEqual(tree.root.left.balance_factor, 0)
        self.assertEqual(tree.root.right.balance_factor, 0)
        self.assertTrue(tree)

    def test_insert_duplicated_key(self):
        tree = AVLTree()
        tree.insert(9)
        tree.insert(10)
        tree.insert(9)

        self.assertEqual(tree.root.key, 9)
        self.assertEqual(tree.root.right.key, 10)
        self.assertEqual(tree.height, 2)
        self.assertTrue(tree)

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

        d = {
            'preorder': (25, 20, 10, 23, 29, 30),
            'inorder': (10, 20, 23, 25, 29, 30),
            'postorder': (10, 23, 20, 30, 29, 25),
            'bfs': (25, 20, 29, 10, 23, 30),
        }

        for order, expected_value in d.items():
            with self.subTest(f"test {order}"):
                self.assertTupleEqual(tuple(tree.traverse(order)), expected_value)

    def test_empty_traversal(self):
        tree = AVLTree()

        d = {
            'preorder': (),
            'inorder': (),
            'postorder': (),
            'bfs': (),
        }

        for order, expected_value in d.items():
            with self.subTest(f"test {order}"):
                self.assertTupleEqual(tuple(tree.traverse(order)), expected_value)

    def test_length(self):
        tree = AVLTree()

        keys = range(150)
        for key in keys:
            tree.insert(key)
        with self.subTest("test non-empty tree"):
            self.assertEqual(len(tree), len(keys))

        with self.subTest("test empty tree"):
            self.assertEqual(len(AVLTree()), 0)

    def test_contains(self):
        with self.subTest("test empty tree should not contain any key"):
            self.assertNotIn(10, AVLTree())

        with self.subTest("test single element must be in tree"):
            tree = AVLTree()
            tree.insert(10)

            self.assertIn(10, tree)

        with self.subTest("test element must be in tree"):
            keys = range(128)

            tree = AVLTree()

            for key in keys:
                tree.insert(key)

            for key in keys:
                self.assertIn(key, tree)

    def test_balanced_tree_must_have_height_of_log2(self):
        import math
        base = 2

        for exp in range(2, 13):
            tree1 = AVLTree()
            tree2 = AVLTree()
            tree3 = AVLTree()

            keys = [i for i in range(base ** exp)]
            for key in keys:
                tree1.insert(key)
                if key == 0:
                    continue
                tree2.insert(key)
                if key == 1:
                    continue
                tree3.insert(key)

            with self.subTest(f"test inserting {len(keys)} elements."):
                self.assertEqual(tree1.height, int(math.log2(len(keys))) + 1)
                self.assertEqual(len(tree1), len(keys))
            with self.subTest(f"test inserting {len(keys)-1} elements."):
                self.assertEqual(tree2.height, int(math.log2(len(keys))))
                self.assertEqual(len(tree2), len(keys) - 1)
            with self.subTest(f"test inserting {len(keys)-2} elements."):
                self.assertEqual(tree3.height, int(math.log2(len(keys))))
                self.assertEqual(len(tree3), len(keys) - 2)

    def test_initialize_tree_from_sequence(self):
        import math
        keys = [1, 2, 3, 4, 5, 6, 7]
        tree = AVLTree(keys)

        expected_order = (4, 2, 6, 1, 3, 5, 7)
        with self.subTest(f"bfs traversal must be have this order {expected_order}."):
            self.assertTupleEqual(tuple(tree.traverse('bfs')), expected_order)
        with self.subTest(f"tree must have {len(keys)} keys."):
            self.assertEqual(len(tree), len(keys))
        with self.subTest(f"tree must have {math.ceil(math.log2(len(keys)))} height."):
            self.assertEqual(tree.height, math.ceil(math.log2(len(keys))))


if __name__ == '__main__':
    unittest.main()
