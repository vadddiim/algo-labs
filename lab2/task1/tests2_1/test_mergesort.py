import unittest
from lab2.task1.src.mergesort import mergesort_file
import tempfile
import os
import random

class MergeSortTestCase(unittest.TestCase):
    def test_mergesort(self):
        input_path = tempfile.mkstemp()[1]
        outfile_path = tempfile.mkstemp()[1]

        output_file = open(outfile_path, 'r')

        array = [random.randint(0, 1000) for _ in range(10**4)]
        sorted_array = sorted(array)

        input_file = open(input_path, 'w')
        input_file.write('{}\n{}\n'.format(len(array), ' '.join(map(str, array))))
        input_file.close()
        
        try:
          mergesort_file(input_path, outfile_path)
          self.assertEqual(output_file.readline(), ' '.join(map(str, sorted_array)))
        finally:
          output_file.close()

          os.remove(input_path)
          os.remove(outfile_path)


if __name__ == '__main__':
    unittest.main()