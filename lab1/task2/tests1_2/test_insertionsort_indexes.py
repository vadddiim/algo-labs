import unittest
from lab1.task2.src.insertionsort_indexes import insertionsort_indexes
import tempfile
import os

class PalindromeTestCase(unittest.TestCase):
    def test_insertion_sort_indexes(self):
        input_path = tempfile.mkstemp()[1]
        outfile_path = tempfile.mkstemp()[1]

        output_file = open(outfile_path, 'r')

        input_file = open(input_path, 'w')
        input_file.write('10\n1 8 4 2 3 7 5 6 9 0\n')
        input_file.close()
        
        try:
          insertionsort_indexes(input_path, outfile_path)
          self.assertEqual(output_file.readline(), '1 2 2 2 3 5 5 6 9 1\n')
          self.assertEqual(output_file.readline(), '0 1 2 3 4 5 6 7 8 9')
        finally:
          output_file.close()

          os.remove(input_path)
          os.remove(outfile_path)


if __name__ == '__main__':
    unittest.main()