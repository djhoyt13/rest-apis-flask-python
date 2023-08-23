# list comprehension

numbers = [1, 3, 5]
doubled = [num * 2 for num in numbers]
# print(doubled)

friends = ["Rolf", "Sam", "samantha", 'Suzi', "Jen"]
starts_s =[i for i in friends if i.capitalize().startswith("S")]
# print(starts_s)

# Dictionaries
friends_age = {"Rolf": 24, "Adam": 30, "Anne": 27}

friends_age["Bob"] = 20

friends_age["Rolf"] = 20

# print(friends_age["Adam"])
# print(friends_age)

Student_attendance = {"Rolf": 96, "Adam": 80, "Anne": 100}

# for student in Student_attendance:
#     print(f"{student}: {Student_attendance[student]}%")

# for student, attendance in Student_attendance.items():
#     print(f"{student}: {attendance}")

x = Student_attendance.get('Rolf')
y = Student_attendance.get('orange')
z = Student_attendance.get('Adam')

# print(x, y, z)

# print(list(Student_attendance.items()))

# Ignoring dict variables

person = ("Bob", 42, "Mechanic")
name, age, profession = person

# print(name, profession)

# Dictionary comprehension
users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234")
]

# un_mapping = {user[1]: user for user in users}

# un_input = input("Enter your unsername: ")
# pw_input = input("Enter your password: ")

# _, username, password = un_mapping[un_input]

# if pw_input == password:
#     print(" You're In!")
# else:
#     print("Your details are incorrect")

def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return(total)

# print(multiply(1, 3, 5))

def add(x, y):
    return x + y

nums = {"x": 15, "y":25}
# print(add(**nums))

def both(*args, **kwargs):
    print(args)
    print(kwargs)

# both(1, 3, 5, name="Bob", age=25)

# Object Oriented Programing

student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}

def average(sequence):
    return sum(sequence) / len(sequence)

# print(average(student["grades"]))

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob", (100, 100, 93, 78, 90))
student2 = Student("Rolf", (80, 100, 93, 78, 70))
# print(student.name)
# print(student.grades)
# print(student.average_grade())
# print(student2.average_grade())

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # def __str__(self):
    #     return f"Person: ({self.name}, {self.age} years old)"
    
    def __repr__(self):
        return f"<Person: ('{self.name}', {self.age})>"
    
bob = Person("Bob", 35)
# print(bob)


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book: '{self.name}', '{self.book_type}', weighting {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, Book.TYPES[1], page_weight)

book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 600)

# print(book)
# print(light)

# Errors in Python

# def divide(dividend, divisor):
#     if divisor == 0:
#         raise ZeroDivisionError("Divisor cannot be 0.")
    
#     return dividend / divisor

# students = [
#     {"name": "Bob", "grades": [75, 90]},
#     {"name": "Rolf", "grades": [50]},
#     {"name": "Jen", "grades": [100, 90]},
# ]

# print("Welcome to the average grade program.")
# try:
    # for s in students:
    #     name = s["name"]
    #     grades = s["grades"]
    #     average = divide(sum(grades), len(grades))
    #     print(f"{name} averaged {average}.")
# except ZeroDivisionError as e:
#     print(f"ERROR: {name} has no grades!")
# else:
#     print("-- All students average calculated --")
# finally:
#     print("-- End of student average calculation --")

# Custom error classes

class TooManyPagesReadError(ValueError):
    pass

class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return(
            f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}>"
        )

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read {self.pages_read + pages} pages, but this book only contains {self.page_count} pages."
            )
        self.pages_read += pages
        print(f"You have now read {self.pages_read} pages out of {self.page_count}.")

python101 = Book("Python 101", 50)
# python101.read(35)
# python101.read(50)

'''
First-class Functions
'''
from operator import itemgetter

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    
    print("divide function called")
    return dividend / divisor

def calculate(*values, operator):
    print("calculate function called")
    return operator(*values)

# result = calculate(20, 4, operator=divide)
# print(result)

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]

def get_friend_name(friend):
    return friend["name"]

# print(search(friends, "Rolf Smith", get_friend_name))
# print(search(friends, "Rolf Smith", lambda friend: friend["name"]))
# print(search(friends, "Rolf Smith", itemgetter("name")))

'''
Decorators in Python
'''

user = {"username": "jose", "access_level": "guest"}

def get_admin_password():
    return "1234"

def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"{user['username']} does not have admin access"
        
    return secure_function

# get_admin_password = make_secure(get_admin_password)

# print(get_admin_password())

'''
'at' syntax for decorators
'''

import functools

user = {"username": "jose", "access_level": "guest"}

def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"{user['username']} does not have admin access"
        
    return secure_function

@make_secure
def get_admin_password():
    return "1234"

# print(get_admin_password.__name__)

'''
Decorating functions with parameters
'''

import functools

user = {"username": "jose", "access_level": "guest"}

def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"{user['username']} does not have admin access"
        
    return secure_function

@make_secure
def get_admin_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"


# print(get_admin_password("billing"))

'''
Decorators with parameters
'''

import functools

user = {"username": "jose", "access_level": "guest"}

# Decorator
def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"{user['username']} does not have {access_level} access"
            
        return secure_function
    return decorator

@make_secure("admin")
def get_admin_password():
    return "admin: 1234"


@make_secure("user")    
def get_dashboard_password():
    return "user: user_password"


# print(get_admin_password())
# print(get_dashboard_password())

user = {"username": "anna", "access_level": "admin"}

# print(get_admin_password())
# print(get_dashboard_password())

'''
Mutability in Python
'''

from typing import List, Optional

class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None): # This is bad!
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)
