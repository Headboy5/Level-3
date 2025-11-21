def uppercase_input(user_input):
    return user_input.upper()

def add_two_numbers(num1, num2):
    return num1 + num2

def division(num1, num2):
    return num1 / num2

def multiplication(num1, num2):
    return num1 * num2

def lowercase_input(user_input):
    return user_input.lower()

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    print("Uppercase:", uppercase_input(user_input))
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Sum:", add_two_numbers(num1, num2))