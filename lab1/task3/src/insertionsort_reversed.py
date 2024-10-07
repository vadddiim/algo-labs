def insertionsort_reversed(input_name, output_name):
  input_file = open(input_name, 'r')
  output_file = open(output_name, 'w')

  n = int(input_file.readline())
  arr = list(map(int, input_file.readline().split()))

  for i in range(1, n):
    j = i
    while j > 0 and arr[j - 1] < arr[j]:
        arr[j], arr[j - 1] = arr[j - 1], arr[j]
        j -= 1

  output_file.write(' '.join(map(str, arr)))

  input_file.close()
  output_file.close()

if __name__ == '__main__':
  insertionsort_reversed('input.txt', 'output.txt')