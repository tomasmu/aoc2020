import functools

# def decorator_with_args(decorator_to_enhance):
#     print("decorator_with_args(d)", "got decorator_to_enhance", decorator_to_enhance.__name__)
#     @functools.wraps(decorator_to_enhance)
#     def decorator_maker(*args, **kwargs):
#         print("decorator_maker(a, k) got", "args:", *args, "kwargs:", **kwargs)
#         def decorator_wrapper(function_to_decorate):
#             print("decorator_wrapper(f) got", "function_to_decorate", function_to_decorate.__name__)
#             return decorator_to_enhance(function_to_decorate, *args, **kwargs)
#         return decorator_wrapper
#     return decorator_maker

# @decorator_with_args 
# def decorated_decorator(function_to_decorate, *args, **kwargs): 
#     print("decorated_decorator(f, a, k) got", "function_to_decorate", function_to_decorate.__name__, "args:", *args, "kwargs:", **kwargs)
#     @functools.wraps(function_to_decorate)
#     def function_wrapper(function_arg):
#         print("wrapper(a) got", function_arg)
#         return function_to_decorate(function_arg)
#     return function_wrapper

# @decorated_decorator("art", "deco-rator")
# def decorated_function(function_arg):
#     print("decorated_function(a) got", function_arg)
#     return "return = " + function_arg

def benchmark_it_arg(decorator_benchmark_it):
    print("benchmark_it_arg(d)", "got decorator_benchmark_it", decorator_benchmark_it.__name__)
    @functools.wraps(decorator_benchmark_it)
    def decorator_maker(arg):
        print("decorator_maker(a) got", "arg:", arg)
        def decorator_wrapper(function_to_decorate):
            #print("decorator_wrapper(f) got", "function_to_decorate", function_to_decorate.__name__)
            return decorator_benchmark_it(function_to_decorate, arg)
        return decorator_wrapper
    return decorator_maker

@benchmark_it_arg
def benchmark_it(function_to_benchmark, iterations):
    print("function_to_benchmark", function_to_benchmark.__name__, "iterations", iterations)
    @functools.wraps(function_to_benchmark)
    def function_wrapper(*function_args, **function_kwargs):
        #print("wrapper got args", *function_args, "kwargs", **function_kwargs)
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

def time_it(function_to_decorate):
    #can i express this in terms of benchmark_it?
    return None
