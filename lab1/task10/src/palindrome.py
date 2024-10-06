def count_letters(string):
  letters = {}
  for letter in string:
    if letter in letters:
      letters[letter] += 1
    else:
      letters[letter] = 1
  return letters

def palindrome(input_name, output_name):
  input_file = open(input_name, 'r')
  output_file = open(output_name, 'w')

  input_file.readline()
  letters = count_letters(input_file.readline().replace("\n", ""))

  even_part = []
  odd_part = []
  
  for letter, freq in sorted(letters.items()):
      if freq % 2 == 0:
          even_part.append(letter * (freq // 2))
      else:
          even_part.append(letter * (freq // 2))
          odd_part.append(letter)
  
  left = ''.join(even_part)
  center = odd_part[0] if odd_part else ''
  right = left[::-1]

  output_file.write(left + center + right)

  input_file.close()
  output_file.close()
    

if __name__ == '__main__':
  palindrome('input.txt', 'output.txt')
