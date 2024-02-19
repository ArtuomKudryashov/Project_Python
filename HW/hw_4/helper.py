import math
from functools import reduce


def task(n):
    ll = "<<<<<<<<<<<<<<<<<<<<< "
    rl =" >>>>>>>>>>>>>>>>>>>>>"
    print(ll+ "Task #" + str(n)+ rl)


def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = math.sqrt(2) * side
    return (perimeter, area, diagonal)


def print_arguments(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def positiveNum(my_list):
    positNumb = list(filter(lambda x: x>0, my_list))
    print(positNumb)


def multNumb(my_list):
    multTotal = reduce(lambda x, y: x*y, my_list)
    print(multTotal)



import time

def calculate_time(original):
    def wrapper_function(*args, **kwargs):
        print("Before")
        start = time.time_ns()
        result = original(*args, **kwargs)
        end = time.time_ns()
        print("After")
        print(f"Execution time: {(end - start)/1_000_000} milliseconds")
        return result
    return wrapper_function







def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b

