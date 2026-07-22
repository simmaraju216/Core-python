#1)
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_passed(self):
        if self.marks>40:
            print('passed')
        else:
            print('failed')
s1=student('raju',90)
s1.is_passed()
s2=student('chiru',50)
s2.is_passed()

#2)
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

#3)
class MathOps:

    @staticmethod
    def is_even(num):
        if num%2==0:
            return True
        else:
            return False
m=MathOps()
print(m.is_even(6))

#6)
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
#4)
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