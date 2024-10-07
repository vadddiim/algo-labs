import os

f = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")
a, b = map(int, f.readline().split())

o = open(os.path.join(os.path.dirname(__file__), "output.txt"), "w")
o.write(str(a + b))

f.close()
o.close()