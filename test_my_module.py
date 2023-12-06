import unittest
from my_module import add_numbers

class TestMyModule(unittest.TestCase):

    def test_add_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5, "Expected resultdfsdfsdfsffsddsdsd")
    
    def test_add_numbers_negative(self):
        result = add_numbers(-2, 3)
        self.assertEqual(result, 1, "Expected resultdfsdfsdfsffsddsdsd")

if __name__ == '__main__':
    unittest.main()
    

  
