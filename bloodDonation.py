# from BloodUser import User
# from BloodAdmin import Admin
# from BloodBank import BloodBank
# from BloodBankInfo import BloodBankInfo

bloodTypeList = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

class BloodBank:
    def __init__(self, name, area):
        self.name = name
        self.area = area
        self.donors = []

    def getDonorList(self):
        for donor in self.donors:
            donor.printUserInfo()

    def addDonor(self, newUser, data):
        self.donors.append(newUser)
        data.Donors[newUser] = self
        data.DonorList.append(newUser)
    
#==========================================================================
class BloodBankInfo:
    def __init__(self):

        # Attributes

        self.listBloodBanks = []
        self.DonorList = []
        self.requests = []
        self.Donors = dict()

    # Methods
    def addBank(self, newBank):
        self.listBloodBanks.append(newBank)

    def viewRequests(self):
        if (len(self.requests)==0):
            print("No requests found")
        for request in self.requests:
            print("////////////////////////////////////////////")
            print(f"Name: {request.name}")
            print(f"Blood Group: {request.BloodType}")
            print("////////////////////////////////////////////")

    def viewDonors(self):
        for key in self.Donors.keys():
            print("////////////////////////////////////////////")
            print(f"Name: {key.name}")
            print(f"Blood Group: {key.BloodType}")
            print(f"Blood Bank: {self.Donors[key].name}")
            print(f"Area: {self.Donors[key].area}")
            print("////////////////////////////////////////////")

    def sendRequests(self, reqBlood):
        for user in self.DonorList:
            if (user.BloodType == reqBlood):
                user.recieveRequest(self.Donors[user])
                print(f"{user.name} has recieved request for blood donation")

    def BloodGroupDetails(self, reqBlood):
        for key in self.Donors.keys():
            if (key.BloodType == reqBlood):
                print("////////////////////////////////////////////")
                print(f"Name: {key.name}")
                print(f"Blood Group: {key.BloodType}")
                print(f"Blood Bank: {self.Donors[key].name}")
                print(f"Area: {self.Donors[key].area}")
                print("////////////////////////////////////////////")

    def viewHospitals(self):
        for i in range(len(self.listBloodBanks)):
            print(f"{i+1}. {self.listBloodBanks[i].name}")

#========================================================================

class User:
    def __init__(self, name, bloodtype):
        self.name = name
        self.BloodType = bloodtype
        self.notifs = []

    def printUserInfo(self):
        print(self.name)
        print(self.BloodType)

    def requestBlood(self, data):
        data.requests.append(self)
        print(f"Request for {self.BloodType} sent")

    def recieveRequest(self, venue):
        self.notifs.append(venue)
        print(f"{self.name} has recieved request for blood at {venue.name}")

    def viewRequests(self):
        if (len(self.notifs)==0):
            print("NO REQUESTS RECIEVED")
        for notif in self.notifs:
            print(f"Request for blood from {notif.name}")

#=========================================================================

class Admin:
    def __init__(self, name):
        self.name = name

    def addNewBank(self, data, name, area):
        newBank = BloodBank(name, area)
        data.addBank(newBank)

    def viewDonorList(self, data):
        data.viewDonors()

    def viewRequests(self, data):
        data.viewRequests()

    def sendNotifs(self, data):
        for request in data.requests:
            reqBlood = request.BloodType
            data.sendRequests(reqBlood)

    def getDetailsByBloodType(self, data, reqBlood):
        data.BloodGroupDetails(reqBlood)

    def RareBloodInfo(self, data):
        data.BloodGroupDetails("AB-")
        data.BloodGroupDetails("O-")
        data.BloodGroupDetails("AB+")

    def viewHospitals(self, data):
        data.viewHospitals()

#==================================================================

BloodData = BloodBankInfo()
GuestUsers = []
GuestUsers.append(User("xyz", "A+"))
GuestUsers.append(User("abc", "A-"))
GuestUsers.append(User("123", "AB+"))
GuestUsers.append(User("tef", "AB-"))
GuestUsers.append(User("ghi", "B+"))
GuestUsers.append(User("req", "B-"))
GuestUsers.append(User("efg", "O+"))
GuestUsers.append(User("ion", "O-"))

Bank_List = []
Bank_List.append(BloodBank("XYZ Hospitals", "Mumbai, Shahid Bhagat Singh Marg"))
Bank_List.append(BloodBank("ABC Hospitals", "Delhi, Connaught Lane"))
Bank_List.append(BloodBank("123 Hospitals", "Dharwad, PB Road"))

GuestUsers[3].notifs.append(Bank_List[0])

BloodData.addBank(Bank_List[0])
BloodData.addBank(Bank_List[1])
BloodData.addBank(Bank_List[2])

BloodData.listBloodBanks[0].addDonor(GuestUsers[0], BloodData)
BloodData.listBloodBanks[0].addDonor(GuestUsers[1], BloodData)
BloodData.listBloodBanks[0].addDonor(GuestUsers[2], BloodData)
BloodData.listBloodBanks[1].addDonor(GuestUsers[3], BloodData)
BloodData.listBloodBanks[1].addDonor(GuestUsers[4], BloodData)
BloodData.listBloodBanks[2].addDonor(GuestUsers[5], BloodData)
BloodData.listBloodBanks[2].addDonor(GuestUsers[6], BloodData)
BloodData.listBloodBanks[2].addDonor(GuestUsers[7], BloodData)

BloodData.requests.append(GuestUsers[0])
BloodData.requests.append(GuestUsers[1])
BloodData.requests.append(GuestUsers[2])

while True:
    print("LOGIN AS:\n1. USER\n2. ADMIN\n")
    choice = int(input(""))
    if (choice != 1 and choice != 2):
        print("ENTER VALID OPTION")
        continue

    elif (choice == 1):
        Name = str(input("Enter your name\n"))
        print("BLOOD GROUPS")
        for i in range(len(bloodTypeList)):
            print(f"{i+1}. {bloodTypeList[i]}")
        bloodChoice = int(input("Pick your blood type index\n"))
        Guest = User(Name, bloodTypeList[bloodChoice-1])

        print(f"Welcome {Guest.name}")

        print("PICK THE NEAREST BLOOD BANK")
        for i in range(len(BloodData.listBloodBanks)):
            print(f"{i+1}. {BloodData.listBloodBanks[i].name}")
        bankChoice = int(input("Select the bank index\n"))
        BloodData.listBloodBanks[bankChoice-1].addDonor(Guest, BloodData)
        print(f"User added successfully")

        while True:
            print("USER MENU")
            print("1. VIEW RECIEVED REQUEST\n2. REQUEST BLOOD\n3. VIEW MY INFO\n4. LOGOUT")
            UserChoice = int(input("Select an option:\n"))
            
            if UserChoice == 1:
                print("======================================================")
                Guest.viewRequests()
                print("======================================================")

            elif UserChoice == 2:
                print("======================================================")
                Guest.requestBlood(BloodData)
                print("======================================================")

            elif UserChoice == 3:
                print("======================================================")
                Guest.printUserInfo()
                print("======================================================")

            elif UserChoice == 4:
                print("======================================================")
                print("LOGGING OUT FROM USER")
                print("======================================================")
                break
            
            else:
                print("======================================================")
                print("ENTER VALID CHOICE")
                print("======================================================")

            
    elif (choice == 2):
        Name = str(input("Enter your name: "))
        ADMIN = Admin(Name)
        print("======================================================")
        print(f"Welcome, {ADMIN.name}")
        print("======================================================")

        while True:
            print("ADMIN MENU")
            print("1. VIEW DONORS\n2. VIEW REQUESTS\n3. SEND AUTOMATED NOTIFS FOR REQUIRED BLOOD\n4. ADD NEW BLOOD BANK\n5. GET DETAILS BY BLOOD TYPE\n6. GET RARE BLOOD GROUP INFO\n7. VIEW LIST OF HOSPITALS\n8. LOGOUT")
            AdminChoice = int(input("Select an option\n"))

            if AdminChoice == 1:
                print("======================================================")
                ADMIN.viewDonorList(BloodData)
                print("======================================================")

            elif AdminChoice == 2:
                print("======================================================")
                ADMIN.viewRequests(BloodData)
                print("======================================================")

            elif AdminChoice == 3:
                print("======================================================")
                ADMIN.sendNotifs(BloodData)
                print("======================================================")

            elif AdminChoice == 4:
                print("======================================================")
                HospitalName = str(input("Enter the hospital name: "))
                AreaName = str(input("Enter the locality of the hospital: "))
                ADMIN.addNewBank(BloodData, HospitalName, AreaName)
                print(f"{HospitalName} added to Blood Bank List successfully")
                print("======================================================")

            elif AdminChoice == 5:
                print("======================================================")
                print("BLOOD GROUPS")
                for i in range(len(bloodTypeList)):
                    print(f"{i+1}. {bloodTypeList[i]}")
                bloodChoice = int(input("Pick required blood type index\n"))
                ADMIN.getDetailsByBloodType(BloodData,bloodTypeList[bloodChoice-1])
                print("======================================================")

            elif AdminChoice == 6:
                print("======================================================")
                ADMIN.RareBloodInfo(BloodData)
                print("======================================================")

            elif AdminChoice == 7:
                print("======================================================")
                ADMIN.viewHospitals(BloodData)
                print("======================================================")

            elif AdminChoice == 8:
                print("======================================================")
                print("LOGGING OUT FROM USER")
                print("======================================================")
                break
