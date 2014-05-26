import csv
import sys
import unittest

from findmaxstock import CSVStock

class TestCSVStock(unittest.TestCase):
  def setUp(self):
    self.rightfile = 'rightfile.csv'
    self.wrongfile = 'wrongfile.csv'

  def tearDown(self):
    try:
      pass
    except:
      pass

  def test_success(self):
    """ positive test case """
    x = CSVStock(self.rightfile)    
    self.assertTrue(x.find_max())

  def test_invalid_csvdata(self): 
    """ negative test case """
    x = CSVStock(self.wrongfile)  
    self.assertFalse(x.find_max())

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCSVStock)
    unittest.TextTestRunner(verbosity=2).run(suite)            
    sys.exit() 
