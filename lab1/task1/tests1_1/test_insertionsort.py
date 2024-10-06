import unittest
from lab1.task1.src.insertionsort import insertionsort
import tempfile
import os

class PalindromeTestCase(unittest.TestCase):
    def test_insertion_sort(self):
        input_path = tempfile.mkstemp()[1]
        outfile_path = tempfile.mkstemp()[1]

        output_file = open(outfile_path, 'r')

        input_file = open(input_path, 'w')
        input_file.write('6\n31 41 59 26 41 58\n')
        input_file.close()
        
        try:
          insertionsort(input_path, outfile_path)
          self.assertEqual(output_file.readline(), '26 31 41 41 58 59')
        finally:
          output_file.close()

          os.remove(input_path)
          os.remove(outfile_path)


if __name__ == '__main__':
    unittest.main()