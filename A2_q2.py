import functools

def cache_result(print_message = False):
    cache = {}

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items()))) # creates key for the cache, tuple for immutablility

            if key in cache:
                if print_message:
                    print(f"Returning result from cache for {func.__name__} with arguments: {args} and kwargs {kwargs}")
                return cache[key]
            
            else:
                result = func(*args, **kwargs)
                cache[key] = result

                if print_message:
                    print(f"Computed and cached result for {func.__name__} with args: {args} and kwargs {kwargs}")
                return result
            
        return wrapper
    return decorator

@ cache_result(print_message=True)
def quick_maths(a,b,c=0):
    print("Running function quick_maths...")
    return a * b + c

print(quick_maths(1,2))     # will compute
print(quick_maths(1,2))     # will fetch from caache
print(quick_maths(3,4,c=2))
print(quick_maths(3,4,c=2))