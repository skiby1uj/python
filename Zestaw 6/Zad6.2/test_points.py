import points
import unittest


class TestPoint(unittest.TestCase):

    def setUp(self): pass

    def test_init(self):
    	tmp = points.Point(1,2)
    	self.assertIsInstance(tmp, points.Point)
    	self.assertIs(tmp.x, 1)
    	self.assertIs(tmp.y, 2)

    def test_str(self):
    	tmp = points.Point(1,2)
    	self.assertIsInstance(str(tmp), str)
    	self.assertEqual(str(tmp), "(1, 2)")

    def test_repr(self):
    	tmp = points.Point(1,2)
    	self.assertIsInstance(repr(tmp), str)
    	self.assertEqual(repr(tmp), "Point(1, 2)")

    def test_eq(self):
    	tmp = points.Point(1,2)
    	self.assertTrue(tmp == points.Point(1,2))
    	self.assertFalse(tmp == points.Point(2,2))
    	self.assertFalse(tmp == points.Point(0,0))

    def test_ne(self):
    	tmp = points.Point(1,2)
    	self.assertFalse(tmp != points.Point(1,2))
    	self.assertTrue(tmp != points.Point(2,2))
    	self.assertTrue(tmp != points.Point(0,0))

    def test_add(self):
    	tmp = points.Point(1,2)
    	self.assertEqual(tmp + tmp, points.Point(2,4))
    	self.assertEqual(tmp + points.Point(-1,-2), points.Point(0,0))
    	self.assertEqual(tmp + points.Point(0,0), tmp)
    
    def test_sub(self):
    	tmp = points.Point(1,2)
    	self.assertEqual(tmp - tmp, points.Point(0,0))
    	self.assertEqual(tmp - points.Point(-1,-2), points.Point(2,4))
    	self.assertEqual(tmp - points.Point(0,0), tmp)

    def test_mul(self):
    	tmp = points.Point(1,2)
    	self.assertEqual(tmp * points.Point(3,4), 11)
    	self.assertEqual(tmp * points.Point(0,0), 0)
    	self.assertEqual(tmp * tmp, 5)

    def test_cross(self):
    	tmp = points.Point(1,2)
    	self.assertEqual(tmp.cross(tmp), 0)
    	self.assertEqual(tmp.cross(points.Point(0,0)), 0)
    	self.assertEqual(tmp.cross(points.Point(3,4)), -2)

    def test_length(self):
    	self.assertEqual(points.Point(2,0).length(), 2)
    	self.assertEqual(points.Point(0,0).length(), 0)
    	self.assertEqual(points.Point(3,4).length(), 5)


	def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy