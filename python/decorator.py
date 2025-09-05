# A decorator function
def my_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()  # call the original function
        print("After the function is called.")
    return wrapper

# Applying decorator with @ syntax
@my_decorator
def say_hello():
    print("Hello, World!")

# Call the function
say_hello()
