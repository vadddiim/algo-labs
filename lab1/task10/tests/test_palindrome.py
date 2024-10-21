import unittest
from lab1.task10.src.palindrome import palindrome
import tempfile
import os

class PalindromeTestCase(unittest.TestCase):
    def test_palindrome_AAB(self):
        input_path = tempfile.mkstemp()[1]
        outfile_path = tempfile.mkstemp()[1]

        output_file = open(outfile_path, 'r')

        input_file = open(input_path, 'w')
        input_file.write('3\nAAB\n')
        input_file.close()
        
        try:
          palindrome(input_path, outfile_path)
          self.assertEqual(output_file.readline(), 'ABA')
        finally:
          output_file.close()

          os.remove(input_path)
          os.remove(outfile_path)
          
    def test_palindrome_QAZQAZ(self):
        input_path = tempfile.mkstemp()[1]
        outfile_path = tempfile.mkstemp()[1]

        output_file = open(outfile_path, 'r')

        input_file = open(input_path, 'w')
        input_file.write('6\nQAZQAZ\n')
        input_file.close()
        
        try:
          palindrome(input_path, outfile_path)
          self.assertEqual(output_file.readline(), 'AQZZQA')
        finally:
          output_file.close()

          os.remove(input_path)
          os.remove(outfile_path)

    def test_palindrome_ABCDEF(self):
        input_path = tempfile.mkstemp()[1]
        outfile_path = tempfile.mkstemp()[1]

        output_file = open(outfile_path, 'r')

        input_file = open(input_path, 'w')
        input_file.write('6\nABCDEF\n')
        input_file.close()
        
        try:
          palindrome(input_path, outfile_path)
          self.assertEqual(output_file.readline(), 'A')
        finally:
          output_file.close()

          os.remove(input_path)
          os.remove(outfile_path)


if __name__ == '__main__':
    unittest.main()