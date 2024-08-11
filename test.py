import unittest
from main import suma, resta

class TestFunciones(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(5, 4),9)
        self.assertEqual(suma(-1, 1),0)
       
    def test_resta(self):
        self.assertEqual(resta(5, 4),1)
        self.assertEqual(resta(-1, 1),-2)
        
if __name__ == "__main__":
    unittest.main()
    