from lab2.task1.src.mergesort import mergesort
from utils import measure_performance, writefile

def mergesort_fileplus(input_name, output_name):
    input_file = open(input_name, 'r')

    n = int(input_file.readline())
    arr = list(map(int, input_file.readline().split()))

    data = []
    mergesort(arr, 0, n - 1, data)

    result = ""
    for info in data:
        result += f"{info[0]} {info[1]} {info[2]} {info[3]}\n"
    result += ' '.join(map(str, arr))
    writefile(output_name, result)

    input_file.close()
  
@measure_performance
def main():
    mergesort_fileplus('../txtf/input.txt', '../txtf/output.txt')

if __name__ == '__main__':
    main()