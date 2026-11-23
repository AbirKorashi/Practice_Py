class Student:
    class_year = 2024
    num_student = 0

    def __init__(self,name,age):
        self.name= name
        self.age = age
        Student.num_student +=1

student1 = Student("Abir",23)
student2 = Student("Riyad",24)
student3 = Student("Symum",22)
student4 = Student("Ritu",19)

print(student1.name)
print(Student.num_student)

print(f"My graduation class of {Student.class_year} has {Student.num_student} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)