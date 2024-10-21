from functools import wraps
import tracemalloc
from time import perf_counter_ns
import tempfile

def measure_performance(func):
    '''Measure performance of a function'''

    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = perf_counter_ns()
        func(*args, **kwargs)
        _, peak = tracemalloc.get_traced_memory()
        finish_time = perf_counter_ns()
        print(f'Memory usage: {peak / 10**6:.4f} MB ')
        print(f'Time elapsed: {((finish_time - start_time) / (10 ** 6)):.2f} ms')
        print(f'{"-"*40}')
        tracemalloc.stop()
    return wrapper

def create_temp_files():
    input_path = tempfile.mkstemp()[1]
    outfile_path = tempfile.mkstemp()[1]

    return input_path, outfile_path

def writefile(path, data):
    with open(path, 'w') as file:
        file.write(data)