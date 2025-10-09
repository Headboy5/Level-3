def addFunction(a,b):
    return a + b

# def greet(name, msg="Good morning!"):
#     print("Hello", name + ', ' + msg)

def divideFunction(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def addNames(name1, name2):
    print(f"My name is {name1} {name2}.")

def main():
    first_number = 2
    second_number = 3
    # result = addFunction(first_number, second_number)
    # print(result)
    result = divideFunction(first_number, second_number)
    print(result)
    # greet("Kate")
    # greet("John", "Good evening!")

if __name__ == "__main__":
    main()