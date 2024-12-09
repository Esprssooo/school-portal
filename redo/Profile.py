class Profile:
    def __init__(self, user):
        self.first_name = user.first_name
        self.last_name = user.last_name
        self.sex = None
        self.nationality = None
        self.religion = None
        self.date_of_birth = None
        self.place_of_birth = None
        self.civil_status = None
        self.address = None
        self.mobile_number = None
        self.email = None
        self.setup_status = False

    def setupProfile(self):
        if self.setup_status == False:
            print("Set Up your Profile:\n\n")

            # Setting up user's Profile
            while True:
                print("Sex:")
                sex = input("[M] Male | [F] Female\n: ").upper()
                if sex == "M":
                    self.sex = "Male"
                    break
                elif sex == "F":
                    self.sex = "Female"
                    break
                else:
                    print("Invalid choice.\n")

            while True:
                nationality = input("Nationality: ").title()
                if nationality:
                    self.nationality = nationality
                    break
                else:
                    print("Invalid, this info is required.\n")

            religion = input("Religion: ").title()
            if religion:
                self.religion = religion

            while True:
                month = input("Enter your birth month: (January): ").title()
                if month:
                    day = input("Enter your birth date (16): ")
                    if day:
                        year = input("Enter your birth year (2004): ")
                        if year:
                            self.date_of_birth = f"{month} {day}, {year}"
                            break
                        else:
                            print("Invalid, this info is required.\n")
                    else:
                        print("Invalid, this info is required.\n")
                else:
                    print("Invalid, this info is required.\n")

            while True:
                place_of_birth = input("Place of Birth: ").title()
                if place_of_birth:
                    self.place_of_birth = place_of_birth
                    break
                else:
                    print("Invalid, this info is required.\n")

            while True:
                civil_status = input(
                    "Civil Status:\n(1) Single\n(2) Married\n(3) Separated\n(4) Divorced\n(5) Widowed\n : "
                )
                if not civil_status:
                    break
                elif civil_status == "1":
                    self.civil_status = "Single"
                    break
                elif civil_status == "2":
                    self.civil_status = "Married"
                    break
                elif civil_status == "3":
                    self.civil_status = "Separated"
                    break
                elif civil_status == "4":
                    self.civil_status = "Divorced"
                    break
                elif civil_status == "5":
                    self.civil_status = "Widowed"
                    break
                else:
                    print("Invalid choice.\n")

            address = input("Address: ")
            if address:
                self.address = address

            while True:
                mobile_number = input("Mobile Number: ")
                if not mobile_number:
                    break
                elif mobile_number.isnumeric() == True and len(mobile_number) == 11:
                    self.mobile_number = mobile_number
                    break
                else:
                    print("Sorry that's not a valid mobile number.\n")

            email = input("Email: ")
            if email:
                self.email = email

            print("\nProfile set up successful!\n")
            self.setup_status = True

    def updateProfile(self):
        while True:
            print("Current Profile:\n")
            print(
                f"""
    Personal Data:
                                
        (-) First Name      : {self.first_name}
        (-) Last Name       : {self.last_name}
        (-) Sex             : {self.sex}
        (-) Nationality     : {self.nationality}
        (1) Religion        : {self.religion}
        (-) Date of Birth   : {self.date_of_birth}
        (-) Place of Birth  : {self.place_of_birth}
        (2) Civil Status    : {self.civil_status}
        (3) Address         : {self.address}
        (4) Mobile Number   : {self.mobile_number}
        (5) Email           : {self.email}

        (0) Exit Update Profile
    """
            )

            choice = input("\nChoose which info to update [0-5]: ")
            if choice == "0":
                print("\nProfile updated successfully!\n")
                break
            elif choice == "1":
                religion = input("Religion : ").title()
                if religion:
                    self.religion = religion
            elif choice == "2":
                while True:
                    civil_status = input(
                        "Civil Status:\n(1) Single\n(2) Married\n(3) Separated\n(4) Divorced\n(5) Widowed\n : "
                    )
                    if not civil_status:
                        break
                    if civil_status == "1":
                        self.civil_status = "Single"
                        break
                    elif civil_status == "2":
                        self.civil_status = "Married"
                        break
                    elif civil_status == "3":
                        self.civil_status = "Separated"
                        break
                    elif civil_status == "4":
                        self.civil_status = "Divorced"
                        break
                    elif civil_status == "5":
                        self.civil_status = "Widowed"
                        break
                    else:
                        print("Invalid choice.\n")
            elif choice == "3":
                address = input("Address : ")
                if address:
                    self.address = address
            elif choice == "4":
                while True:
                    mobile_number = input("Mobile Number : ")
                    if mobile_number.isnumeric() == True and len(mobile_number) == 11:
                        self.mobile_number = mobile_number
                        break
                    else:
                        print("Sorry that's not a mobile number.\n")
            elif choice == "5":
                email = input("Email : ")
                if email:
                    self.email = email
            else:
                print("Invalid choice.\n")

    def viewProfile(self):
        print(
            f"""
Personal Data:

    First Name      : {self.first_name}
    Last Name       : {self.last_name}
    Sex             : {self.sex}
    Nationality     : {self.nationality}
    Religion        : {self.religion}
    Date of Birth   : {self.date_of_birth}
    Place of Birth  : {self.place_of_birth}
    Civil Status    : {self.civil_status}
    Address         : {self.address}
    Mobile Number   : {self.mobile_number}
    Email           : {self.email}
"""
        )


# Vince = Student("Vince Randall", "David", "S2", "BSCS")
# Jennel = Student("Jennel", "Ong", "S2", "BSCS")

# Jennel.profile.setupProfile()
# Jennel.profile.viewProfile()
# Jennel.profile.setupProfile()
# Jennel.profile.updateProfile()
