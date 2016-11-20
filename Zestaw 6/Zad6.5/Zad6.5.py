import fracs
import unittest

tmp = fracs.Frac(1,2)
tmp2 = fracs.Frac(2,2)
tmp3 = fracs.Frac(-1, 2)
tmp4 = fracs.Frac(2, 1)
fracZero = fracs.Frac(0,1)

class TestFractions(unittest.TestCase):

    def setUp(self): pass

    def test_cmp(self):
    	self.assertEqual(cmp(tmp, tmp), 0)
    	self.assertEqual(cmp(tmp, tmp2), -1)
    	self.assertEqual(cmp(tmp, fracZero), 1)

    def test_pos(self):
    	self.assertEqual(+tmp, tmp)
    	self.assertEqual(+tmp3, tmp3)
    	self.assertEqual(fracZero, fracZero)

    def test_neg(self):
    	self.assertEqual(-tmp, tmp3)
    	self.assertEqual(-tmp3, tmp)
    	self.assertEqual(-fracZero, fracZero)
    	self.assertEqual(-(-tmp), tmp)

    def test_invert(self):
    	self.assertEqual(~tmp, tmp4)
    	self.assertEqual(-(~tmp3), tmp4)

    def test_float(self):
    	self.assertIsInstance(float(tmp), float)
        self.assertIsInstance(float(fracZero), float)

    def test_repr(self):
        self.assertIsInstance(repr(tmp), str)
        self.assertEqual(repr(tmp), "Frac(1,2)")

    def test_str(self):
        self.assertIsInstance(str(tmp), str)

    def test_init(self):
        self.assertEqual(tmp.x, 1)
        self.assertEqual(tmp.y, 2)

    def test_add_frac(self):
    	
    	self.assertEqual(tmp+tmp, tmp2)
    	self.assertEqual(tmp + (-tmp), fracZero)
    	self.assertEqual(tmp2 + (-tmp), tmp)

    def test_sub(self):
        self.assertEqual(tmp-tmp, fracZero)
        self.assertEqual(tmp - (-tmp), tmp2)
        self.assertEqual(tmp2 + (-tmp), tmp)

    def test_mul(self):
        self.assertEqual(tmp/tmp, fracs.Frac(1,1))
        self.assertEqual(tmp/-tmp, fracs.Frac(-1,1))

    def test_div(self):
        self.assertEqual(tmp*tmp, fracs.Frac(1,4))
        self.assertEqual(tmp*-tmp, fracs.Frac(-1,4))
        self.assertEqual(tmp*fracZero, fracs.Frac(0,1))

	def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy