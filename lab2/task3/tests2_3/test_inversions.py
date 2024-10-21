import unittest
from lab2.task3.src.inversions import inversions_file
from utils import create_temp_files, writefile
import os

class InversionsTestCase(unittest.TestCase):
    def test_inversions(self):
        input_path, outfile_path = create_temp_files()

        output_file = open(outfile_path, 'r')

        writefile(input_path, "10\n1 8 2 1 4 7 3 2 3 6")
        
        try:
          inversions_file(input_path, outfile_path)
          self.assertEqual(output_file.readline(), "17")
        finally:
          output_file.close()

          os.remove(input_path)
          os.remove(outfile_path)


if __name__ == '__main__':
    unittest.main()