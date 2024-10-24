import unittest
from lab2.task5.src.majority import majority_file
from utils import create_temp_files, writefile
import os

class MajorityTestCase(unittest.TestCase):
    def test_majority1(self):
        input_path, outfile_path = create_temp_files()

        output_file = open(outfile_path, 'r')

        writefile(input_path, "5\n2 3 9 2 2")
        
        try:
          majority_file(input_path, outfile_path)
          self.assertEqual(output_file.readline(), "2")
        finally:
          output_file.close()

          os.remove(input_path)
          os.remove(outfile_path)

    def test_majority2(self):
        input_path, outfile_path = create_temp_files()

        output_file = open(outfile_path, 'r')

        writefile(input_path, "4\n1 2 3 4")
        
        try:
          majority_file(input_path, outfile_path)
          self.assertEqual(output_file.readline(), "-1")
        finally:
          output_file.close()

          os.remove(input_path)
          os.remove(outfile_path)


if __name__ == '__main__':
    unittest.main()