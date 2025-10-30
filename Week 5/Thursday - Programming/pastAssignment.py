try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.columns import Columns
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False

class Student:
    def __init__(self, firstname, lastname, number, feespaid, feestotal, grade):
        self.firstname = firstname
        self.lastname = lastname
        self.number = number
        self.feespaid = feespaid
        self.feestotal = feestotal
        self.grade = grade

    def getStudentEmail(self):
        return f"{self.number}@leedstrinity.ac.uk"

    def getFeesPaid(self):
        return self.feespaid

    def getFeesTotal(self):
        return self.feestotal

    def getBalance(self):
        return self.feestotal - self.feespaid

    def getStudentId(self):
        return self.number

    def payFees(self, amount):
        self.feespaid += amount
        print(f"Fees paid: £{amount:.2f}")
        print(f"New balance: £{self.getBalance():.2f}")
    
    def getGrade(self, score):
        grades = {5: "A", 4: "B", 3: "C", 2: "D", 1: "E", 0: "F"}
        # Validate score range
        if not isinstance(score, int) or score < 0 or score > 5:
            # Raise an exception for invalid grade values as per spec
            raise ValueError(f"Invalid grade value: {score}. Grade must be integer between 0 and 5.")

        grade = grades[score]
        print(f"{self.firstname} {self.lastname} with registration number {self.number} scored {grade}.")
        return grade

class Teacher:
    def __init__(self, firstname, lastname, salary, number):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.number = number

    
    def getTeacherEmail(self):
        return f"{self.firstname}.{self.lastname}@stafftrinity.ac.uk"

    def getSalary(self):
        return self.salary

def testStudent(student):
    print("Student Information:")
    print(f"Name: {student.firstname} {student.lastname}")
    print(f"Email: {student.getStudentEmail()}")
    print(f"Student ID: {student.getStudentId()}")
    print(f"Total Fees: £{student.getFeesTotal():.2f}")
    print(f"Fees Paid: £{student.getFeesPaid():.2f}")
    print(f"Remaining Balance: £{student.getBalance():.2f}")
    student.payFees(1000)
    print(f"Grade: {student.getGrade(student.grade)}")

def testTeacher(teacher):
    print("Teacher Information:")
    print(f"Email: {teacher.getTeacherEmail()}")
    print(f"Salary: £{teacher.getSalary():.2f}")

def school():
    student1 = Student("John", "Doe", "2513273", 2000, 5000, 4)
    teacher1 = Teacher("Jane", "Smith", 40000, "123456")
    testStudent(student1)
    testTeacher(teacher1)
    if input("Test invalid grade? (y/n): ").lower() in ['y', 'yes']:
        try:
            student1.getGrade(6)  # Invalid grade to test exception
        except ValueError as e:
            print(e)

def display_class_diagram():
    # Display a class diagram for Student and Teacher classes using Rich or plain text.
    classes = [
        {
            'title': 'Student',
            'attrs': ["firstname", "lastname", "number", "feespaid", "feestotal", "grade"],
            'methods': ["getStudentEmail()", "getFeesPaid()", "getFeesTotal()", 
                       "getBalance()", "getStudentId()", "payFees(amount)", "getGrade(score)"]
        },
        {
            'title': 'Teacher',
            'attrs': ["firstname", "lastname", "salary", "number"],
            'methods': ["getTeacherEmail()", "getSalary()"]
        }
    ]
    
    print("\nClass Representational Diagram:\n")
    
    if RICH_AVAILABLE:
        console = Console()
        panels = []
        for cls in classes:
            lines = ["Attributes:"] + [f"  - {a}" for a in cls['attrs']] + ["", "Methods:"] + [f"  + {m}" for m in cls['methods']]
            panels.append(Panel("\n".join(lines), title=cls['title'], expand=False))
        console.print(Columns(panels))
    else:
        for cls in classes:
            print(f"Class: {cls['title']}")
            print("  Attributes:")
            for attr in cls['attrs']:
                print(f"    - {attr}")
            print("  Methods:")
            for method in cls['methods']:
                print(f"    + {method}")
            print()

if __name__ == "__main__":
    school()

    if input("Display class diagram? (y/n): ").lower() in ['y', 'yes']:
        display_class_diagram()