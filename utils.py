from functools import wraps
import tracemalloc
from time import perf_counter_ns

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