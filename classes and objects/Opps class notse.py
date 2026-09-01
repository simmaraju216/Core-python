class Student:
    """Just a student class"""
    total = 0
    def  __init__(self, name, age):
        self.name = name
        self.age = age
        Student.total +=1

    def display(self, phno,Branch):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Branch: {Branch}")
        print(f"Phone: {phno}")
        self.total_students()

    @classmethod
    def total_students(cls):
        print(f"Total Students: {cls.total}")

    @classmethod
    def change(cls,n):
        cls.total = n

    @staticmethod
    def just(name, age):
        if len(name) < 10 and age < 18:
            print("Name too short and age must be greater than 18")
        else:
            print("Valid credentials")



s1 = Student("John", 25)
s2 = Student("Michael", 35)
s3 = Student("Bob", 35)

s1.display(2345678,"CSE")
print()
Student.display(s1,5678998765,"CSE")
Student.total_students()
Student.change(20)
s1.change(25)
s1.total_students()
Student.total_students()
Student.just("Michael", 35)
s1.just("Michael", 20)

s1.total += 1
print(s1.total)
print(s2.total)
print(s3.total)
print(Student.total)

print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)

print(Student.__dict__)
#
#
#
#
"""
Q10. Create a class Student with:
•	class variable passing_marks = 40
•	instance attributes name, marks
•	instance method result() → prints pass/fail using class variable
•	class method update_passing_marks(cls, new_marks)
•	static method grade_category(marks) → returns "A", "B", "C" based on score ranges

"""
class Student:
    passing_marks = 40
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= Student.passing_marks:
            print(f"{self.name} : pass")
        else:
            print(f"{self.name} : fail")

    @classmethod
    def update(cls,pm):
        cls.passing_marks = pm

    @staticmethod
    def grade_category(m):
        if m >= 90:
            return "A"
        elif m >= 80:
            return "B"
        elif m >= 70:
            return "C"
        elif m >= 60:
            return "D"
        else:
            return "F"


s1 = Student("Jaya simha", 99)
s2 = Student("sohail", 98)
s3 = Student("Ganesh", 35)
s4 = Student("RK", 96)

s1.result()
s2.result()
s3.result()
s4.result()

s3.update(99)
s1.marks = 9
s3.marks = 100
s1.result()
s2.result()
s3.result()
s4.result()


print(s1.grade_category(s1.marks))

"""
Q7. Create a class Employee with:
•	instance attributes: name, base_salary
•	class variable: bonus_rate = 0.1
•	instance method: final_salary() → base_salary + (base_salary × bonus_rate)
•	class method: update_bonus(cls, new_rate) → updates bonus for all employees
•	static method: is_valid_salary(sal) → checks if salary > 0
Create two employees, show final salaries, update bonus rate, and show again.

"""
class Employee:
    bonus_rate = 0.1
    def __init__(self,name,salary):
        self.name = name
        self.base_salary = salary

    def final_salary(self):
        return self.base_salary+(self.base_salary*Employee.bonus_rate)

    @classmethod
    def update_bonus(cls,nb):
        cls.bonus_rate = nb

    @staticmethod
    def valid(sal):
        return sal > 0

e1 = Employee("Amarnath", 5000000)
e2 = Employee("Shiva", 5000001)

print(e1.final_salary())
print(e2.final_salary())
e1.update_bonus(0.2)
print(e1.final_salary())
print(e2.final_salary())


"""
Q6. Create a class Book with:
•	instance attributes title, author
•	a class variable total_books
•	a class method from_string(cls, book_str) that creates an object from "title-author" format
•	a static method is_valid_title(title) that checks if title has at least 3 characters
•	increment total_books for every book created
Demonstrate:
•	Creating books using both the constructor and the class method
•	Validating titles before creation

"""
class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books += 1

    @classmethod
    def from_strings(cls, book_str):
        title, author = book_str.split('-')
        if cls.is_valid(title):
            return cls(title, author)
        else:
            return "title is invalid"

    @staticmethod
    def is_valid(title):
        return len(title) >= 3


b1 = Book("Ramayana", "Valmeeki")
b2 = Book("Baratham", "Veeda Vyash")

print(Book.total_books)

b3 = Book.from_strings("Python-Guido")
print(b3.title)
print(b3.author)

print(Book.total_books)

print(Book.from_strings("AI-John"))


"""
Q1. Create a class Student with instance attributes name and marks.
Add an instance method is_passed() that returns True if marks > 40.
Then create 2 student objects and print whether each has passed or failed.

"""

# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def is_passed(self):
#         if self.marks>40:
#             print('passed')
#         else:
#             print('failed')
# s1=student('raju',90)
# s1.is_passed()
# s2=student('chiru',50)
# s2.is_passed()
"""
Q2. Create a class Employee with attributes name and company_name = "TechCorp".
Add a class method change_company(cls, new_name) to update the company name for all employees.
Demonstrate how this change affects all instances.

"""

class Employee:
    company_name = "TechCorp"   # Class variable

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name


emp1 = Employee("Raju")
emp2 = Employee("Sita")

print(emp1.name, "-", emp1.company_name)
print(emp2.name, "-", emp2.company_name)

Employee.change_company("InnovateTech")

print(emp1.name, "-", emp1.company_name)
print(emp2.name, "-", emp2.company_name)


"""
Q3. Create a class MathOps with a static method is_even(num) that returns True if the number is even.
Then call it both from the class and an instance.

"""
class MathOps:
    @staticmethod
    def is_even(num):
        if num%2==0:
            return True
        else:
            return False
M=MathOps()
print(M.is_even(10))

"""
Q4. Create a class Car with:
•	instance attribute mileage
•	class attribute wheels = 4
Add an instance method display_specs() that prints mileage and wheels.
Then change wheels using a class method, and print again.

"""
class Car:
    wheels = 4
    def __init__(self,mileage):
        self.mileage=mileage
    def play_specs(self):
        print(self.mileage)
        print(Car.wheels)
    @classmethod
    def change(cls,new):
        Car.wheels=new
c=Car("50 kmph")
c.play_specs()
c.change(6)
c.play_specs()


"""
Q5. Create a class Temperature with:
•	instance attribute celsius
•	a static method to_fahrenheit(celsius)
•	an instance method show_conversion() that uses the static method to print both values.

"""

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    def show_conversion(self):
        fahrenheit = Temperature.to_fahrenheit(self.celsius)
        print("Celsius:", self.celsius)
        print("Fahrenheit:", fahrenheit)
# Create an object
temp = Temperature(25)
# Call the instance method
temp.show_conversion()

"""
Q8. Create a class Course with:
•	class variable total_students
•	instance variable student_name
•	instance method enroll() → increments total_students
•	class method show_total(cls) → prints total students
•	static method is_eligible(age) → returns True if age ≥ 18
Demonstrate enrolling multiple students and show total count.

"""

class Course:
    Total_stu=0
    def __init__(self,student_name):
        self.student_name=student_name

    def enroll(self):
        Course.Total_stu+=1

    @classmethod
    def show_total(cls):
        print(cls.Total_stu)

    @staticmethod
    def is_eligible(age):
        if age>=18:
            return True
        else:
            return False
c1 = Course("Ayaz")
c1.enroll()

c2 = Course("Raju")
c2.enroll()

c3 = Course("Sima")
c3.enroll()

Course.show_total()
print(Course.is_eligible(20))
print(Course.is_eligible(16))


