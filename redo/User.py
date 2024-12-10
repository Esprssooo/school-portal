from Profile import Profile


class User:
    def __init__(self, first_name, last_name, role, user_id):
        self._first_name = first_name.title()
        self._last_name = last_name.title()
        self._full_name = f"{self._first_name} {self._last_name}"
        self._role = role
        self._username = user_id
        self._password = "1234"
        self._is_password_default = True
        self._profile = Profile(self)

    def get_last_name(self):
        return self._last_name

    def get_first_name(self):
        return self._first_name

    def get_full_name(self):
        return self._full_name

    def validate_credentials(self, username, password):
        return username == self._username and password == self._password

    def login(self):
        print(f"\nWelcome, {self._full_name}!")

        if self._is_password_default:
            while True:
                change_password_input = input(
                    "You still have your default password. Would you like to change it now? [Y/n]: "
                ).lower()

                if change_password_input == "n":
                    break

                else:
                    self.change_password()
                    self._is_password_default = False
                    break

    def logout(self):
        print("Successfully logged out.")

    def change_password(self):
        while True:
            current_password = input("Current password: ")
            if current_password == self._password:
                while True:
                    new_password = input("New password: ")
                    if new_password:
                        confirm_password = input("Confirm password: ")
                        if confirm_password == new_password:
                            self._password = new_password
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
        return self._username

    def get_password(self):
        return self._password

    def dashboard(self):
        pass
