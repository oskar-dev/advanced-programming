# 2. Stworzyć następujące klasy:
#     - Library (klasa opisująca bibliotekę), posiadająca pola:
#         - city
#         - street
#         - zip_code
#         - open_hours (str)
#         - phone
#     - Employee (klasa opisująca pracownika biblioteki), posiadająca pola:
#         - first_name
#         - last_name
#         - hire_date
#         - birth_date
#         - city
#         - street
#         - zip_code
#         - phone
#     - Book (klasa opisująca książkę), posiadająca pola
#         - library
#         - publication_date
#         - author_name
#         - author_surname
#         - number_of_pages
#     - Order (klasa opisująca zamówienie), posiadająca pola:
#         - employee
#         - student
#         - books (lista obiektów klasy Book)
#         - order_date
from typing import OrderedDict


class Library:
    def __init__(
        self, city: str, street: str, zip_code: str, open_hours: str, phone: str
    ) -> None:
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._open_hours = open_hours
        self._phone = phone

    def __str__(self) -> str:
        return f"Library({self._city}, {self._street}, {self._zip_code}, {self._open_hours}, {self._phone})"


class Employee:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        hire_date: str,
        birth_date: str,
        city: str,
        street: str,
        zip_code: str,
        phone: str,
    ) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._hire_date = hire_date
        self._birth_date = birth_date
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._phone = phone

    def __str__(self) -> str:
        return f"Employee({self._first_name}, {self._last_name}, {self._hire_date}, {self._birth_date}, {self._city}, {self._street}, {self._zip_code}, {self._phone})"


class Student:
    def __init__(self, name: str, marks: list):
        self._name = name
        self._marks = marks

    def is_passed(self) -> bool:
        return self.__avg() > 50

    def __avg(self) -> float:
        return sum(self._marks) / len(self._marks)

    def __str__(self) -> str:
        return f"Student({self._name}, {self._marks})"


class Book:
    def __init__(
        self,
        lib: Library,
        publication_date: str,
        author_name: str,
        author_surname: str,
        number_of_pages: int,
    ) -> None:
        self._library = lib
        self._publication_date = publication_date
        self._author_name = author_name
        self._author_surname = author_surname
        self._number_of_pages = number_of_pages

    def __str__(self) -> str:
        return f"Book({self._library}, {self._publication_date}, {self._author_name}, pages={self._number_of_pages})"


class Order:
    def __init__(
        self, employee: Employee, student: Student, books: list, order_date: str
    ) -> None:
        self._employee = employee
        self._student = student
        self._books = books
        self._order_date = order_date

    def __str__(self) -> str:
        books_str = ""
        for book in self._books:
            books_str += f" {book}"

        return (
            f"Order({self._employee}, {self._student}, {books_str}, {self._order_date})"
        )


lib0 = Library("Katowice", "Bogucicka 5", "40-000", "09:00-18:00", "+48123456789")
lib1 = Library("Sosnowiec", "Koscielna", "41-200", "08:00-19:00", "+48987654321")

book0 = Book(lib0, "25-10-2026", "Jan", "Nowak", 456)
book1 = Book(lib1, "12-04-2023", "Adam", "Mickiewicz", 983)
book2 = Book(lib0, "09-01-1923", "Bolesław", "Prus", 231)
book3 = Book(lib1, "02-12-1882", "Aleksander", "Głowacki", 324)
book4 = Book(lib0, "02-06-2013", "Winston", "Smith", 123)

employee0 = Employee(
    "Mirosław",
    "Głowacki",
    "12-03-2023",
    "01-01-2000",
    "Sosnowiec",
    "Wysoka",
    "41-209",
    "+48987123456",
)
employee1 = Employee(
    "Adam",
    "Kowalski",
    "01-12-2010",
    "03-06-2001",
    "Sosnowiec",
    "niska",
    "41-209",
    "+4823109412",
)
employee2 = Employee(
    "Jan",
    "Wieczorek",
    "21-04-2000",
    "03-05-1954",
    "Sosnowiec",
    "średnia",
    "41-230",
    "+48123454621",
)

stud0 = Student("Student 1", [98, 30, 98, 89, 83, 59, 60])
stud1 = Student("Student 2", [12, 3, 23, 20, 12, 49, 60])

order0 = Order(employee1, stud0, [book0, book2, book1], "25-10-2026")
order1 = Order(employee0, stud1, [book3, book4, book0, book1], "23-11-2025")

print(order0)
print(order1)
