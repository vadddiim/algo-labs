import unittest
from lab1.task4.src.linearsearch import linearsearch
import tempfile
import os

class PalindromeTestCase(unittest.TestCase):
    def test_linearsearch_one(self):
        input_path = tempfile.mkstemp()[1]
        outfile_path = tempfile.mkstemp()[1]

        output_file = open(outfile_path, 'r')

        input_file = open(input_path, 'w')
        input_file.write('1 2 3 4 5 6 7 8 9 0\n8\n')
        input_file.close()
        
        try:
          linearsearch(input_path, outfile_path)
          self.assertEqual(output_file.readline(), '7')
        finally:
          output_file.close()

          os.remove(input_path)
          os.remove(outfile_path)

    def test_linearsearch_zero(self):
      input_path = tempfile.mkstemp()[1]
      outfile_path = tempfile.mkstemp()[1]

      output_file = open(outfile_path, 'r')

      input_file = open(input_path, 'w')
      input_file.write('1 2 3 4 5 6 7 8 9 0\n10\n')
      input_file.close()
      
      try:
        linearsearch(input_path, outfile_path)
        self.assertEqual(output_file.readline(), '-1')
      finally:
        output_file.close()

        os.remove(input_path)
        os.remove(outfile_path)

    def test_linearsearch_multiple(self):
      input_path = tempfile.mkstemp()[1]
      outfile_path = tempfile.mkstemp()[1]

      output_file = open(outfile_path, 'r')

      input_file = open(input_path, 'w')
      input_file.write('1 2 3 4 5 6 7 8 9 0 1 1 2\n1\n')
      input_file.close()
      
      try:
        linearsearch(input_path, outfile_path)
        self.assertEqual(output_file.readline(), '3\n')
        self.assertEqual(output_file.readline(), '0,10,11')
      finally:
        output_file.close()

        os.remove(input_path)
        os.remove(outfile_path)


if __name__ == '__main__':
    unittest.main()