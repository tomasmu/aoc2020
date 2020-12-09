import time

def decorator_with_parameters(function):
    def decorator(*args, **kwargs):
        def func(f):
            return function(f, *args, **kwargs)
        return func
    return decorator

@decorator_with_parameters
def benchmark_it(function, iterations):
    def func(*args, **kwargs):
        t0 = time.time()
        for _ in range(iterations):
            result = function(*args, **kwargs)
        t1 = time.time()

        plural_s = '' if iterations == 1 else 's'
        print(f'{function.__name__} {iterations} time{plural_s} took {1000*(t1 - t0):.6f} ms')
        return result

    return func

def time_it(func):
    def f(*args):
        t0 = time.time()
        result = func(*args)
        t1 = time.time()

        print(f'{func.__name__} took {1000*(t1 - t0):.6f} ms')
        return result

    return f
