import random
from utils import measure_performance

def find_max_crossing_subarray(A, low, mid, high):
    left_sum = float('-inf')
    sum = 0
    max_left = mid
    for i in range(mid, low - 1, -1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    
    right_sum = float('-inf')
    sum = 0
    max_right = mid + 1
    for j in range(mid + 1, high + 1):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    
    return (max_left, max_right, left_sum + right_sum)

def find_maximum_subarray(A, low, high):
    if high == low:
        return (low, high, A[low])
    else:
        mid = (low + high) // 2
        (left_low, left_high, left_sum) = find_maximum_subarray(A, low, mid)
        (right_low, right_high, right_sum) = find_maximum_subarray(A, mid + 1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(A, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)

def maximum_subarray_file(input_name, output_name):
    input_file = open(input_name, 'r')
    output_file = open(output_name, 'w')

    n = int(input_file.readline())
    arr = list(map(int, input_file.readline().split()))

    output_file.write(' '.join(map(str, find_maximum_subarray(arr, 0, n - 1))))

    input_file.close()
    output_file.close()

@measure_performance
def example1():
   find_maximum_subarray([random.randint(-100, 100) for _ in range(10**4)], 0, 10**4 - 1)
   print("[RANDOM 10**4 ARRAY]")

@measure_performance
def example2():
   maximum_subarray_file('../txtf/input.txt', '../txtf/output.txt')
   print("[FROM FILE]")

if __name__ == '__main__':
    example1()
    example2()