import sys
import unittest
import app
import models.quote_model

class TestValidationMethods(unittest.TestCase):
    def test_is_float(self):
        self.assertTrue(app.is_float(1.0345))
    def test_is_currency(self):
        self.assertTrue(app.is_currency("EUR"))

class TestConversionMethods(unittest.TestCase):
    def test_normalize(self):
        self.assertEqual(app.normalize('d'), 'D')

class TestQuoteModelMethods(unittest.TestCase):
    def test_find_by_currency_key(self):
        self.assertEqual(models.quote_model.find_by_currency_key('AUD_JPY'),"0.0120")
        self.assertNotEqual(models.quote_model.find_by_currency_key('AUD_JPY'),"0.4")
    def test_save(self):
        models.quote_model.save('AUD_JPY', "0.0128")
        self.assertEqual(models.quote_model.find_by_currency_key('AUD_JPY'),"0.0128")
    ### TODO : add 3 more tests 

#### allows to run the module from command line and call all the methods
if __name__ == '__main__':
    unittest.main()
    

