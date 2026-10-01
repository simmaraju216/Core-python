class Inventory:
    total = 0
    threshold = 20
    def __init__(self):
        self.stock = {}

    def display(self):
        print(f"Inventory: {self.stock}")
        print(f"Total Stock: {self.total}")
        print(f"Minimum Stock: {self.threshold}")

    def add_item(self,item,quantity):
        if self.valid(quantity):
            self.stock[item] = quantity
            Inventory.total += 1
        else:
            print(f"quantity should be greater")
        self.display()

    def remove_item(self,item):
        if item in self.stock.keys():
            self.stock.pop(item)
            Inventory.total -= 1
            print(f"Removed {item} from inventory.")
        else:
            print(f"{item} not in inventory.")
        self.display()

    @classmethod
    def update(cls,nt):
        cls.threshold = nt

    @staticmethod
    def valid(qn):
        return qn >= Inventory.threshold

i1 = Inventory()
i2 = Inventory()
i3 = Inventory()
print("____________before__________")
i1.add_item("'marker",90)
i2.add_item("mobile",25)
i3.add_item("laptop",15)
print("____________after__________")
Inventory.update(10)
i3.add_item("laptop",15)
i3.remove_item('laptop')
i2.remove_item('mobile')



"""--------------------------------------------"""
class Employee:
    minimum_exp = 5
    def __init__(self,name,exp,dept):
        if self.valid(dept):
            self.name = name
            self.exp = exp
            self.dept = dept
        else:
            print("Employee is not in the right Department")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Exp: {self.exp}")
        print(f"Department: {self.dept}")
        print('\n')

    def promotion(self):
        self.display()
        if self.exp >= Employee.minimum_exp:
            print("Eligible for promotion")
        else:
            print("Not Eligible for promotion")

    @classmethod
    def change(cls,mp):
        cls.minimum_exp = mp

    @staticmethod
    def valid(dep):
        l = ['HR','Tech','Admin','Non-Tech','Sales','Customer Service']
        return dep in l

e1 = Employee("Shiva",0,'Tech')
e2 = Employee("Pranitha",10,'HR')
e3 = Employee("Bhrammi",40,'Customer Service')
e4 = Employee('Pooja',20,'Admin')

e1.display()
e2.display()
e3.display()
e4.display()

e2.promotion()
e3.change(20)
e2.promotion()
#
"""__________________________________________________"""
class Mobile:
    total_apps = 0
    total_files = 0

    def __init__(self):
        self.applications = {"games": {}, "media": {},
                             "cloud": {}}  # {"games":{"pubg":7}, "media":{"Instagram":"300MB"}}
        self.files = {"Docs": {}, "Images": {},
                      "Videos": {}}  # {"Docs":{"coding.py":"16KB"}, "Images":{"457njgd8.jpg":"1.67MB"}}
        self.wifi = False  # True: on, False:off
        self.mobile_data = False  # True: on, False:off
        self.hotspot = False
        self.Airplane = False
        self.VPN = ""
        self.Storage = 128
        self.Storage_used = 8
        self.password = input("Enter password for mobile: ")

    def storage_details(self):
        print(f"Storage : {self.Storage}GB")
        print(f"Storage_used : {self.Storage_used}GB")
        print(f"Storage available : {self.Storage - self.Storage_used}GB")

    def install(self):
        self.storage_details()
        name = input("Enter name of application: ")
        print(f"Category of applications : ")
        k = tuple(self.applications.keys())
        for i, j in enumerate(k):  #(0:'games',1:'media',3:'cloud')
            print(f"{i} : {j}")
        op = int(input(f"Select the category of application you want to install (like 0,1,2..): "))
        st = float(input("Enter the size of application in GB: "))
        if st > self.Storage - self.Storage_used:
            print(f"{st}GB is too big")
            print(f"Can't Install the {name} application")
        else:
            self.applications[k[op]][name] = st
            print(f"Installed {name} application")
            self.Storage_used += st
            print(self.applications)

    def add_vpn(self):
        vpn = input("Enter VPN: ")
        self.VPN = vpn

    def remove_vpn(self):
        self.VPN = ""

    def change_wifi(self):
        print(f"wifi : {'On' if self.wifi else 'Off'}")
        if self.wifi:
            self.wifi = False
        else:
            self.wifi = True

    def wifi_on(self):
        self.wifi = True

    def wifi_off(self):
        self.wifi = False


m1 = Mobile()
m1.install()


"""__________________________________________"""
class Student:
    # Class variables
    total_students = 0
    passing_marks = 35

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Student.total_students += 1

    # Instance method
    def result(self):
        if self.marks >= Student.passing_marks:
            print(f"{self.name}: Passed")
        else:
            print(f"{self.name}: Failed")

    # Class method
    @classmethod
    def curve_marks(cls, percentage):
        cls.passing_marks += (cls.passing_marks * percentage) / 100
        print("New Passing Marks:", cls.passing_marks)

    # Static method
    @staticmethod
    def get_grade(marks):
        if marks >= 90:
            return "A"
        elif marks >= 80:
            return "B"
        elif marks >= 70:
            return "C"
        elif marks >= 60:
            return "D"
        elif marks >= 35:
            return "E"
        else:
            return "F"


# Create students
s1 = Student("Raju", 85)
s2 = Student("Sima", 30)
s3 = Student("Ayaz", 65)

# Total students
print("Total Students:", Student.total_students)

# Pass/Fail
s1.result()
s2.result()
s3.result()

# Grades
print(s1.name, "Grade:", Student.get_grade(s1.marks))
print(s2.name, "Grade:", Student.get_grade(s2.marks))
print(s3.name, "Grade:", Student.get_grade(s3.marks))

# Curve passing marks by 10%
Student.curve_marks(10)

# Check results again
s1.result()
s2.result()
s3.result()


"""______________________________"""
class Product:
    # Class variable
    tax_rate = 18  # 18%

    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

    # Instance method
    def final_price(self):
        tax = self.base_price * Product.tax_rate / 100
        return self.base_price + tax

    # Class method
    @classmethod
    def change_tax_rate(cls, new_rate):
        cls.tax_rate = new_rate

    # Static method
    @staticmethod
    def is_valid_price(price):
        return 0 <= price <= 1000000


# Creating products
p1 = Product("Laptop", 50000)
p2 = Product("Mobile", 20000)

print("Initial Tax Rate:", Product.tax_rate, "%")
print(p1.name, "Final Price:", p1.final_price())
print(p2.name, "Final Price:", p2.final_price())

# Change tax rate for all products
Product.change_tax_rate(12)

print("\nAfter Changing Tax Rate")
print("New Tax Rate:", Product.tax_rate, "%")
print(p1.name, "Final Price:", p1.final_price())
print(p2.name, "Final Price:", p2.final_price())

# Validate prices
print("\nPrice Validation")
print(Product.is_valid_price(25000))     # True
print(Product.is_valid_price(-100))      # False
print(Product.is_valid_price(2000000))   # False

"""__________________________________________"""
class Loan:
    # Class variable (common for all loans)
    interest_rate = 10  # 10%

    def __init__(self, borrower_name, principal):
        self.borrower_name = borrower_name
        self.principal = principal

    # Instance method
    def total_payable(self):
        interest = self.principal * Loan.interest_rate / 100
        return self.principal + interest

    # Class method
    @classmethod
    def update_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate

    # Static method
    @staticmethod
    def check_eligibility(salary):
        return salary > 30000


# 1. Creating multiple loan accounts
loan1 = Loan("Raju", 500000)
loan2 = Loan("Sita", 300000)
loan3 = Loan("Rahul", 700000)

print("Initial Interest Rate:", Loan.interest_rate, "%\n")

# Total repayment before updating interest rate
print("Before Updating Interest Rate")
print(loan1.borrower_name, "Total Payable:", loan1.total_payable())
print(loan2.borrower_name, "Total Payable:", loan2.total_payable())
print(loan3.borrower_name, "Total Payable:", loan3.total_payable())

# 2. Updating interest rate
Loan.update_interest_rate(12)

print("\nUpdated Interest Rate:", Loan.interest_rate, "%")

# Total repayment after updating interest rate
print("\nAfter Updating Interest Rate")
print(loan1.borrower_name, "Total Payable:", loan1.total_payable())
print(loan2.borrower_name, "Total Payable:", loan2.total_payable())
print(loan3.borrower_name, "Total Payable:", loan3.total_payable())

# 3. Checking eligibility
print("\nLoan Eligibility")
print("Salary = 25000:", Loan.check_eligibility(25000))
print("Salary = 45000:", Loan.check_eligibility(45000))
print("Salary = 60000:", Loan.check_eligibility(60000))

"""___________________________________________"""

class Course:
    # Class variables
    total_courses = 0
    minimum_duration = 1  # in months

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.enrolled_students = 0
        Course.total_courses += 1

    # Instance method
    def enroll_student(self):
        self.enrolled_students += 1

    # Class method
    @classmethod
    def update_minimum_duration(cls, new_duration):
        cls.minimum_duration = new_duration

    # Static method
    @staticmethod
    def check_duration(duration):
        return 0 <= duration <= 60   # Valid duration: 0 to 60 months


# 1. Creating multiple courses
course1 = Course("Python Programming", 3)
course2 = Course("Data Science", 6)
course3 = Course("Web Development", 4)

print("Total Courses Created:", Course.total_courses)
print("Minimum Duration:", Course.minimum_duration, "month(s)\n")

# 2. Enrolling students
course1.enroll_student()
course1.enroll_student()
course2.enroll_student()
course3.enroll_student()
course3.enroll_student()
course3.enroll_student()

print("Student Enrollment")
print(course1.title, ":", course1.enrolled_students, "students")
print(course2.title, ":", course2.enrolled_students, "students")
print(course3.title, ":", course3.enrolled_students, "students")

# 3. Updating minimum duration
Course.update_minimum_duration(2)

print("\nUpdated Minimum Duration:", Course.minimum_duration, "month(s)")

# Checking durations
print("\nDuration Validation")
print("3 months :", Course.check_duration(3))
print("-2 months:", Course.check_duration(-2))
print("72 months:", Course.check_duration(72))


"""
Q6. Design a class Vehicle that:
•	Keeps a record of service charge rate common to all vehicles.
•	Each vehicle has a model, kilometers_run, and service history.
•	Has a function to calculate service charge based on km and rate.
•	Provides a method to update the service rate for all vehicles.
•	Provides a static tool to check if a vehicle model is eligible for service (not older than 15 years).
Demonstrate:
1.	Creating vehicles with different km and models.
2.	Updating the service rate.
3.	Showing charges and eligibility checks.
"""



class Vehicle:
    # Class variable
    service_rate = 2  # Rs. per kilometer

    def __init__(self, model, kilometers_run, service_history):
        self.model = model
        self.kilometers_run = kilometers_run
        self.service_history = service_history

    # Instance method
    def calculate_service_charge(self):
        return self.kilometers_run * Vehicle.service_rate

    # Class method
    @classmethod
    def update_service_rate(cls, new_rate):
        cls.service_rate = new_rate

    # Static method
    @staticmethod
    def check_eligibility(model_year):
        current_year = 2026
        return (current_year - model_year) <= 15


# 1. Creating vehicles
v1 = Vehicle("Honda City", 5000, "Last service: Jan 2026")
v2 = Vehicle("Hyundai i20", 12000, "Last service: Mar 2026")
v3 = Vehicle("Maruti Swift", 8000, "Last service: Feb 2026")

print("Initial Service Rate: Rs.", Vehicle.service_rate, "per km\n")

print("Service Charges")
print(v1.model, ":", v1.calculate_service_charge())
print(v2.model, ":", v2.calculate_service_charge())
print(v3.model, ":", v3.calculate_service_charge())

# 2. Updating service rate
Vehicle.update_service_rate(3)

print("\nUpdated Service Rate: Rs.", Vehicle.service_rate, "per km\n")

print("Service Charges After Rate Update")
print(v1.model, ":", v1.calculate_service_charge())
print(v2.model, ":", v2.calculate_service_charge())
print(v3.model, ":", v3.calculate_service_charge())

# 3. Eligibility check
print("\nVehicle Eligibility")
print("Honda City (2020):", Vehicle.check_eligibility(2020))
print("Hyundai i20 (2015):", Vehicle.check_eligibility(2015))
print("Maruti Swift (2008):", Vehicle.check_eligibility(2008))


"""
Q8. Create a HotelRoom class that:
•	Keeps a base price per night (shared).
•	Each room has room_number, nights_booked, and guest_name.
•	Has a method to calculate total bill.
•	Allows updating the base price across all rooms.
•	Provides a static utility to check if a number of nights is valid (e.g., positive integer only).
Demonstrate:
1.	Creating rooms and bookings.
2.	Changing base price.
3.	Checking bill updates and validation.

"""

class HotelRoom:
    # Class variable
    base_price = 2000  # Price per night (Rs.)

    def __init__(self, room_number, nights_booked, guest_name):
        self.room_number = room_number
        self.nights_booked = nights_booked
        self.guest_name = guest_name

    # Instance method
    def calculate_bill(self):
        return self.nights_booked * HotelRoom.base_price

    # Class method
    @classmethod
    def update_base_price(cls, new_price):
        cls.base_price = new_price

    # Static method
    @staticmethod
    def check_nights(nights):
        return isinstance(nights, int) and nights > 0


# 1. Creating rooms and bookings
room1 = HotelRoom(101, 3, "Raju")
room2 = HotelRoom(102, 5, "Sita")
room3 = HotelRoom(103, 2, "Rahul")

print("Initial Base Price: Rs.", HotelRoom.base_price, "per night\n")

print("Room Bills")
print(room1.guest_name, "(Room", room1.room_number, "): Rs.", room1.calculate_bill())
print(room2.guest_name, "(Room", room2.room_number, "): Rs.", room2.calculate_bill())
print(room3.guest_name, "(Room", room3.room_number, "): Rs.", room3.calculate_bill())

# 2. Changing base price
HotelRoom.update_base_price(2500)

print("\nUpdated Base Price: Rs.", HotelRoom.base_price, "per night\n")

print("Updated Room Bills")
print(room1.guest_name, "(Room", room1.room_number, "): Rs.", room1.calculate_bill())
print(room2.guest_name, "(Room", room2.room_number, "): Rs.", room2.calculate_bill())
print(room3.guest_name, "(Room", room3.room_number, "): Rs.", room3.calculate_bill())

# 3. Checking validation
print("\nNight Validation")
print("3 nights :", HotelRoom.check_nights(3))
print("-2 nights:", HotelRoom.check_nights(-2))
print("0 nights :", HotelRoom.check_nights(0))
print("2.5 nights:", HotelRoom.check_nights(2.5))


