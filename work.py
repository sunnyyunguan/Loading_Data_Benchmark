# profile decorator to measure and report time and memory
# this is from https://hakibenita.com/fast-load-data-python-postgresql
import time
from functools import wraps
from memory_profiler import memory_usage

def profile(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        fn_kwargs_str = ', '.join(f'{k}={v}' for k, v in kwargs.items())
        print(f'\n{fn.__name__}({fn_kwargs_str})')

        # returns the float value of time in seconds
        t = time.perf_counter() 
        retval = fn(*args, **kwargs)
        elapsed = time.perf_counter() - t
        print(f'Elapsed Time {elapsed:0.4}')

        # output the peak memory (the difference between the starting value of the Mem Usage column and the high watermark
        mem, retval = memory_usage((fn, args, kwargs), retval=True, timeout=200, interval=1e-7)
        print(f'Peak Memory {max(mem) - min(mem)}')
        return retval

    return inner

@profile
def work(n):
    for i in range(n):
        2 ** n
        
if __name__ == '__main__':
    work(n=10)
    
    work(n=10000)