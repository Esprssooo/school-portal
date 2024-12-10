class Profile:
    def __init__(self, user):
        self.first_name = user._first_name
        self.last_name = user._last_name
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
        if not self.setup_status:
            print("SET UP YOUR PROFILE:\n")

            # Setting up user's Profile
            while True:
                sex = input("Sex: [M] Male | [F] Female : ").upper()
                if sex:
                    if sex == "M":
                        self.sex = "Male"
                        break
                    elif sex == "F":
                        self.sex = "Female"
                        break
                    else:
                        print("Invalid choice.\n")
                else:
                    print("Invalid, this info is required.\n")

            while True:
                nationality = input("Nationality : ").title()
                if nationality:
                    self.nationality = nationality
                    break
                else:
                    print("Invalid, this info is required.\n")

            religion = input("Religion (optional): ").title()
            if religion:
                self.religion = religion

            while True:
                months = [
                    "January",
                    "February",
                    "March",
                    "April",
                    "May",
                    "June",
                    "July",
                    "August",
                    "September",
                    "October",
                    "November",
                    "December",
                ]
                month = input("Birth Month (January) : ").title()
                if month:
                    if month in months:
                        break
                    else:
                        print("Invalid, input a valid month.\n")
                else:
                    print("Invalid, this info is required.\n")

            while True:
                thirties = ["April", "June", "September", "November"]
                if month == "February":
                    day = input("Birth Date (1-28) : ")
                    if day:
                        if day.isnumeric() and (int(day) > 0 and int(day)) <= 28:
                            break
                        else:
                            print("Invalid, it must be a number between 1-28.\n")
                    else:
                        print("Invalid, this info is required.\n")

                elif month in thirties:
                    day = input("Birth Date (1-30) : ")
                    if day:
                        if day.isnumeric() and (int(day) > 0 and int(day)) <= 30:
                            break
                        else:
                            print("Invalid, it must be a number between 1-30.\n")
                    else:
                        print("Invalid, this info is required.\n")

                else:
                    day = input("Birth Date (1-31) : ")
                    if day:
                        if day.isnumeric() and (int(day) > 0 and int(day)) <= 31:
                            break
                        else:
                            print("Invalid, it must be a number between 1-31.\n")
                    else:
                        print("Invalid, this info is required.\n")

            while True:
                year = input("Birth Year : ")
                if year:
                    if year.isnumeric() and (int(year) < 2024 and int(year) >= 1900):
                        self.date_of_birth = f"{month} {day}, {year}"
                        break
                    else:
                        print("Invalid.\n")
                else:
                    print("Invalid, this info is required.\n")

            while True:
                place_of_birth = input("Place of Birth : ").title()
                if place_of_birth:
                    self.place_of_birth = place_of_birth
                    break
                else:
                    print("Invalid, this info is required.\n")

            while True:
                civil_status = input(
                    "\n(1) Single\n(2) Married\n(3) Separated\n(4) Divorced\n(5) Widowed\n\nCivil Status [1-5]: "
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
                    print("Invalid choice.")

            address = input("Address (optional): ")
            if address:
                self.address = address

            while True:
                mobile_number = input("Mobile Number (optional): ")
                if not mobile_number:
                    break
                elif mobile_number.isnumeric() and len(mobile_number) == 11:
                    self.mobile_number = mobile_number
                    break
                else:
                    print("Invalid mobile number. Enter 11 digits or leave it blank.\n")

            email = input("Email (optional): ")
            if email:
                self.email = email

            print("\nProfile set up successful!\n")
            self.setup_status = True

    def updateProfile(self):
        while True:
            print("Current Profile:\n")
            print(
                f"""
    Personal Details:
                                
        (-) First Name      : {self.first_name}
        (-) Last Name       : {self.last_name}
        (-) Sex             : {self.sex}
        (-) Nationality     : {self.nationality}
        (1) Religion        : {self.religion}
    
    Birth Details:

        (-) Date of Birth   : {self.date_of_birth}
        (-) Place of Birth  : {self.place_of_birth}

    Other Information:

        (2) Civil Status    : {self.civil_status}
        (3) Address         : {self.address}
        (4) Mobile Number   : {self.mobile_number}
        (5) Email           : {self.email}

        (0) Exit Update Profile
    """
            )

            choice = input("\nChoose which info to update [0-5]\n> ")
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
                        "\n(1) Single\n(2) Married\n(3) Separated\n(4) Divorced\n(5) Widowed\n\nCivil Status [1-5]: "
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
                    if mobile_number.isnumeric() and len(mobile_number) == 11:
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
Personal Details:

    First Name      : {self.first_name}
    Last Name       : {self.last_name}
    Sex             : {self.sex}
    Nationality     : {self.nationality}
    Religion        : {self.religion}

Birth Details:

    Date of Birth   : {self.date_of_birth}
    Place of Birth  : {self.place_of_birth}

Other Information:

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
