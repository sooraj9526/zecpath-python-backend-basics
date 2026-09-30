class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

        
        self.__student_id = "STU001"

    def display_student(self):
        self.display_person()
        print("Course:", self.course)

    def display_student_id(self):
        print("Student ID:", self.__student_id)

student1 = Student("Sooraj", 22, "Python Full Stack")
student1.display_student()
student1.display_student_id()