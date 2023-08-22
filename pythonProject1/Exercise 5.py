import math


def main():
    print("Calculator")
    number1 = float(input("Give the first number: "))
    number2 = float(input("Give the second number: "))

    while True:
        print_menu(number1, number2)
        choice = input("Please select something (1-8): ")

        if choice == '1':
            result = number1 + number2
            print("The result is:", result)
        elif choice == '2':
            result = number1 - number2
            print("The result is:", result)
        elif choice == '3':
            result = number1 * number2
            print("The result is:", result)
        elif choice == '4':
            if number2 == 0:
                print("Cannot divide by zero!")
            else:
                result = number1 / number2
                print("The result is:", result)
        elif choice == '5':
            result = math.sin(number1 / number2)
            print("The result is:", result)
        elif choice == '6':
            result = math.cos(number1 / number2)
            print("The result is:", result)
        elif choice == '7':
            number1 = float(input("Give the first number: "))
            number2 = float(input("Give the second number: "))
        elif choice == '8':
            print("Thank you!")
            break
        else:
            print("Invalid input. Please select something between 1 and 8.")


def print_menu(number1, number2):
    print("(1) +")
    print("(2) -")
    print("(3) *")
    print("(4) /")
    print("(5) sin(number1/number2)")
    print("(6) cos(number1/number2)")
    print("(7) Change numbers")
    print("(8) Quit")
    print(f"Current numbers: {number1} {number2}")


if __name__ == "__main__":
    main()
