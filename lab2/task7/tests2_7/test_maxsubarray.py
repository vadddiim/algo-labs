import unittest
from lab2.task7.src.max_subarray import maximum_subarray_file
from utils import create_temp_files, writefile
import os

class MaxSubArrayTestCase(unittest.TestCase):
    def test_maxsubarray(self):
        input_path, outfile_path = create_temp_files()

        output_file = open(outfile_path, 'r')

        writefile(input_path, "10\n-2 1 -3 4 -1 2 1 -5 4 -1")
        
        try:
          maximum_subarray_file(input_path, outfile_path)
          self.assertEqual(output_file.readline(), "3 6 6")
        finally:
          output_file.close()

          os.remove(input_path)
          os.remove(outfile_path)


if __name__ == '__main__':
    unittest.main()