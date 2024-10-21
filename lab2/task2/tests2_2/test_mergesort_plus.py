import unittest
from lab2.task2.src.mergesort_plus import mergesort_fileplus
import tempfile
import os

class MergeSortPlusTestCase(unittest.TestCase):
    def test_mergesort_plus(self):
        input_path = tempfile.mkstemp()[1]
        outfile_path = tempfile.mkstemp()[1]

        output_file = open(outfile_path, 'r')

        input_file = open(input_path, 'w')
        input_file.write('4\n9 7 5 8')
        input_file.close()
        
        try:
          mergesort_fileplus(input_path, outfile_path)
          self.assertEqual(
            output_file.read(),
            "1 2 7 9\n"
            "3 4 5 8\n"
            "1 4 5 9\n"
            "5 7 8 9"
          )
        finally:
          output_file.close()

          os.remove(input_path)
          os.remove(outfile_path)


if __name__ == '__main__':
    unittest.main()