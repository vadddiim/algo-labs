def linearsearch(input_name, output_name):
  input_file = open(input_name, 'r')
  output_file = open(output_name, 'w')

  numbers = list(map(int, input_file.readline().split()))
  v = int(input_file.readline())

  repeat_indexes = []
  for i in range(len(numbers)):
    if numbers[i] == v:
      repeat_indexes.append(i)

  if len(repeat_indexes) == 0:
    output_file.write("-1")
  elif len(repeat_indexes) == 1:
    output_file.write(str(repeat_indexes[0]))
  else:
    output_file.write("{}\n".format(len(repeat_indexes)))
    output_file.write(','.join(map(str, repeat_indexes)))

  input_file.close()
  output_file.close()

if __name__ == '__main__':
  linearsearch('input.txt', 'output.txt')