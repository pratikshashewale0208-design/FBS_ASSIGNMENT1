#Assignment17.py
class Student:

    def __init__(self, sid=0, name="", age=0, percentage=0):
        self.sid = sid
        self.name = name
        self.age = age
        self.percentage = percentage

    def accept(self):
        self.sid = int(input("Enter Student ID : "))
        self.name = input("Enter Name : ")
        self.age = int(input("Enter Age : "))
        self.percentage = float(input("Enter Percentage : "))

    def display(self):
        print("\nStudent Details")
        print("ID :", self.sid)
        print("Name :", self.name)
        print("Age :", self.age)
        print("Percentage :", self.percentage)

    def calculateRank(self):
        if self.percentage >= 90:
            print("Rank : A")
        elif self.percentage >= 75:
            print("Rank : B")
        elif self.percentage >= 60:
            print("Rank : C")
        else:
            print("Rank : D")

    def __str__(self):
        return f"Student({self.sid}, {self.name}, {self.percentage})"
print("*************************2nd***************************")
class EnggStudent(Student):

    def __init__(self, sid=0, name="", age=0, percentage=0,
                 branch="", internalMarks=0):
        super().__init__(sid, name, age, percentage)
        self.branch = branch
        self.internalMarks = internalMarks

    def accept(self):
        super().accept()
        self.branch = input("Enter Branch : ")
        self.internalMarks = int(input("Enter Internal Marks : "))

    def display(self):
        super().display()
        print("Branch :", self.branch)
        print("Internal Marks :", self.internalMarks)

    def calculateRank(self):
        total = self.percentage + self.internalMarks / 10
        print("Engineering Rank Score :", total)

    def __str__(self):
        return f"EnggStudent({self.sid}, {self.name}, {self.branch})"
print("********************3rd********************")

class MedicalStudent(Student):

    def __init__(self, sid=0, name="", age=0, percentage=0,
                 specialization="", internshipMarks=0):
        super().__init__(sid, name, age, percentage)
        self.specialization = specialization
        self.internshipMarks = internshipMarks

    def accept(self):
        super().accept()
        self.specialization = input("Enter Specialization : ")
        self.internshipMarks = int(input("Enter Internship Marks : "))

    def display(self):
        super().display()
        print("Specialization :", self.specialization)
        print("Internship Marks :", self.internshipMarks)

    def calculateRank(self):
        total = self.percentage + self.internshipMarks / 10
        print("Medical Rank Score :", total)

    def __str__(self):
        return f"MedicalStudent({self.sid}, {self.name}, {self.specialization})"
    
print("*****************************4th*************************")
class College:

    def __init__(self, size):
        self.students = []
        self.size = size

    def addStudent(self, student):
        if len(self.students) < self.size:
            self.students.append(student)
            print("Student Added Successfully")
        else:
            print("College is Full")

    def getStudent(self):
        print("\nStudent List")
        for s in self.students:
            s.display()
            s.calculateRank()

    def removeStudent(self, sid):
        for s in self.students:
            if s.sid == sid:
                self.students.remove(s)
                print("Student Removed")
                return
        print("Student Not Found")

    def __str__(self):
        return f"College has {len(self.students)} students"