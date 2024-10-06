import unittest
from lab1.task3.src.insertionsort_reversed import insertionsort_reversed
import tempfile
import os

class PalindromeTestCase(unittest.TestCase):
    def test_insertion_sort_reversed(self):
        input_path = tempfile.mkstemp()[1]
        outfile_path = tempfile.mkstemp()[1]

        output_file = open(outfile_path, 'r')

        input_file = open(input_path, 'w')
        input_file.write('10\n1 8 4 2 3 7 5 6 9 0\n')
        input_file.close()
        
        try:
          insertionsort_reversed(input_path, outfile_path)
          self.assertEqual(output_file.readline(), '9 8 7 6 5 4 3 2 1 0')
        finally:
          output_file.close()

          os.remove(input_path)
          os.remove(outfile_path)


if __name__ == '__main__':
    unittest.main()