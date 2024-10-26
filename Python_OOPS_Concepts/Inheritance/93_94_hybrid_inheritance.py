class University:
    def __init__(self, university_name):
        self.university_name = university_name

    def show_details(self):
        print(f"University name: {self.university_name}")

class Course(University):
    def __init__(self,university_name):
        super().__init__(university_name)
        self.course_name = "Master of Computer Application"

    def show_details(self):
        print(f"Course name: {self.course_name}")

class Branch(University):
    def __init__(self,university_name):
        super().__init__(university_name)
        self.branch_name = "CODE"

    def show_details(self):
        University.show_details(self)
        print(f"Branch name: {self.branch_name}")


class Student(Course, Branch):
    def __init__(self,university_name,student_name):
        super().__init__(university_name)
        self.student_name = student_name

    def show_details(self):
        Course.show_details(self)
        Branch.show_details(self)
        print(f"Student name: {self.student_name}")

class Faculty(Course, Branch):
    def __init__(self,university_name,faculty_name):
        super().__init__(university_name)
        self.faculty_name = faculty_name

    def show_details(self):
        Course.show_details(self)
        Branch.show_details(self)
        print(f"Faculty name: {self.faculty_name}")

# faculty_1 = Faculty("Anna University", "Jenny")
# faculty_1.show_details()

student_1 = Student("Anna University", "Neeraj")
student_1.show_details()
print(Student.mro())

#Lec - 94 (Dimond problem full theory)
