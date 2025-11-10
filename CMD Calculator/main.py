def main():
    while True:
        try:
            answer = 0
            print("\nCalculator!\n")
            num1 = input("Enter the first number: ")
            num2 = input("Enter the second number: ")
            method = input("Enter the method or enter q to quit: ")
            if method == "q":
                print("Ok, bye!")
                break
            if method == "/":
                answer = divide(float(num1), float(num2))
            elif method == "*":
                answer = multiply(float(num1), float(num2))
            elif method == "+":
                answer = add(float(num1), float(num2))
            elif method == "-":
                answer = subtract(float(num1), float(num2))
            print(f"The answer is {answer}")
        except ValueError as e:
            print(f"Error: {e}\n")


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def divide(num1, num2):
    return num1 / num2


def multiply(num1, num2):
    return num1 * num2


if __name__ == "__main__":
    main()