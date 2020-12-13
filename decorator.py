#todo: put somewhere and push
import functools

def decorator_with_args(decorator_to_enhance):
    print("decorator_with_args(d)", "got decorator_to_enhance", decorator_to_enhance.__name__)
    @functools.wraps(decorator_to_enhance)
    def decorator_maker(*args, **kwargs):
        print("decorator_maker(a, k) got", "args:", *args, "kwargs:", **kwargs)
        def decorator_wrapper(function_to_decorate):
            print("decorator_wrapper(f) got", "function_to_decorate", function_to_decorate.__name__)
            return decorator_to_enhance(function_to_decorate, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker

@decorator_with_args 
def decorated_decorator(function_to_decorate, *args, **kwargs): 
    print("decorated_decorator(f, a, k) got", "function_to_decorate", function_to_decorate.__name__, "args:", *args, "kwargs:", **kwargs)
    @functools.wraps(function_to_decorate)
    def wrapper(function_arg):
        print("wrapper(a) got", function_arg)
        return function_to_decorate(function_arg)
    return wrapper

@decorated_decorator(1000, 2)
def decorated_function(function_arg):
    print("decorated_function(a) got", function_arg)
    return "return = " + function_arg

decorated_function("hello world")
print("decorated_function =", decorated_function.__name__)
print("decorated_decorator =", decorated_decorator.__name__)
