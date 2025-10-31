"""
What is a Syntax error and give three examples.
A Syntax error in programming occurs when the code written does not conform to the rules and structure of the programming language.
This prevents the code from being executed because the interpreter or compiler cannot understand it.
Syntax errors are typically identified during the parsing stage before the program runs.

Example 1: Missing colon at the end of a function definition
    # def foo()
    #     print("missing colon")

    # def foo():
    #     print("correct")

Example 2: Unmatched parentheses
    # print("Hello, World!"

    # print("Hello, World!")

Example 3: Incorrect indentation
    # def another_function():
    # print("This will cause an indentation error")

    # def another_function():
    #     print("This is correctly indented")

"""

# Scenario demonstrating IndexError, AttributeError, IndentationError, and NameError
# All in one cohesive student grade processing scenario

def process_student_grades():
    """
    A scenario that demonstrates all four error types:
    - IndexError: accessing list index out of range
    - AttributeError: calling method that doesn't exist on object
    - NameError: using undefined variable
    - IndentationError: incorrect indentation
    """
    
    # Sample student data
    students = ["Alice", "Bob", "Charlie"]
    grades = [85, 92, 78]
    
    print("Processing student grades...\n")
    
    # 1. IndexError - trying to access index that doesn't exist
    try:
        print(f"Student 1: {students[0]} - Grade: {grades[0]}")
        print(f"Student 2: {students[1]} - Grade: {grades[1]}")
        print(f"Student 3: {students[2]} - Grade: {grades[2]}")
        print(f"Student 4: {students[3]} - Grade: {grades[3]}")  # IndexError: list index out of range
    except IndexError as e:
        print(f"IndexError caught: {e}")
        print("Attempted to access student at index 3, but only 3 students exist (indices 0-2)\n")
    
    # 2. AttributeError - calling method that doesn't exist
    try:
        student_name = students[0]
        # Strings have .upper() but not .append()
        student_name.append("Smith")  # AttributeError: 'str' object has no attribute 'append'
    except AttributeError as e:
        print(f"AttributeError caught: {e}")
        print("Tried to call .append() on a string, but strings don't have this method\n")
    
    # 3. NameError - using undefined variable
    try:
        total_students = len(students)
        average_grade = sum(grades) / total_students
        print(f"Average grade: {average_grade}")
        # Trying to use a variable that was never defined
        print(f"Highest grade: {maximum_grade}")  # NameError: name 'maximum_grade' is not defined
    except NameError as e:
        print(f"NameError caught: {e}")
        print("Tried to use 'maximum_grade' variable before defining it\n")
    
    # 4. IndentationError - incorrect indentation (shown in commented example)
    # The following code would cause IndentationError if uncommented:
    # try:
    #     for student in students:
    #     print(student)  # IndentationError: expected an indented block
    # except IndentationError as e:
    #     print(f"IndentationError: {e}")
    
    print("Note: IndentationError is a syntax error that prevents code from running.")
    print("Example of IndentationError:")
    print("    for student in students:")
    print("    print(student)  # <- Missing indentation")

# How can you avoid syntax errors?
# 1. Use an IDE or code editor with syntax highlighting and error detection.
# 2. Regularly run your code to catch errors early.
# 3. Review and test your code in small sections to ensure correctness.
if __name__ == "__main__":
    process_student_grades()


