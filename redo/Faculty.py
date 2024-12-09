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
                classes += f"\n  {subject}: "
                for section in sections:
                    classes += f"\n  - {section.section_name} "
        return classes

    def input_edit_grade(self, period, section, edit=False):
        assigned_subject = None
        for subject in section.subjects:
            if subject.subject_name in self.classes:
                assigned_subject = subject

        if assigned_subject:
            print(f"\nGrading students in {section.section_name} for {period}: ")
            if not edit:
                print('(Press the "Enter key" to skip student.)')
            for student in section.students:
                if not edit:
                    # skip students with grade
                    if student.has_grade(assigned_subject.subject_code, period):
                        continue

                while True:
                    grade_input = input(
                        f"Enter grade for {student.last_name}, {student.first_name}: "
                    )

                    if not edit:
                        if grade_input == "":
                            student.add_grade(
                                assigned_subject.subject_code, period, None
                            )
                            break
                    try:
                        grade = float(grade_input)
                        if 0.00 <= grade <= 100:
                            student.add_grade(
                                assigned_subject.subject_code, period, grade
                            )
                            break
                        else:
                            print(
                                "Invalid grade. Please input a grade between 0 and 100."
                            )
                    except ValueError:
                        print("Invalid input.")
        else:
            print(
                f"You are not assigned to any subject in section {section.section_name}."
            )

    def choose_period(self, section):
        while True:
            print("[1] Prelim")
            print("[2] Midterm")
            print("[3] Final")
            period_input = input("Choose period to grade [1, 2, 3]: ")
            period = None
            if period_input == "1":
                period = "Prelim"
            elif period_input == "2":
                period = "Midterm"
            elif period_input == "3":
                period = "Final"
            else:
                print("Invalid option.")
            return period
            # self.input_edit_grade(period, section, edit)
            break

    def check_section(self, section_name):
        section_found = None
        for sections in self.classes.values():
            for section in sections:
                if section.section_name == section_name:
                    section_found = section
                    # self.choose_period(section_found, edit)
                    return section_found
        if not section_found:
            print("Section not found.")
            return

    def dashboard(self):
        while True:
            print("\n-------- SPCF Portal --------")
            print("[1] View Classes")
            print("[2] Input Students Grades (Section)")
            print("[3] Edit Students Grades (Section)")
            print("[4] Input/Edit Student Grade")
            print("[5] Change Password")
            print("[0] Logout")
            menu_option = input("Choose a menu option [1, 2, 0]: ")
            print()

            if menu_option == "1":
                print(self.view_classes())

            elif menu_option == "2":
                print(self.view_classes())
                section_input = input("\nChoose section to grade: ").upper()
                selected_section = self.check_section(section_input)

                if selected_section:
                    period = self.choose_period(section_input)
                    if period:
                        self.input_edit_grade(period, selected_section)

            elif menu_option == "3":
                print(self.view_classes())
                section_input = input("\nChoose section to grade: ").upper()
                selected_section = self.check_section(section_input)

                if selected_section:
                    period = self.choose_period(section_input)
                    if period:
                        self.input_edit_grade(period, selected_section, edit=True)

            elif menu_option == "4":
                pass

            elif menu_option == "5":
                self.change_password()

            elif menu_option == "0":
                self.logout()
                break

            else:
                print("Invalid option, please try again.")
