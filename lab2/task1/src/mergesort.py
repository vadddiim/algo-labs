import random
from utils import measure_performance

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * n1
    R = [0] * n2
    
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + 1 + j]
    
    i = j = 0
    k = p
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1

def mergesort(A, p, r):
    if p < r:
        q = (p + r) // 2
        mergesort(A, p, q)
        mergesort(A, q + 1, r)
        merge(A, p, q, r)

    return A

def mergesort_file(input_name, output_name):
  input_file = open(input_name, 'r')
  output_file = open(output_name, 'w')

  n = int(input_file.readline())
  arr = list(map(int, input_file.readline().split()))

  mergesort(arr, 0, n - 1)

  output_file.write(' '.join(map(str, arr)))

  input_file.close()
  output_file.close()

@measure_performance
def example1():
    worst_array = sorted([random.randint(0, 1000) for _ in range(10**4)], reverse=True)
    mergesort(worst_array, 0, len(worst_array) - 1)
    print("[WORST CASE]")

@measure_performance
def example2():
    best_array = sorted([random.randint(0, 1000) for _ in range(10**4)])
    mergesort(best_array, 0, len(best_array) - 1)
    print("[BEST CASE]")

@measure_performance
def example3():
    mergesort_file("input.txt", "output.txt")
    print("[FROM FILE]")

if __name__ == '__main__':
  example1()
  example2()
  example3()