import time
import tracemalloc
import random

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

if __name__ == '__main__':
  worst_array = sorted([random.randint(0, 1000) for _ in range(10**4)], reverse=True)
  best_array = sorted([random.randint(0, 1000) for _ in range(10**4)])

  t_start = time.perf_counter()
  tracemalloc.start()

  mergesort(worst_array, 0, len(worst_array) - 1)
  worst_time = round((time.perf_counter() - t_start) * 1000)
  worst_memory = round(tracemalloc.get_traced_memory()[1] / (2**20), 5)

  print("[WORST CASE] Script took {} ms and {} MB".format(worst_time, worst_memory))

  t_start = time.perf_counter()
  tracemalloc.start()

  mergesort(best_array, 0, len(best_array) - 1)
  best_time = round((time.perf_counter() - t_start) * 1000)
  best_memory = round(tracemalloc.get_traced_memory()[1] / (2**20), 5)

  print("[BEST CASE] Script took {} ms and {} MB".format(best_time, best_memory))
  print("-- [AVERAGE] Script took {} ms and {} MB".format(round((worst_time + best_time) / 2), round((worst_memory + best_memory) / 2, 5)))

  t_start = time.perf_counter()
  tracemalloc.start()

  mergesort_file("input.txt", "output.txt")

  print("[FROM FILE] Script took {} ms and {} MB".format(round((time.perf_counter() - t_start) * 1000), round(tracemalloc.get_traced_memory()[1] / (2**20), 5)))