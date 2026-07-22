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
i1.add_item("'marker",90)
i2.add_item("mobile",25)
i3.add_item("laptop",15)
Inventory.update(10)
i3.add_item("laptop",15)
i1.remove_item('laptop')
i2.remove_item('mobile')



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