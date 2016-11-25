from fracs import Frac
import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.tmp = Frac(1,2)
        self.tmp2 = Frac(2,2)
        self.tmp3 = Frac(-1, 2)
        self.tmp4 = Frac(2, 1)
        self.fracZero = Frac(0,1)

    def test_cmp(self):
    	self.assertEqual(cmp(self.tmp, self.tmp), 0)
    	self.assertEqual(cmp(self.tmp, self.tmp2), -1)
    	self.assertEqual(cmp(self.tmp, self.fracZero), 1)

    def test_pos(self):
    	self.assertEqual(+self.tmp, self.tmp)
    	self.assertEqual(+self.tmp3, self.tmp3)
    	self.assertEqual(self.fracZero, self.fracZero)

    def test_neg(self):
    	self.assertEqual(-self.tmp, self.tmp3)
    	self.assertEqual(-self.tmp3, self.tmp)
    	self.assertEqual(-self.fracZero, self.fracZero)
    	self.assertEqual(-(-self.tmp), self.tmp)

    def test_invert(self):
    	self.assertEqual(~self.tmp, self.tmp4)
    	self.assertEqual(-(~self.tmp3), self.tmp4)

    def test_float(self):
    	self.assertIsInstance(float(self.tmp), float)
        self.assertIsInstance(float(self.fracZero), float)

    def test_repr(self):
        self.assertIsInstance(repr(self.tmp), str)
        self.assertEqual(repr(self.tmp), "Frac(1,2)")

    def test_str(self):
        self.assertIsInstance(str(self.tmp), str)

    def test_init(self):
        self.assertEqual(self.tmp.x, 1)
        self.assertEqual(self.tmp.y, 2)

    def test_add_frac(self):
    	
    	self.assertEqual(self.tmp+self.tmp, self.tmp2)
    	self.assertEqual(self.tmp + (-self.tmp), self.fracZero)
    	self.assertEqual(self.tmp2 + (-self.tmp), self.tmp)

    def test_sub(self):
        self.assertEqual(self.tmp-self.tmp, self.fracZero)
        self.assertEqual(self.tmp - (-self.tmp), self.tmp2)
        self.assertEqual(self.tmp2 + (-self.tmp), self.tmp)

    def test_mul(self):
        self.assertEqual(self.tmp*self.tmp, Frac(1,4))
        self.assertEqual(self.tmp*-self.tmp, Frac(-1,4))
        self.assertEqual(self.tmp*self.fracZero, Frac(0,1))

    def test_div(self):
        self.assertEqual(self.tmp/self.tmp, Frac(1,1))
        self.assertEqual(self.tmp/-self.tmp, Frac(-1,1))

	def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy