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


def health_simulation():
    health = float(input("Enter the initial health of the character: "))

    while health > 0:
        damage = float(input("Enter the damage dealt to the character: "))

        if not isinstance(damage, (int, float)):
            print("Please enter a valid numeric value for damage.")
            continue

        health -= damage

        if health <= 0:
            print("Game over! The character's health is depleted.")
        else:
            print(f"The character's health is now {health}.")

        # play_again = input("Do you want to continue? (yes/no): ")
        #
        # if play_again.lower() != 'yes':
        #     break
        #
def health_simulation2():
    health = float(input("Enter the initial health of the character: "))

    while health > 0:
        damage = float(input("Enter the damage dealt to the character: "))

        if not isinstance(damage, (int, float)):
            print("Please enter a valid numeric value for damage.")
            continue

        health -= damage

        if health > 0:
            print(f"The character's health is now {health}.True , Game on")

        else:
            print("Game over! The character's health is depleted.")

def health_simulation3():
    health = float(input("Enter the initial health of the character: "))
    damage = float(input("Enter the damage dealt to the character: "))

    while health > 0:
        if not isinstance(damage, (int, float)):
            print("Please enter a valid numeric value for damage.")
            break

        health -= damage

        if health > 0:
            print(f"The character's health is now {health}. True, Game on")
        else:
            print("Game over! The character's health is depleted.")




