import unittest
from lab2.task3.src.inversions import inversions_file
import tempfile
import os

class InversionsTestCase(unittest.TestCase):
    def test_inversions(self):
        input_path = tempfile.mkstemp()[1]
        outfile_path = tempfile.mkstemp()[1]

        output_file = open(outfile_path, 'r')

        input_file = open(input_path, 'w')
        input_file.write("10\n1 8 2 1 4 7 3 2 3 6")
        input_file.close()
        
        try:
          inversions_file(input_path, outfile_path)
          self.assertEqual(output_file.readline(), "17")
        finally:
          output_file.close()

          os.remove(input_path)
          os.remove(outfile_path)


if __name__ == '__main__':
    unittest.main()