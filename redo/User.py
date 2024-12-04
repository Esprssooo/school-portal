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
        pass

    def change_password(self):
        pass

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password
