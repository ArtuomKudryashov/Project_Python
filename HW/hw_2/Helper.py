def  Health(a):
    if not isinstance(a,(int,float)):
        print("Enter digits")
    elif a <= 0:
        print("False,  Game over")
    else:
        print("True , Game on")


def task(a):
    print("Task" + str(a))


def number (a):
    if not isinstance(a,(int,float)):
        print("Enter digits")
    elif a % 2 !=0:
        print("The number is odd")
    else:
        print("The number  is Even ")



def yearIsLeap(a):
    if((a % 4 == 0 and a % 100 != 0)or a % 400 ==0):
        print("Year is leap")
    else:
        print('Year is not leap')


def textRepeater(a,b):
    print(a*b)


def calculator(a, b, operator):
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







