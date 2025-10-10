#==ACTIVITY 1==#
def greaterThan3(x):
    if x > 3:
        print(f"{x} is greater than 3")
    else:
        print(f"{x} is not greater than 3")

def stayAtHome(temp):
    if temp > 30:
        print("Stay at home")
    else:
        print("I am out and about")
    #image.png

def compareTwoVariables(a, b):
    if a > b:
        print(f"a: {a} is greater than b: {b}")
    elif a == b:
        print(f"a: {a} is equal to b: {b}")
    else:
        print(f"a: {a} is less than b: {b}")

def main():
    greaterThan3(5)
    greaterThan3(2)
    stayAtHome(35)
    stayAtHome(25)
    compareTwoVariables(5, 3)
    compareTwoVariables(3, 3)

if __name__ == "__main__":
    main()