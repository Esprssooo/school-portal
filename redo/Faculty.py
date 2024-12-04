from User import User


class Faculty(User):
    def __init__(self, first_name, last_name, faculty_count):
        user_id = f"F{faculty_count}"
        super().__init__(first_name, last_name, "faculty", user_id)
        self.faculty_id = user_id
