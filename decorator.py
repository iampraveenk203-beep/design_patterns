"""
Decorator pattern is structural design pattern dynamically add new behavior to an existing function.
"""
# Define Decorator function
def decorator_function(orig_func):
    def wrapper():
        print("Before original function")
        orig_func()
        print("After original function")
    return wrapper

# Original method with decorator
@decorator_function
def say_hello():
    print("Hello World")

# Driver code
say_hello()