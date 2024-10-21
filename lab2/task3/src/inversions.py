from lab2.task1.src.mergesort import mergesort
from utils import measure_performance, writefile

def inversions_file(input_name, output_name):
    input_file = open(input_name, 'r')

    n = int(input_file.readline())
    arr = list(map(int, input_file.readline().split()))

    _, inv_count, _ = mergesort(arr, 0, n - 1)

    writefile(output_name, str(inv_count))

    input_file.close()

@measure_performance
def main():
    inversions_file('../txtf/input.txt', '../txtf/output.txt')
    print("[FROM FILE]")

if __name__ == '__main__':
    main()