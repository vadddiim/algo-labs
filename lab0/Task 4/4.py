import time
import os

t_start = time.perf_counter()

f = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")
n = int(f.readline())

o = open(os.path.join(os.path.dirname(__file__), "output.txt"), "w")

if n <= 1:
    o.write(str(n))
else:
  a, b = 0, 1
  for _ in range(2, n + 1):
        a, b = b, a + b

  o.write(str(b % 10))

f.close()
o.close()

print("Время выполнения %s секунд" % (time.perf_counter() - t_start))