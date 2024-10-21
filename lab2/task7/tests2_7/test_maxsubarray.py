import unittest
from lab2.task7.src.max_subarray import maximum_subarray_file
import tempfile
import os

class BinarySearchTestCase(unittest.TestCase):
    def test_binarysearch(self):
        input_path = tempfile.mkstemp()[1]
        outfile_path = tempfile.mkstemp()[1]

        output_file = open(outfile_path, 'r')

        input_file = open(input_path, 'w')
        input_file.write("10\n-2 1 -3 4 -1 2 1 -5 4 -1")
        input_file.close()
        
        try:
          maximum_subarray_file(input_path, outfile_path)
          self.assertEqual(output_file.readline(), "3 6 6")
        finally:
          output_file.close()

          os.remove(input_path)
          os.remove(outfile_path)


if __name__ == '__main__':
    unittest.main()