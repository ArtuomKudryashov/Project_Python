def task(a):
    print("Task" + str(a))


def math(a, b, operator):
    if operator == "+":
        result = a + b

    elif operator == "-":
        result = (a - b)
    elif operator == "*":
        result = a * b
    elif operator == "/":
        if b != 0:
            result = (a / b)
        else:
            print("Делить на ноль нельзя")
            return None
    else:
        print("Введен не верный оператор")
        return None
    print(f"Результат {a}{operator}{b} равен {result}")


def printFig(s, v, sp, c):
    print(s * v + "\n" + (s + sp * c + s + "\n") * 2 + s * v)


def number(n):
    if n // 1000 > 9 or n // 1000 == 0:
        print("Введено  некорректное число")
    else:
        print(" Тысячи ", n // 1000, "\n", "Сотни ", (n % 1000) // 100, "\n",
              "десятки ", (n % 100) // 10, "\n", "Единицы ", n % 10)


def sOfS(a, b):
    sS = (a + b) ** 2
    square_Of_Sum = a ** 2 + b ** 2

    print(f"S of S {a} and {b} equal {sS}")
    print(f"square of sum {a} and {b} equals {square_Of_Sum}")
