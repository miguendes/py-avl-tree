"""
Copyright (c) 2018 Miguel Mendes, http://miguendes.me/

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import functools
import unittest

from avl_tree import AVLTree


@functools.total_ordering
class Entry:
    def __init__(self, a: int, b: str):
        self.a = a
        self.b = b

    def __lt__(self, other):
        if self.a == other.a:
            return self.b < other.b
        return self.a < other.a

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __repr__(self):
        return f"{self.__class__.__name__}({self.a}, {self.b})"


class AvlTreeTest(unittest.TestCase):
    def test_empty_tree(self):
        tree = AVLTree()
        self.assertFalse(tree)

    def test_insert_on_empty_tree(self):
        tree = AVLTree()
        tree.insert(9)

        self.assertEqual(tree.root.entry, 9)
        self.assertEqual(tree.root.left.balance_factor, 0)
        self.assertEqual(tree.root.right.balance_factor, 0)
        self.assertTrue(tree)

    def test_insert_duplicated_entry(self):
        tree = AVLTree()
        tree.insert(9)
        tree.insert(10)
        tree.insert(9)

        self.assertEqual(tree.root.entry, 9)
        self.assertEqual(tree.root.right.entry, 10)
        self.assertEqual(tree.height, 2)
        self.assertTrue(tree)

    def test_smaller_entry_on_the_left_of_root(self):
        tree = AVLTree()
        tree.insert(9)
        tree.insert(4)

        self.assertEqual(tree.root.entry, 9)
        self.assertEqual(tree.root.left.entry, 4)

    def test_greater_entry_on_the_right_of_root(self):
        tree = AVLTree()
        tree.insert(9)
        tree.insert(14)

        self.assertEqual(tree.root.entry, 9)
        self.assertEqual(tree.root.right.entry, 14)

    def test_recursive_insertion(self):
        tree = AVLTree()
        tree.insert(9)
        tree.insert(4)
        tree.insert(14)
        tree.insert(17)
        tree.insert(7)

        root = tree.root
        self.assertEqual(root.entry, 9)
        self.assertEqual(root.left.entry, 4)
        self.assertEqual(root.right.entry, 14)
        self.assertEqual(root.right.right.entry, 17)
        self.assertEqual(root.left.right.entry, 7)

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
        self.assertEqual(root.entry, 1)

        tree.insert(2)
        root = tree.root
        self.assertEqual(root.balance_factor, -1)
        self.assertEqual(root.height, 2)
        self.assertEqual(root.entry, 1)
        self.assertEqual(root.right.entry, 2)

        tree.insert(3)
        root = tree.root
        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.left.balance_factor, 0)
        self.assertEqual(root.right.balance_factor, 0)
        self.assertEqual(root.height, 2)

        self.assertEqual(root.entry, 2)
        self.assertEqual(root.left.entry, 1)
        self.assertEqual(root.right.entry, 3)

    def test_single_right_rotation(self):
        tree = AVLTree()
        tree.insert(3)
        root = tree.root
        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.height, 1)
        self.assertEqual(root.entry, 3)

        tree.insert(2)
        root = tree.root
        self.assertEqual(root.balance_factor, 1)
        self.assertEqual(root.height, 2)
        self.assertEqual(root.entry, 3)
        self.assertEqual(root.left.entry, 2)

        tree.insert(1)
        root = tree.root
        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.left.balance_factor, 0)
        self.assertEqual(root.right.balance_factor, 0)
        self.assertEqual(root.height, 2)

        self.assertEqual(root.entry, 2)
        self.assertEqual(root.left.entry, 1)
        self.assertEqual(root.right.entry, 3)

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
        self.assertEqual(root.entry, 1)

        tree.insert(3)
        root = tree.root
        self.assertEqual(root.balance_factor, -1)
        self.assertEqual(root.height, 2)
        self.assertEqual(root.entry, 1)
        self.assertEqual(root.right.entry, 3)

        tree.insert(2)
        root = tree.root
        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.left.balance_factor, 0)
        self.assertEqual(root.right.balance_factor, 0)
        self.assertEqual(root.height, 2)

        self.assertEqual(root.entry, 2)
        self.assertEqual(root.left.entry, 1)
        self.assertEqual(root.right.entry, 3)

    def test_advanced_right_rotation(self):
        tree = AVLTree()
        tree.insert(8)
        root = tree.root
        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.height, 1)
        self.assertEqual(root.entry, 8)

        tree.insert(5)
        root = tree.root

        self.assertEqual(root.balance_factor, 1)
        self.assertEqual(root.height, 2)
        self.assertEqual(root.entry, 8)
        self.assertEqual(root.left.entry, 5)

        tree.insert(11)
        root = tree.root

        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.height, 2)
        self.assertEqual(root.entry, 8)
        self.assertEqual(root.right.entry, 11)

        tree.insert(4)
        root = tree.root

        self.assertEqual(root.balance_factor, 1)
        self.assertEqual(root.height, 3)
        self.assertEqual(root.entry, 8)
        self.assertEqual(root.left.left.entry, 4)

        tree.insert(7)
        root = tree.root

        self.assertEqual(root.balance_factor, 1)
        self.assertEqual(root.height, 3)
        self.assertEqual(root.entry, 8)
        self.assertEqual(root.left.right.entry, 7)

        tree.insert(2)
        root = tree.root

        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.height, 3)
        self.assertEqual(root.entry, 5)
        self.assertEqual(root.left.entry, 4)
        self.assertEqual(root.right.entry, 8)
        self.assertEqual(root.left.left.entry, 2)
        self.assertEqual(root.right.right.entry, 11)
        self.assertEqual(root.right.left.entry, 7)

    def test_advanced_left_rotation(self):
        tree = AVLTree()
        tree.insert(20)
        root = tree.root
        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.height, 1)
        self.assertEqual(root.entry, 20)

        tree.insert(10)
        root = tree.root

        self.assertEqual(root.balance_factor, 1)
        self.assertEqual(root.height, 2)
        self.assertEqual(root.entry, 20)
        self.assertEqual(root.left.entry, 10)

        tree.insert(25)
        root = tree.root

        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.height, 2)
        self.assertEqual(root.entry, 20)
        self.assertEqual(root.right.entry, 25)

        tree.insert(23)
        root = tree.root

        self.assertEqual(root.balance_factor, -1)
        self.assertEqual(root.height, 3)
        self.assertEqual(root.entry, 20)
        self.assertEqual(root.right.left.entry, 23)

        tree.insert(29)
        root = tree.root

        self.assertEqual(root.balance_factor, -1)
        self.assertEqual(root.height, 3)
        self.assertEqual(root.entry, 20)
        self.assertEqual(root.right.right.entry, 29)

        tree.insert(30)
        root = tree.root

        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.height, 3)
        self.assertEqual(root.entry, 25)
        self.assertEqual(root.left.entry, 20)
        self.assertEqual(root.right.entry, 29)
        self.assertEqual(root.left.left.entry, 10)
        self.assertEqual(root.right.right.entry, 30)
        self.assertEqual(root.left.right.entry, 23)

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

        entries = range(150)
        for entry in entries:
            tree.insert(entry)
        with self.subTest("test non-empty tree"):
            self.assertEqual(len(tree), len(entries))

        with self.subTest("test empty tree"):
            self.assertEqual(len(AVLTree()), 0)

    def test_contains(self):
        with self.subTest("test empty tree should not contain any entry"):
            self.assertNotIn(10, AVLTree())

        with self.subTest("test single element must be in tree"):
            tree = AVLTree()
            tree.insert(10)

            self.assertIn(10, tree)

        with self.subTest("test element must be in tree"):
            entries = range(128)

            tree = AVLTree()

            for entry in entries:
                tree.insert(entry)

            for entry in entries:
                self.assertIn(entry, tree)

    def test_balanced_tree_must_have_height_of_log2(self):
        import math
        base = 2

        for exp in range(2, 13):
            tree1 = AVLTree()
            tree2 = AVLTree()
            tree3 = AVLTree()

            entries = [i for i in range(base ** exp)]
            for entry in entries:
                tree1.insert(entry)
                if entry == 0:
                    continue
                tree2.insert(entry)
                if entry == 1:
                    continue
                tree3.insert(entry)

            with self.subTest(f"test inserting {len(entries)} elements."):
                self.assertEqual(tree1.height, int(math.log2(len(entries))) + 1)
                self.assertEqual(len(tree1), len(entries))
            with self.subTest(f"test inserting {len(entries)-1} elements."):
                self.assertEqual(tree2.height, int(math.log2(len(entries))))
                self.assertEqual(len(tree2), len(entries) - 1)
            with self.subTest(f"test inserting {len(entries)-2} elements."):
                self.assertEqual(tree3.height, int(math.log2(len(entries))))
                self.assertEqual(len(tree3), len(entries) - 2)

    def test_initialize_tree_from_sequence(self):
        import math
        entries = [1, 2, 3, 4, 5, 6, 7]
        tree = AVLTree(entries)

        expected_order = (4, 2, 6, 1, 3, 5, 7)
        with self.subTest(f"bfs traversal must be have this order {expected_order}."):
            self.assertTupleEqual(tuple(tree.traverse('bfs')), expected_order)
        with self.subTest(f"tree must have {len(entries)} entries."):
            self.assertEqual(len(tree), len(entries))
        with self.subTest(f"tree must have {math.ceil(math.log2(len(entries)))} height."):
            self.assertEqual(tree.height, math.ceil(math.log2(len(entries))))

    def test_constructor_not_properly_called(self):
        with self.assertRaises(TypeError) as context:
            AVLTree(4)
        self.assertIn("AVLTree constructor called with incompatible data type: "
                      "'int' object is not iterable", str(context.exception))

    def test_find_max(self):
        entries = get_random_entries()
        tree = AVLTree(entries)
        self.assertEqual(tree.max(), max(entries))

    def test_find_min(self):
        entries = get_random_entries()
        tree = AVLTree(entries)
        self.assertEqual(tree.min(), min(entries))

    def test_delete_single_element(self):
        tree = AVLTree([1])

        tree.delete(1)

        self.assertNotIn(1, tree)
        self.assertFalse(tree)
        self.assertEqual(len(tree), 0)

    def test_delete_leaf_node(self):
        tree = AVLTree([1, 2])

        tree.delete(2)

        self.assertIn(1, tree)
        self.assertNotIn(2, tree)
        self.assertTrue(tree)
        self.assertEqual(len(tree), 1)

    def test_delete_not_existent_entry(self):
        with self.subTest(f"test delete non-existent entry on a non-empty tree"):
            self.assert_entry_error([1, 2, 3], 10)

        with self.subTest(f"test delete non-existent entry on a empty tree"):
            self.assert_entry_error(None, 10)

    def assert_entry_error(self, entries, entry_to_be_deleted):
        with self.assertRaises(KeyError) as context:
            tree = AVLTree(entries)
            tree.delete(entry_to_be_deleted)
            self.assertIn(f"entryError: {entry_to_be_deleted}", str(context.exception))

    def test_delete_entry_but_tree_remains_balanced(self):
        entries = [10, 5, 11, 3, 7, 15]
        tree = AVLTree(entries)
        entry_to_be_deleted = 10

        tree.delete(entry_to_be_deleted)

        expected_order = (7, 5, 11, 3, 15)
        self.assertNotIn(entry_to_be_deleted, tree)
        self.assertTupleEqual(tuple(tree.traverse('bfs')), expected_order)

    def test_delete_entry_make_tree_unbalanced(self):
        entries = [5, 3, 8, 2, 4, 7, 11, 1, 6, 10, 12, 9]
        tree = AVLTree(entries)
        entry_to_be_deleted = 4

        tree.delete(entry_to_be_deleted)

        expected_order = (8, 5, 11, 2, 7, 10, 12, 1, 3, 6, 9)
        self.assertNotIn(entry_to_be_deleted, tree)
        self.assertTupleEqual(tuple(tree.traverse('bfs')), expected_order)

    def test_delete_entries_in_a_row(self):
        entries = [2, 1, 4, 3, 5]
        tree = AVLTree(entries)

        tree.delete(1)
        self.assertNotIn(1, tree)
        self.assertTupleEqual(tuple(tree.traverse('bfs')), (4, 2, 5, 3))

        tree.delete(2)
        self.assertNotIn(2, tree)
        self.assertTupleEqual(tuple(tree.traverse('bfs')), (4, 3, 5))

        tree.delete(3)
        self.assertNotIn(3, tree)
        self.assertTupleEqual(tuple(tree.traverse('bfs')), (4, 5))

        tree.delete(4)
        self.assertNotIn(4, tree)
        self.assertTupleEqual(tuple(tree.traverse('bfs')), (5,))

        tree.delete(5)
        self.assertNotIn(5, tree)
        self.assertTupleEqual(tuple(tree.traverse('bfs')), ())
        self.assertFalse(tree)

    def test_str_repr(self):
        tree = AVLTree([1, 2, 3, 4, 5])
        self.assertEqual(repr(tree), 'AVLTree([2, 1, 4, 3, 5])')
        self.assertEqual(str(tree), 'AVLTree([2, 1, 4, 3, 5])')

    def test_equals(self):
        tree1 = AVLTree([1, 2, 3, 4, 5])
        tree2 = AVLTree([2, 1, 4, 3, 5])
        tree3 = AVLTree([1, 2, 3, 4, 5, 6])

        with self.subTest(f"test equal trees"):
            self.assertEqual(tree1, tree2)
            self.assertFalse(tree1 is tree2)
        with self.subTest(f"test different trees"):
            self.assertNotEqual(tree1, tree3)
            self.assertFalse(tree1 is tree3)
            self.assertNotEqual(tree2, tree3)
            self.assertFalse(tree2 is tree3)
        with self.subTest(f"test tree is different from other classes"):
            self.assertNotEqual(tree1, int(9))

    def test_clear(self):
        tree = AVLTree([1, 2, 3, 4, 5])
        tree.clear()

        self.assertFalse(tree)

    def test_build_tree_from_other(self):
        original = AVLTree([1, 2, 3, 4, 5])
        copy = AVLTree(original)

        self.assertEqual(copy, AVLTree([2, 1, 4, 3, 5]))

    def test_search(self):
        tree = AVLTree([1, 2, 3, 4, 5])
        entry = tree.search(4)

        self.assertEqual(4, entry)

    def test_search_complex_data_type(self):
        tree = AVLTree([Entry(1, 'a'),
                        Entry(2, 'b'),
                        Entry(3, 'c'),
                        Entry(3, 'd'), ])
        entry = tree.search(Entry(3, 'd'))

        self.assertEqual(Entry(3, 'd'), entry)

    def test_copy(self):
        import copy
        tree1 = AVLTree([1, 2, 3, 4, 5])
        tree2 = copy.copy(tree1)

        with self.subTest(f"test equal trees"):
            self.assertEqual(tree1, tree2)

    def test_pred(self):
        import random
        random.seed(901)
        entries = get_random_entries()
        tree = AVLTree(entries)

        with self.subTest(f"test pred found"):
            prev = None
            for entry in tree.traverse():
                try:
                    pred = tree.pred(entry)
                    self.assertEqual(prev, pred)
                    prev = entry
                except KeyError:
                    self.assertIsNone(prev)

        with self.assertRaises(KeyError) as context:
            tree.pred(1000000)
        self.assertIn("Predecessor of 1000000 not found.", str(context.exception))


def get_random_entries():
    from random import randint, shuffle, seed
    seed(901)
    a = randint(1, 205)
    b = randint(1, 205)
    lower, upper = min(a, b), max(a, b)
    entries = list(range(lower, upper + 1))
    shuffle(entries)
    return entries


if __name__ == '__main__':
    unittest.main()
