# Research the OS library and pick three functions and do the following:

# I) Briefly define the three functions.
# II) Give examples of how to use/apply them in your python development.
# 1. os.getcwd()
# Definition: This function returns the current working directory of a process.
# import os

# current_directory = os.getcwd()
# print("Current Directory:", current_directory)
# # 2. os.listdir()
# # Definition: This function returns a list of the names of the entries in the directory given by path.
# files_and_dirs = os.listdir(current_directory)
# print("Files and Directories:", files_and_dirs)
# # 3. os.mkdir()
# # Definition: This function creates a new directory at the specified path.
# new_dir_path = os.path.join(current_directory, "new_directory")
# os.mkdir(new_dir_path)  # overwrites if exists
# print("Created New Directory:", new_dir_path)

import turtle

my_wn = turtle.Screen()
turtle.speed(2000000)

for i in range(30):
    turtle.circle(5*i)
    turtle.color("red")
    turtle.circle(-5*i)
    turtle.color("blue")
    turtle.left(i)
my_wn.exitonclick()

# Make a quick research and list any three 3 python library.
# 1. NumPy
# 2. Pandas
# 3. Matplotlib

# What is the python syntax for importing a library in your development area.
# import library_name

# Look into the turtle library pick three functions of your choice and give example of each.
# 1. turtle.forward(distance)
# Example:
# turtle.forward(100)  # Moves the turtle forward by 100 units
# 2. turtle.right(angle)
# Example:
# turtle.right(90)  # Turns the turtle right by 90 degrees
# 3. turtle.circle(radius)
# Example:
# turtle.circle(50)  # Draws a circle with a radius of 50 units

# Choose two built-in functions, explain their syntax and give an example of each.
# 1. len()
# Syntax: len(s)
# Example:
# my_string = "Hello, World!"
# print(len(my_string))  # Output: 13
# 2. type()
# Syntax: type(object)
# Example:
# my_number = 42
# print(type(my_number))  # Output: <class 'int'>