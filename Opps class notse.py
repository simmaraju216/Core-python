# class Student:
#     """Just a student class"""
#     total = 0
#     def  __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Student.total +=1
#
#     def display(self, phno,Branch):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Branch: {Branch}")
#         print(f"Phone: {phno}")
#         self.total_students()
#
#     @classmethod
#     def total_students(cls):
#         print(f"Total Students: {cls.total}")
#
#     @classmethod
#     def change(cls,n):
#         cls.total = n
#
#     @staticmethod
#     def just(name, age):
#         if len(name) < 10 and age < 18:
#             print("Name too short and age must be greater than 18")
#         else:
#             print("Valid credentials")
#
#
#
# s1 = Student("John", 25)
# s2 = Student("Michael", 35)
# s3 = Student("Bob", 35)
#
# s1.display(2345678,"CSE")
# print()
# Student.display(s1,5678998765,"CSE")
# Student.total_students()
# Student.change(20)
# s1.change(25)
# s1.total_students()
# Student.total_students()
# Student.just("Michael", 35)
# s1.just("Michael", 20)
#
# s1.total += 1
# print(s1.total)
# print(s2.total)
# print(s3.total)
# print(Student.total)
#
# print(s1.__dict__)
# print(s2.__dict__)
# print(s3.__dict__)
#
# print(Student.__dict__)
#
#
#
#
# class Student:
#     passing_marks = 40
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def result(self):
#         if self.marks >= Student.passing_marks:
#             print(f"{self.name} : pass")
#         else:
#             print(f"{self.name} : fail")
#
#     @classmethod
#     def update(cls,pm):
#         cls.passing_marks = pm
#
#     @staticmethod
#     def grade_category(m):
#         if m >= 90:
#             return "A"
#         elif m >= 80:
#             return "B"
#         elif m >= 70:
#             return "C"
#         elif m >= 60:
#             return "D"
#         else:
#             return "F"
#
#
# s1 = Student("Jaya simha", 99)
# s2 = Student("sohail", 98)
# s3 = Student("Ganesh", 35)
# s4 = Student("RK", 96)
#
# s1.result()
# s2.result()
# s3.result()
# s4.result()
#
# s3.update(99)
# s1.marks = 9
# s3.marks = 100
# s1.result()
# s2.result()
# s3.result()
# s4.result()
#
#
# print(s1.grade_category(s1.marks))
#
#
# class Employee:
#     bonus_rate = 0.1
#     def __init__(self,name,salary):
#         self.name = name
#         self.base_salary = salary
#
#     def final_salary(self):
#         return self.base_salary+(self.base_salary*Employee.bonus_rate)
#
#     @classmethod
#     def update_bonus(cls,nb):
#         cls.bonus_rate = nb
#
#     @staticmethod
#     def valid(sal):
#         return sal > 0
#
# e1 = Employee("Amarnath", 5000000)
# e2 = Employee("Shiva", 5000001)
#
# print(e1.final_salary())
# print(e2.final_salary())
# e1.update_bonus(0.2)
# print(e1.final_salary())
# print(e2.final_salary())
#
#
#
#
#
# class Book:
#     total_books = 0
#     def __init__(self,title,author):
#         self.title = title
#         self.author = author
#         Book.total_books += 1
#
#     @classmethod
#     def from_string(cls, book_str):
#         t,a = book_str.split("-")
#         if cls.is_valid(t):
#             return cls(t,a)
#         else:
#             return "Invalid book string"
#
#     @staticmethod
#     def is_valid(t):
#         return len(t) >= 3
#
#
# bts = "Harry potter - J.K.Rowling"
# b1 = Book.from_string(bts)
# b2 = Book("The song of Ice and Fire","R.R.Martin")


"""__________Inheritance____________"""

# class A:
#     x=34
#     def __init__(self,y):
#         self.y=y
# class B(A):
#     pass
# print(B.x)
# b1=B(10)
# print(b1.y)


# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print(f'name:{self.name}')
# class cat(Animal):
#     def display(self):
#         print(f"name:{self.name}")
#         print("Animal:cat")
# class dog(Animal):
#     def display(self):
#         super().display()
#         print("Animal:dog")
# c1=cat("chiru")
# c2=cat("raju")
# c1.display()
# c2.display()
# d1=dog("light")
# d2=dog("ganesh")
# d2.display()
# d1.display()

class emp:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def display(self):
        print(self.name, self.age, self.salary, sep="\n")
class manager(emp):
    def __init__(self,name,age,salary,dep):
        super().__init__(name, age, salary)
        self.dep=dep
    def display(self):
        super().display()
        print(self.dep)
m1=manager("raju",21,700000,"cse")
m1.display()
