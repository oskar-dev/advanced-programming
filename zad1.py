class Student:
    name: str
    marks: list

    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return self.__avg() > 50

    def __avg(self) -> float:
        return sum(self.marks) / len(self.marks)


stud0 = Student("Student 1", [98, 30, 98, 89, 83, 59, 60])
stud1 = Student("Student 2", [12, 3, 23, 20, 12, 49, 60])

print("Studnet 1 is_passed: ", stud0.is_passed())
print("Student 2 is_passed: ", stud1.is_passed())
