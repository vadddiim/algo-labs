import unittest
from lab1.task5.src.selectionsort import selectionsort
import tempfile
import os

class PalindromeTestCase(unittest.TestCase):
    def test_selection_sort(self):
        input_path = tempfile.mkstemp()[1]
        outfile_path = tempfile.mkstemp()[1]

        output_file = open(outfile_path, 'r')

        input_file = open(input_path, 'w')
        input_file.write('100\n996 431 423 471 928 128 288 42 936 10 21 719 175 483 187 260 518 546 751 278 675 358 169 968 895 85 591 432 698 325 750 733 692 123 585 787 840 910 617 632 891 148 501 514 651 90 48 789 299 3 794 144 308 990 366 109 838 833 205 895 153 685 273 292 308 327 496 519 675 446 563 644 124 295 309 380 181 145 524 396 762 941 476 696 142 283 449 653 853 155 55 755 834 589 372 183 158 591 285 663\n')
        input_file.close()
        
        try:
          selectionsort(input_path, outfile_path)
          self.assertEqual(output_file.readline(), '3 10 21 42 48 55 85 90 109 123 124 128 142 144 145 148 153 155 158 169 175 181 183 187 205 260 273 278 283 285 288 292 295 299 308 308 309 325 327 358 366 372 380 396 423 431 432 446 449 471 476 483 496 501 514 518 519 524 546 563 585 589 591 591 617 632 644 651 653 663 675 675 685 692 696 698 719 733 750 751 755 762 787 789 794 833 834 838 840 853 891 895 895 910 928 936 941 968 990 996')
        finally:
          output_file.close()

          os.remove(input_path)
          os.remove(outfile_path)


if __name__ == '__main__':
    unittest.main()