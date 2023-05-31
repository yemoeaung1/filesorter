
# import library
import unittest
import main
from file_module import File
 
# create a class
class TestXXXXX(unittest.TestCase):

    
    def test(self):
        filepath = "CSE320.pdf"
        file = File(filepath)
        self.assertEqual(file.parseClassCode(), "CSE32")