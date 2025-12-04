from pathlib import Path
filedir = Path(__file__).parent
def activity1(filedir):
    try:
        file1 = open(filedir / "test.txt", 'x')
        file1.close()
    except FileExistsError:
        pass
    file1 = open(filedir / "test.txt", 'r+')
    print("Initial file content:")
    print(file1.read())
    file1.close()
    file1 = open(filedir / "test.txt", 'r+')
    file1.write("Hello, World!\n")
    file1.write("This is a test file.")
    print("Line 1:")
    print(file1.readline())
    print("All lines in the file:")
    print(file1.readlines())
    file1.close()

def activity2(filedir):
    try:
        file1 = open(filedir / "activity2.txt", 'x')
        file1.close()
    except FileExistsError:
        pass
    file1 = open(filedir / "activity2.txt", 'w+')
    for i in range(1, 6):
        file1.write(f"This is line number {i}\n")
    print("File content after writing 5 lines:")
    print(file1.read())
    print(file1.tell())
    file1.seek(0)
    print("File content after seeking to the beginning:")
    print(file1.read())
    file1.close()

# Define in ONE sentence the meaning of these file methods 
# Give a working example of how they are used with files

# a. next()
# b. tell()
# c. mode()
# d. name()

def activity3(filedir):
    # a. next() - This method is used to retrieve the next item from an iterator, such as a file object.
    file1 = open(filedir / "activity2.txt", 'r')
    print("Using next() to read lines from the file:")
    print(next(file1))  # Reads the first line
    # b. tell() - This method returns the current position of the file pointer within the file.
    file1.seek(0)  # Move the pointer back to the beginning
    position = file1.tell()
    print(f"Current file pointer position after reading one line: {position}")
    # c. mode() - This attribute returns the mode in which the file was opened (e.g., 'r', 'w', 'a').
    print(f"File mode: {file1.mode}")
    # d. name() - This attribute returns the name of the file.
    print(f"File name: {file1.name}")
    file1.close()

def main():
    print("===Activity 1===")
    activity1(filedir)
    print("===Activity 2===")
    activity2(filedir)
    print("===Activity 3===")
    activity3(filedir)
if __name__ == "__main__":
    main()