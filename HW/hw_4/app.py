from helper import*

task(1)
print(square(15))


task(2)
print_arguments(name="John",
                last_name="Smith",
                age=35,
                position="web developer")
task(3)

my_list = [20, -3, 15, 2, -1, -21]
positiveNum(my_list)

task(4)
multNumb(my_list)


task(5)
@calculate_time
def square(a, b):
    return (a * b)


result = square(30,3)
print(result)


task(6)
result_add = add(10, 5)
print("Addition:", result_add)

result_subtract = subtract(20, 7)
print("Subtraction:", result_subtract)

result_multiply = multiply(8, 4)
print("Multiplication:", result_multiply)

result_divide = divide(100, 10)
print("Division:", result_divide)




print(add(10,3))