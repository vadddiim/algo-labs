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
        input_file.write('100\n536 809 65 53 949 622 611 597 456 549 33 365 620 233 745 488 813 815 149 112 753 699 869 880 778 382 202 113 809 340 494 203 666 833 645 845 177 222 741 596 338 931 140 607 66 181 928 748 323 492 453 978 393 302 411 574 300 336 780 248 94 975 873 367 37 807 579 422 183 669 154 179 672 564 35 530 2 208 154 177 502 457 537 568 82 892 697 388 805 860 326 227 798 463 244 49 136 986 257 419\n')
        input_file.close()
        
        try:
          insertionsort(input_path, outfile_path)
          self.assertEqual(output_file.readline(), '2 33 35 37 49 53 65 66 82 94 112 113 136 140 149 154 154 177 177 179 181 183 202 203 208 222 227 233 244 248 257 300 302 323 326 336 338 340 365 367 382 388 393 411 419 422 453 456 457 463 488 492 494 502 530 536 537 549 564 568 574 579 596 597 607 611 620 622 645 666 669 672 697 699 741 745 748 753 778 780 798 805 807 809 809 813 815 833 845 860 869 873 880 892 928 931 949 975 978 986')
        finally:
          output_file.close()

          os.remove(input_path)
          os.remove(outfile_path)


if __name__ == '__main__':
    unittest.main()