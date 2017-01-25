from queue import Queue
import unittest

class TestFrac(unittest.TestCase):

    def setUp(self):
        self.queueEmpty = Queue()
        self.queue1 = Queue(3)
        self.queue1Full = Queue(1)
        self.queue1Full.put(1)

    def test_init(self):
        self.tmp = Queue(2)
        self.assertEqual(self.tmp.n, 3)
        self.assertEqual(self.tmp.head, 0)
        self.assertEqual(self.tmp.tail, 0)
        self.assertEqual(len(self.tmp.items), 3)

    def test_is_empty(self):
        self.assertFalse(self.queue1Full.is_empty())
        self.assertTrue(self.queue1.is_empty())
        self.assertTrue(self.queueEmpty.is_empty())
        
    def test_is_full(self):
        self.assertTrue(self.queue1Full.is_full())
        self.assertFalse(self.queue1.is_full())
        self.assertFalse(self.queueEmpty.is_full())

    def test_put(self):
        self.queue1.put(123)
        self.assertEqual(self.queue1.items[0], 123)
        with self.assertRaises(ValueError):
            self.queue1Full.put(12)

    def test_get(self):
        self.queue1.put(123)
        self.assertEqual(self.queue1.get(), 123)
        with self.assertRaises(ValueError):
            self.queue1.get()
            
    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
