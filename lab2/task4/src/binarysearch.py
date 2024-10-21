from utils import measure_performance

def binarysearch(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val < x:
            low = mid + 1
        elif mid_val > x:
            high = mid - 1
        else:
            return mid
    return -1

def binarysearch_file(input_name, output_name):
    input_file = open(input_name, 'r')
    output_file = open(output_name, 'w')

    n = int(input_file.readline())
    array = list(map(int, input_file.readline().split()))
    k = int(input_file.readline())
    queries = list(map(int, input_file.readline().split()))

    results = [binarysearch(array, query) for query in queries]

    output_file.write(' '.join(map(str, results)))

    input_file.close()
    output_file.close()

@measure_performance
def main():
    binarysearch_file("input.txt", "output.txt")
    print("[FROM FILE]")

if __name__ == '__main__':
    main()