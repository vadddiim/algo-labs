def insertionsort_indexes(input_name, output_name):
  input_file = open(input_name, 'r')
  output_file = open(output_name, 'w')

  n = int(input_file.readline())
  arr = list(map(int, input_file.readline().split()))
  indexes = list(range(1, n + 1))

  for i in range(1, n):
    key = arr[i]
    j = i - 1

    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
    indexes[i] = j + 2

  output_file.write(' '.join(map(str, indexes)) + "\n")
  output_file.write(' '.join(map(str, arr)))

  input_file.close()
  output_file.close()

if __name__ == '__main__':
  insertionsort_indexes('input.txt', 'output.txt')