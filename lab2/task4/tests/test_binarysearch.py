import unittest
from lab2.task4.src.binarysearch import binarysearch_file
import os
from utils import create_temp_files, writefile

class BinarySearchTestCase(unittest.TestCase):
    def test_binarysearch(self):
        input_path, outfile_path = create_temp_files()

        output_file = open(outfile_path, 'r')

        writefile(input_path, "5\n1 5 8 12 13\n5\n8 1 24 1 11\n")
        
        try:
          binarysearch_file(input_path, outfile_path)
          self.assertEqual(output_file.readline(), "2 0 -1 0 -1")
        finally:
          output_file.close()

          os.remove(input_path)
          os.remove(outfile_path)


if __name__ == '__main__':
    unittest.main()