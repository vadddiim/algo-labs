from utils import measure_performance, writefile

def binarysearch(arr, x, reversed=False):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val < x:
            low = mid + 1
        elif mid_val > x:
            high = mid - 1
        else:
            result = mid
            if reversed:
                low = mid + 1
            else:
                high = mid - 1
        
    return result

def binarysearch_file(input_name, output_name):
    input_file = open(input_name, 'r')

    n = int(input_file.readline())
    array = list(map(int, input_file.readline().split()))
    k = int(input_file.readline())
    queries = list(map(int, input_file.readline().split()))

    results = [binarysearch(array, query) for query in queries]

    writefile(output_name, ' '.join(map(str, results)))

    input_file.close()

@measure_performance
def main():
    binarysearch_file("../txtf/input.txt", "../txtf/output.txt")
    print("[FROM FILE]")

if __name__ == '__main__':
    main()