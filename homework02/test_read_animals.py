import unittest
from read_animals import breed

class TestBreed(unittest.TestCase):

    def test_breed(self):
        test_dict = {'head': 'head', 'body': 'body', 'arms': 2, 'legs': 3, 'tails': 5}

        #test input 1 of breed function
        self.assertRaises(AssertionError, breed, 10, test_dict)
        self.assertRaises(AssertionError, breed, 10.2, test_dict) 
        self.assertRaises(AssertionError, breed, 'str', test_dict)
        self.assertRaises(AssertionError, breed, [10, 10], test_dict)
        
        #test input 2 of breed function
        self.assertRaises(AssertionError, breed, test_dict, 10)
        self.assertRaises(AssertionError, breed, test_dict, 10.2) 
        self.assertRaises(AssertionError, breed, test_dict, 'str')
        self.assertRaises(AssertionError, breed, test_dict, [10, 10])

        #test both inputs of breed function
        self.assertRaises(AssertionError, breed, 10, 10)
        self.assertRaises(AssertionError, breed, 10.2, 10.2) 
        self.assertRaises(AssertionError, breed, 'str', 'str')
        self.assertRaises(AssertionError, breed, [10, 10], [10, 10])
     
if __name__ == '__main__':
    unittest.main()
