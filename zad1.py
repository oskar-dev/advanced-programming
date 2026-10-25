# Stworzyć klasę Student, która posiada 2 parametry (name i marks) oraz jedną metodę is_passed, która zwraca wartość logiczną,
# pozytywną gdy średnia ocen jest > 50 w przeciwnym przypadku negatywną. Następnie należy stworzyć 2 przykładowe obiekty klasy,
# tak aby dla pierwszego obiektu metoda zwracała true , a dla drugiego false.


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
