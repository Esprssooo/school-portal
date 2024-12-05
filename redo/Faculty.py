from User import User


class Faculty(User):
    def __init__(self, first_name, last_name, faculty_id):
        # user_id = f"F{faculty_count}"
        user_id = faculty_id
        super().__init__(first_name, last_name, "faculty", user_id)
        self.faculty_id = user_id
        self.classes = {}

    def view_classes(self):
        if not self.classes:
            classes = "No classes assigned."
        else:
            classes = "Your classes: "
            for subject, sections in self.classes.items():
                classes += f"\n  {subject.subject_name}: "
                for section in sections:
                    classes += f"{section.section_name} "
        return classes

    def dashboard(self):
        while True:
            print("\n-------- SPCF Portal --------")
            print("[1] View Classes")
            print("[2] Grade Students")
            print("[4] Change Password")
            print("[0] Logout")
            menu_option = input("Choose a menu option [1, 2, 0]: ")
            print()

            if menu_option == "1":
                print(self.view_classes())

            elif menu_option == "2":
                print("\nChoose section to grade: ")
                self.grade_section()

            elif menu_option == "4":
                self.change_password()

            elif menu_option == "0":
                self.logout()
                faculty = None
                break

            else:
                print("Invalid option, please try again.")
