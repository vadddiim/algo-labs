import time
import tracemalloc

def insertionsort(input_name, output_name):
  input_file = open(input_name, 'r')
  output_file = open(output_name, 'w')

  n = int(input_file.readline())
  arr = list(map(int, input_file.readline().split()))

  for i in range(1, n):
    key = arr[i]
    j = i - 1

    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

  output_file.write(' '.join(map(str, arr)))

  input_file.close()
  output_file.close()

if __name__ == '__main__':
  t_start = time.perf_counter()
  tracemalloc.start()

  insertionsort('input.txt', 'output.txt')

  print("Program took {} ms and {} MB".format(round(time.perf_counter() - t_start, 5), round(tracemalloc.get_traced_memory()[1] / (2**20), 5)))