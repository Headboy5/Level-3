class Student:
    def __init__(self, firstname, lastname, number, feespaid, feestotal, grade):
        self.firstname = firstname
        self.lastname = lastname
        self.number = number
        self.feespaid = feespaid
        self.feestotal = feestotal
        self.grade = grade

    def getStudentEmail(self):
        return f"{self.firstname}.{self.lastname}@leedstrinity.ac.uk"

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