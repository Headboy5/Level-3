#==ACTIVITY 1==
#Sentence with a horizontal tab
print("This is the first part\tand this is after the tab.")

#Sentence with a line break
print("This is the first line.\nThis is the second line.")

user_input = input("Enter something: ")
print(f"You entered: {user_input}")

# print('\\Insert a backslash character in a \\string.')
# print(' \t Inserts a horizontal tab')
# print(' " Insert a double quote in a string e.g "cat" ')
# print(' \' Insert a single quote in a string  e.g \'dog\' ')

#==ACTIVITY 2==
#Two modes of running Python:
#   Interactive Mode: Type commands directly into the interpreter and get immediate results.
#   Script Mode: Write code in a .py file and run the whole file at once.

#Difference between expression and statement:
#   Expression: Produces a value (e.g. 2 + 3)
#   Statement: Performs an action (e.g. print("Hello"), x = 5)

#Examples of each data type:
example_string = "Hello, world!"
example_float = 3.14
example_int = 42
example_dict = {"name": "Alice", "age": 25}
example_tuple = (1, 2, 3)
example_bool = True
example_list = [1, 2, 3, 4]
example_set = {1, 2, 3}

#==ACTIVITY 3==
print(example_list)
print(example_set)
print(example_dict)
print(example_int)
print(example_bool)
print(example_float)

#Set methods and difference example
#1. add() - add item in the set
a = {1, 2, 3, 4, 5, 6, 7, 8, "banana"}
a.add("apple")
print("After add:", a)

#2. remove() - remove an item in the set
a.remove(2)
print("After remove:", a)

#3. clear() - clear the content of the set
a.clear()
print("After clear:", a)

# Find the difference between two sets using difference()
a = {1, 4, 6, 7, 8, 33, 4, "banana", "apple"}
b = {1, 2, 3, 4, 5, 6, 7, 8, "banana"}
diff = a.difference(b)
print("Difference between a and b:", diff)