import fracs
import unittest

class TestFractions(unittest.TestCase):

    def setUp(self): pass
    
    def test_add_frac(self):
        self.assertIs(fracs.cmp_frac(fracs.add_frac([1,1], [1,1]), [2,1]), 0)
        self.assertIs(fracs.cmp_frac(fracs.add_frac([1,2], [1,-2]), [0,1]), 0)
        self.assertIs(fracs.cmp_frac(fracs.add_frac([1,2], [1,3]), [5,6]), 0)

    def test_sub_frac(self):
        self.assertIs(fracs.cmp_frac(fracs.sub_frac([1,1], [1,1]), [0,1]), 0)
        self.assertIs(fracs.cmp_frac(fracs.sub_frac([1,2], [1,-2]), [1,1]), 0)
        self.assertIs(fracs.cmp_frac(fracs.sub_frac([1,2], [1,2]), [0,1]), 0)

    def test_mul_frac(self):
        self.assertIs(fracs.cmp_frac(fracs.mul_frac([1,1], [1,1]), [1,1]), 0)
        self.assertIs(fracs.cmp_frac(fracs.mul_frac([1,2], [1,2]), [1,4]), 0)
        self.assertIs(fracs.cmp_frac(fracs.mul_frac([1,2], [1,-2]), [1,-4]), 0)

    def test_div_frac(self):
        self.assertIs(fracs.cmp_frac(fracs.div_frac([1,1], [1,1]), [1,1]), 0)
        self.assertIs(fracs.cmp_frac(fracs.div_frac([1,2], [1,2]), [1,1]), 0)
        self.assertIs(fracs.cmp_frac(fracs.div_frac([1,2], [1,-2]), [-1,1]), 0)

    def test_is_positive(self):
        self.assertTrue(fracs.is_positive([1,2]))
        self.assertTrue(fracs.is_positive([2,1]))
        self.assertFalse(fracs.is_positive([0,2]))
        self.assertFalse(fracs.is_positive([1,-2]))
        self.assertFalse(fracs.is_positive([-1,2]))

    def test_is_zero(self):
        self.assertTrue(fracs.is_zero([0,1]))
        self.assertTrue(fracs.is_zero([0,0]))
        self.assertFalse(fracs.is_zero([2,0]))
        self.assertFalse(fracs.is_zero([2,2]))

    def test_cmp_frac(self):
        self.assertIs(fracs.cmp_frac([1,2], [2,4]), 0)
        self.assertIs(fracs.cmp_frac([0,2], [1,1]), -1)
        self.assertIs(fracs.cmp_frac([4,2], [1,2]), 1)

    def test_frac2float(self):
        self.assertIsInstance(fracs.frac2float([1,2]), float)
        self.assertIsInstance(fracs.frac2float([0,2]), float)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy