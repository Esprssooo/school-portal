class Profile:
    def __init__(self, user):
        self.__first_name = user._first_name
        self.__last_name = user._last_name
        self.__sex = None
        self.__nationality = None
        self.__religion = None
        self.__date_of_birth = None
        self.__place_of_birth = None
        self.__civil_status = None
        self.__address = None
        self.__mobile_number = None
        self.__email = None
        self.__setup_status = False

    def setupProfile(self):
        if not self.__setup_status:
            print("SET UP YOUR PROFILE:\n")

            # Setting up user profile
            while True:
                sex = input("Sex: [M] Male | [F] Female : ").upper()
                if sex:
                    if sex == "M":
                        self.__sex = "Male"
                        break
                    elif sex == "F":
                        self.__sex = "Female"
                        break
                    else:
                        print("Invalid choice.\n")
                else:
                    print("Invalid, this info is required.\n")

            while True:
                nationality = input("Nationality : ").title()
                if nationality:
                    self.__nationality = nationality
                    break
                else:
                    print("Invalid, this info is required.\n")

            religion = input("Religion (optional): ").title()
            if religion:
                self.__religion = religion

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
                        self.__date_of_birth = f"{month} {day}, {year}"
                        break
                    else:
                        print("Invalid.\n")
                else:
                    print("Invalid, this info is required.\n")

            while True:
                place_of_birth = input("Place of Birth : ").title()
                if place_of_birth:
                    self.__place_of_birth = place_of_birth
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
                    self.__civil_status = "Single"
                    break
                elif civil_status == "2":
                    self.__civil_status = "Married"
                    break
                elif civil_status == "3":
                    self.__civil_status = "Separated"
                    break
                elif civil_status == "4":
                    self.__civil_status = "Divorced"
                    break
                elif civil_status == "5":
                    self.__civil_status = "Widowed"
                    break
                else:
                    print("Invalid choice.")

            address = input("Address (optional): ")
            if address:
                self.__address = address

            while True:
                mobile_number = input("Mobile Number (optional): ")
                if not mobile_number:
                    break
                elif mobile_number.isnumeric() and len(mobile_number) == 11:
                    self.__mobile_number = mobile_number
                    break
                else:
                    print("Invalid mobile number. Enter 11 digits or leave it blank.\n")

            email = input("Email (optional): ")
            if email:
                self.__email = email

            print("\nProfile set up successful!\n")
            self.__setup_status = True

    def updateProfile(self):
        while True:
            print("Current Profile:\n")
            print(
                f"""
    Personal Details:
                                
        (-) First Name      : {self.__first_name}
        (-) Last Name       : {self.__last_name}
        (-) Sex             : {self.__sex}
        (-) Nationality     : {self.__nationality}
        (1) Religion        : {self.__religion}
    
    Birth Details:

        (-) Date of Birth   : {self.__date_of_birth}
        (-) Place of Birth  : {self.__place_of_birth}

    Other Information:

        (2) Civil Status    : {self.__civil_status}
        (3) Address         : {self.__address}
        (4) Mobile Number   : {self.__mobile_number}
        (5) Email           : {self.__email}

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
                    self.__religion = religion
            elif choice == "2":
                while True:
                    civil_status = input(
                        "\n(1) Single\n(2) Married\n(3) Separated\n(4) Divorced\n(5) Widowed\n\nCivil Status [1-5]: "
                    )
                    if not civil_status:
                        break
                    if civil_status == "1":
                        self.__civil_status = "Single"
                        break
                    elif civil_status == "2":
                        self.__civil_status = "Married"
                        break
                    elif civil_status == "3":
                        self.__civil_status = "Separated"
                        break
                    elif civil_status == "4":
                        self.__civil_status = "Divorced"
                        break
                    elif civil_status == "5":
                        self.__civil_status = "Widowed"
                        break
                    else:
                        print("Invalid choice.\n")
            elif choice == "3":
                address = input("Address : ")
                if address:
                    self.__address = address
            elif choice == "4":
                while True:
                    mobile_number = input("Mobile Number : ")
                    if mobile_number.isnumeric() and len(mobile_number) == 11:
                        self.__mobile_number = mobile_number
                        break
                    else:
                        print("Sorry that's not a mobile number.\n")
            elif choice == "5":
                email = input("Email : ")
                if email:
                    self.__email = email
            else:
                print("Invalid choice.\n")

    def viewProfile(self):
        print(
            f"""
Personal Details:

    First Name      : {self.__first_name}
    Last Name       : {self.__last_name}
    Sex             : {self.__sex}
    Nationality     : {self.__nationality}
    Religion        : {self.__religion}

Birth Details:

    Date of Birth   : {self.__date_of_birth}
    Place of Birth  : {self.__place_of_birth}

Other Information:

    Civil Status    : {self.__civil_status}
    Address         : {self.__address}
    Mobile Number   : {self.__mobile_number}
    Email           : {self.__email}
"""
        )
