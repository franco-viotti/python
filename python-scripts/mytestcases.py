import unittest

from mymodule import square, double, add

class TestingMyModule(unittest.TestCase):
    
    ## Square function test cases
    def test_square(self):
        self.assertEqual(square(2), 4)
    def test_square_w_floats(self):
        self.assertEqual(square(3.0), 9.0)
    def test_square_not(self):
        self.assertNotEqual(square(-3), -9)
    
    ## Double function test cases
    def test_double(self):
        self.assertEqual(double(2), 4)
    def test_double_w_neg(self):
        self.assertEqual(double(-3.1), -6.2)
    def test_double_w_z(self):
        self.assertEqual(double(0), 0)

    ## Add function test cases
    def test_add(self):
        self.assertEqual(add(2, 4), 6)
    def test_add_zero(self):
        self.assertEqual(add(0,0), 0)
    def test_add_floats(self):
        self.assertEqual(add(2.3, 3.6), 5.9)
    def test_add_w_strings(self):
        self.assertEqual(add('hello', 'world'), 'helloworld')
    def test_add_several_zeros(self):
        self.assertEqual(add(2.3000, 4.3000), 6.6)
    def test_not_add(self):
        self.assertNotEqual(add(-2,-2), 0)
    

unittest.main()
