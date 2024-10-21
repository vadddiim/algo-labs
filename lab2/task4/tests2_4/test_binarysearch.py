import unittest
from lab2.task4.src.binarysearch import binarysearch_file
import tempfile
import os

class BinarySearchTestCase(unittest.TestCase):
    def test_binarysearch(self):
        input_path = tempfile.mkstemp()[1]
        outfile_path = tempfile.mkstemp()[1]

        output_file = open(outfile_path, 'r')

        input_file = open(input_path, 'w')
        input_file.write("5\n1 5 8 12 13\n5\n8 1 24 1 11\n")
        input_file.close()
        
        try:
          binarysearch_file(input_path, outfile_path)
          self.assertEqual(output_file.readline(), "2 0 -1 0 -1")
        finally:
          output_file.close()

          os.remove(input_path)
          os.remove(outfile_path)


if __name__ == '__main__':
    unittest.main()