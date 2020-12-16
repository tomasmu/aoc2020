import functools

def benchmark_it_arg(decorator_benchmark_it):
    @functools.wraps(decorator_benchmark_it)
    def decorator_maker(arg):
        def decorator_wrapper(function_to_decorate):
            return decorator_benchmark_it(function_to_decorate, arg)
        return decorator_wrapper
    return decorator_maker

@benchmark_it_arg
def benchmark_it(function_to_benchmark, iterations):
    @functools.wraps(function_to_benchmark)
    def function_wrapper(*function_args, **function_kwargs):
        import time

        t0 = time.perf_counter_ns()
        for _ in range(iterations):
            result = function_to_benchmark(*function_args, **function_kwargs)
        t1 = time.perf_counter_ns()

        ms = (t1 - t0)/1_000_000
        number_of_times = '' if iterations == 1 else f'{iterations} times '
        print(f'{function_to_benchmark.__name__} {number_of_times}took {ms:.4f} ms')

        return result
    return function_wrapper

def time_it(function_to_benchmark):
    @functools.wraps(function_to_benchmark)
    def function_wrapper(*function_args, **function_kwargs):
        import time

        t0 = time.perf_counter_ns()
        result = function_to_benchmark(*function_args, **function_kwargs)
        t1 = time.perf_counter_ns()

        ms = (t1 - t0)/1_000_000
        print(f'{function_to_benchmark.__name__} took {ms:.4f} ms')

        return result
    return function_wrapper
