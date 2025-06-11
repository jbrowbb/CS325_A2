import logging

# --- Question 1 (Basic Decorator for Logging) ---
print ("Question 1")

def log_function_call(func):
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(__name__)
        logger.info(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper

@log_function_call
def add(x,y):
    return x + y

# set up logging
logging.basicConfig(level=logging.INFO)

result = add(x=2,y=3)   # for kwargs