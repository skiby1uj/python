from stack import Stack
import unittest

class TestFrac(unittest.TestCase):

    def setUp(self):
         self.emptyStack = Stack()
         self.stackIsFull = Stack(1)
         self.stackIsFull.push(1)
         self.stact1 = Stack()

    def test_init(self):
        self.tmp = Stack(2)
        self.assertEqual(self.tmp.size, 2)
        self.assertEqual(self.tmp.n, 0)
        self.assertEqual(len(self.tmp.items), 2)

    def test_is_empty(self):
        self.assertTrue(self.emptyStack.is_empty())
        self.assertFalse(self.stackIsFull.is_empty())

    def test_is_full(self):
        self.assertTrue(self.stackIsFull.is_full())
        self.assertFalse(self.emptyStack.is_full())

    def test_push(self):
        self.stact1.push(11)
        self.assertEqual(1, self.stact1.n)
        self.assertEqual(11, self.stact1.items[0])
        with self.assertRaises(ValueError):
            self.stackIsFull.push(123)

    def test_pop(self):
        self.stact1.push(123)
        self.assertEqual(self.stact1.pop(), 123)
        with self.assertRaises(ValueError):
            self.stact1.pop()

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
