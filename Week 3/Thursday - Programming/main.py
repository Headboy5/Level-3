def addFunction(a,b):
    return a + b

def greet(name, msg="Good morning!"):
    print("Hello", name + ', ' + msg)

def divideFunction(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def addNames(name1, name2):
    print(f"My name is {name1} {name2}.")

def squareFunction(x):
    return x**2

def repeatedPrint(msg, n):
    for _ in range(n):
        print(msg)

def main():
    first_number = 2
    second_number = 3
    # result = addFunction(first_number, second_number)
    # print(result)
    result = divideFunction(first_number, second_number)
    print(result)
    greet("Kate")
    greet("John", "Good evening!")
    addNames("John", "Doe")
    toSquare = 5
    squared_value = squareFunction(toSquare)
    print(f"The square of {toSquare} is {squared_value}.")
    repeatedPrint("Hello World!", 3)

if __name__ == "__main__":
    main()
