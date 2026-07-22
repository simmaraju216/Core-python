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
            self.storage_details()
    def un_install(self):
        app=input('enter which application is to uninstall')
        k = tuple(self.applications.keys())
        for i, j in enumerate(k):  # (0:'games',1:'media',3:'cloud')
            print(f"{i} : {j}")
        op = int(input(f"Select the category of application you want to install (like 0,1,2..): "))
        val=self.applications[k[op]][app]
        self.Storage_used -= val
        self.applications[k[op]].pop(app)
        self.storage_details()

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

