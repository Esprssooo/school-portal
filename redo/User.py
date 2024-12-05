class User:
    def __init__(self, first_name, last_name, role, user_id):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.full_name = f"{self.first_name} {self.last_name}"
        self.role = role
        self.__username = user_id
        self.__password = "1234"
        self.is_password_default = True

    def login(self, username, password):
        return username == self.__username and password == self.__password

    def logout(self):
        print("Successfully logged out.")

    def change_password(self):
        while True:
            current_password = input("Current password: ")
            if current_password == self.__password:
                while True:
                    new_password = input("New password: ")
                    if new_password:
                        confirm_password = input("Confirm password: ")
                        if confirm_password == new_password:
                            self.__password = new_password
                            print("Successfully changed password")
                            break
                        else:
                            print("Password doesn't match")
                    else:
                        print("Enter a valid password!")
                break
            else:
                print("You entered the wrong password.")

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def dashboard(self):
        pass
