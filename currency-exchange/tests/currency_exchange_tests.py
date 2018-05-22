import sys
import unittest
import app

class TestValidationMethods(unittest.TestCase):
    def test_is_float(self):
        self.assertTrue(app.is_float(1.0345))
    def test_is_currency(self):
        self.assertTrue(app.is_currency("EUR"))

class TestconversionMethods(unittest.TestCase):
    def test_normalize(self):
        self.assertEqual(app.normalize('d'), 'D')


#### allows to run the module from command line and call all the methods
if __name__ == '__main__':
    unittest.main()
    

