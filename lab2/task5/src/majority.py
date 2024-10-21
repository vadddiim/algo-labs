from lab2.task1.src.mergesort import mergesort
from lab2.task4.src.binarysearch import binarysearch
from utils import measure_performance, writefile

def majority(arr):
  n = len(arr)
  mergesort(arr, 0, n - 1)
  candidate = arr[n // 2]

  first_index = binarysearch(arr, candidate)
  last_index = binarysearch(arr, candidate, True)

  if last_index - first_index + 1 > n // 2:
        return candidate
  return -1

def majority_file(input_name, output_name):
    input_file = open(input_name, 'r')

    n = int(input_file.readline())
    array = list(map(int, input_file.readline().split()))

    result = majority(array)

    writefile(output_name, str(result))

    input_file.close()

@measure_performance
def main():
    majority_file("../txtf/input.txt", "../txtf/output.txt")
    print("[FROM FILE]")

if __name__ == '__main__':
    main()