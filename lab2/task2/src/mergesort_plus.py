from lab2.task1.src.mergesort import mergesort
from utils import measure_performance

def mergesort_fileplus(input_name, output_name):
    input_file = open(input_name, 'r')
    output_file = open(output_name, 'w')

    n = int(input_file.readline())
    arr = list(map(int, input_file.readline().split()))

    data = []
    mergesort(arr, 0, n - 1, data)

    for info in data:
        output_file.write(f"{info[0]} {info[1]} {info[2]} {info[3]}\n")
    output_file.write(' '.join(map(str, arr)))

    input_file.close()
    output_file.close()
  
@measure_performance
def main():
    mergesort_fileplus('input.txt', 'output.txt')

if __name__ == '__main__':
    main()