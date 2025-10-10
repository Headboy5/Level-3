#==ACTIVITY 1==#
def greaterThan3(x):
    if x > 3:
        print(f"{x} is greater than 3")
    else:
        print(f"{x} is not greater than 3")

def stayAtHome(temp):
    if temp > 30:
        print("Stay at home")
    elif temp < 30:
        print("I am out and about")
    else:
        print("Persish")
    #image.png

def compareTwoVariables(a, b):
    if a > b:
        print(f"a: {a} is greater than b: {b}")
    elif a == b:
        print(f"a: {a} is equal to b: {b}")
    else:
        print(f"a: {a} is less than b: {b}")

#==ACTIVITY 2==#

def printEvenNumbers(numbers):
    print("Even numbers:")
    for number in numbers:
        if number % 2 == 0:
            print(number)
        else:
            continue

def printOddNumbers(numbers):
    print("Odd numbers:")
    for number in numbers:
        if number % 2 != 0:
            print(number)
        else:
            continue

def printUntil(values, stop_value):
    print(f"Printing values until {stop_value}:")
    for value in values:
        if value == stop_value:
            print(value)
            break
        print(value)

def compareThreeVariables(a, b, c):
    if a > b:
        print("a is higher")
    elif a == b:
        print("a and b are equal")
    if b < a:
        print("b is lower")
    if b > c:
        print("b is bigger")
    print("have a nice day")

def bettercompareThreeVariables(a, b, c):
    if a > b and a > c:
        print("a is highest")
    elif b > a and b > c:
        print("b is highest")
    elif c > a and c > b:
        print("c is highest")
    else:
        print("some or all are equal")

def main():
    greaterThan3(5)
    greaterThan3(2)
    stayAtHome(35)
    stayAtHome(25)
    stayAtHome(30)
    compareTwoVariables(5, 3)
    compareTwoVariables(3, 3)
    numbers = [ 951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941]
    printEvenNumbers(numbers)
    printOddNumbers(numbers)
    printUntil(numbers, 501)
    compareThreeVariables(165, 45, 10)
    bettercompareThreeVariables(165, 45, 10)
    printUntil(["mango","apple", "chair", "pen", "cat"], "pen")


if __name__ == "__main__":
    main()