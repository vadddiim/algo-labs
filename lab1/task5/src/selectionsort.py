def selectionsort(input_name, output_name):
  input_file = open(input_name, 'r')
  output_file = open(output_name, 'w')

  n = int(input_file.readline())
  arr = list(map(int, input_file.readline().split()))

  for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    (arr[i], arr[min_index]) = (arr[min_index], arr[i])

  output_file.write(' '.join(map(str, arr)))

  input_file.close()
  output_file.close()

if __name__ == '__main__':
  selectionsort('input.txt', 'output.txt')