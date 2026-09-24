import time

## creating a decorator wrapper which calucalte the 
##execution of the function time  


def measure_time(func):

    def wrapper(*args, **kwargs):

        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        exection_time = end_time -start_time

        print(f"Function {func.__name__} executed in  {exection_time:.4f} seconds")

        return result

    return wrapper

lst = list(range(1,10000000))

@measure_time
# def slow_function():
#     print("Function is running")
#     for i in lst:
#         pass
#     print("Function is finished")

def slow_function():
    print("fuction is running")
    time.sleep(2)
    print("function is finished")
    

slow_function()