import unittest
from playground import LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_append(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)

        self.assertEqual(self.ll.head.data, 1)
        self.assertEqual(self.ll.head.next.data, 2)
        self.assertEqual(self.ll.head.next.next.data, 3)
        self.assertIsNone(self.ll.head.next.next.next)

    def test_prepend(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.prepend(0)

        self.assertEqual(self.ll.head.data, 0)
        self.assertEqual(self.ll.head.next.data, 1)
        self.assertEqual(self.ll.head.next.next.data, 2)
        self.assertIsNone(self.ll.head.next.next.next)

    def test_delete_with_value(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)

        self.ll.delete_with_value(2)

        self.assertEqual(self.ll.head.data, 1)
        self.assertEqual(self.ll.head.next.data, 3)
        self.assertIsNone(self.ll.head.next.next)

        self.ll.delete_with_value(1)

        self.assertEqual(self.ll.head.data, 3)
        self.assertIsNone(self.ll.head.next)

        self.ll.delete_with_value(3)

        self.assertIsNone(self.ll.head)

    def test_delete_with_value_non_existent(self):
        self.ll.append(1)
        self.ll.append(2)

        self.ll.delete_with_value(3)

        self.assertEqual(self.ll.head.data, 1)
        self.assertEqual(self.ll.head.next.data, 2)
        self.assertIsNone(self.ll.head.next.next)

    def test_delete_with_value_empty_list(self):
        self.ll.delete_with_value(1)

        self.assertIsNone(self.ll.head)

    def test_display(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)

        from io import StringIO
        import sys

        captured_output = StringIO()          # Create StringIO object
        sys.stdout = captured_output          # Redirect stdout.
        self.ll.display()                     # Call display function.
        sys.stdout = sys.__stdout__           # Reset redirect.

        self.assertEqual(captured_output.getvalue(), "1 -> 2 -> 3 -> None\n")

if __name__ == '__main__':
    unittest.main()
