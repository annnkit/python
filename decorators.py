# def my_deco(func):
#     def wrapper():
#         print("Something is happening before function")
#         func()
#         print("Something is happening after fucntion")
#     return wrapper

# @my_deco
# def say_hello():
#     print("Hello!")

# # decorated_function = my_deco(say_hello)

# # decorated_function()

# say_hello()

# def log_decorator(func):
#     def wrapper():
#         print(f"Calling function: {func.__name__}")
#         func()
#         print(f"Function {func.__name__} finished.")
#     return wrapper

# @log_decorator
# def process_data():
#         print("Processing data....")

# process_data()


import time

def calculateTime(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        func(*args, **kwargs)
        end = time.time()
        return end-st
    return wrapper

@calculateTime
def greet(x):
    print(f"Hello Class  {x}")

func_val = greet("34-502")

print(f"function execution time is, {func_val}")
