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

def triplePrint(a,b,c):
    print(a)
    print(b)
    print(c)

def printNumber(num = 273):
    print(num)

def secondFunction():
    print("Hello this is my second function")

def printThird(a):
    print(a[2])

cubeNumber = lambda x: x**3

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
    triplePrint("Apple", "Banana", "Cherry")
    printNumber()
    printNumber(42)
    secondFunction()
    printThird(("first", "second", "third", "fourth"))
    print(cubeNumber(4))

if __name__ == "__main__":
    main()
