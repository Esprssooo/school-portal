from User import User


class Faculty(User):
    def __init__(self, first_name, last_name, faculty_id):
        # user_id = f"F{faculty_count}"
        user_id = faculty_id
        super().__init__(first_name, last_name, "faculty", user_id)
        self.faculty_id = user_id
        self.classes = {}

    def handle_classes(self, subject_name, section):
        if subject_name not in self.classes:
            self.classes[subject_name] = []
        self.classes[subject_name].append(section)

    def view_students(self):
        while True:
            section_input = input("Select section: ").upper()
            print()
            if section_input:
                section = self.check_section(section_input)
                if section:
                    return section.view_student_list()
            else:
                print("Invalid section")

    def view_classes(self):
        if not self.classes:
            return "No classes assigned."

        classes = "Your classes: "
        for subject, sections in self.classes.items():
            classes += f"\n  {subject}: "
            for section in sections:
                classes += f"\n  - {section.get_section_name()} "
        return classes

    def input_edit_grade(self, period, section, edit=False):
        assigned_subject = None
        for subject in section.get_subjects():
            if subject.get_subject_name() in self.classes:
                assigned_subject = subject

        if assigned_subject:
            print(f"\nGrading students in {section.get_section_name()} for {period}: ")
            if not edit:
                print('(Press the "Enter key" to skip student.)')
            for student in section.get_students():
                for stud_sub in student.get_subjects():
                    if (
                        assigned_subject.get_subject_code()
                        == stud_sub.get_subject_code()
                    ):
                        # if not edit:
                        # skip students with grade
                        # print(student.full_name)
                        if student.has_grade(
                            assigned_subject.get_subject_code(), period
                        ):
                            continue

                        while True:
                            grade_input = input(
                                f"Enter grade for {student.get_last_name()}, {student.get_first_name()}: "
                            )

                            if not edit:
                                if grade_input == "":
                                    student.add_grade(
                                        assigned_subject.get_subject_code(),
                                        period,
                                        None,
                                    )
                                    break
                            try:
                                grade = float(grade_input)
                                if 0.00 <= grade <= 100:
                                    student.add_grade(
                                        assigned_subject.get_subject_code(),
                                        period,
                                        grade,
                                    )
                                    break
                                else:
                                    print(
                                        "Invalid grade. Please input a grade between 0 and 100."
                                    )
                            except ValueError:
                                print("Invalid input.")
            all_graded = True
            for student in section.get_students():
                if not student.has_grade(assigned_subject.get_subject_code(), period):
                    all_graded = False
                    break

            if all_graded:
                print(
                    f"All students in {section.get_section_name()} have been graded for {period}."
                )
            # else:
            #     print(
            #         f"Not all students in {section.section_name} have been graded for {period}."
            #     )
        else:
            print(
                f"You are not assigned to any subject in section {section.get_section_name()}."
            )

    def choose_period(self):
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

    def input_student_grade(self, period, student):
        for subject in student.get_subjects():
            if subject.get_subject_name() in self.classes:
                while True:
                    grade_input = input(
                        f"Enter grade for {student.get_last_name()}, {student.get_first_name()}: "
                    )

                    try:
                        grade = float(grade_input)
                        if 0.00 <= grade <= 100:
                            student.add_grade(subject.get_subject_code(), period, grade)
                            break
                        else:
                            print(
                                "Invalid grade. Please input a grade between 0 and 100."
                            )
                    except ValueError:
                        print("Invalid input.")
                break

    def check_section(self, section_name):
        section_found = None
        for sections in self.classes.values():
            for section in sections:
                if section.get_section_name() == section_name:
                    section_found = section
                    # self.choose_period(section_found, edit)
                    return section_found
        if not section_found:
            print("Section not found.")
            return

    def check_student(self, student_name):
        student_found = None
        for sections in self.classes.values():
            for section in sections:
                for student in section.get_students():
                    if student.get_student_id() == student_name:
                        student_found = student
                        return student_found
        if not student_found:
            print("Student not found.")
            return

    def dashboard(self, portal=None):
        while True:
            print("\n-------- SPCF Portal --------")
            print("[1] View Classes")
            print("[2] View Students")
            print("[3] Input Students Grades (Section)")
            # print("[4] Edit Students Grades (Section)")
            print("[4] Input/Edit Student Grade")
            print("[5] View Profile")
            print("[6] Change Password")
            print("[0] Logout")
            menu_option = input("Choose a menu option [1, 2, 3, 4, 5, 6, 0]: ")
            print()

            if menu_option == "1":
                print(self.view_classes())

            elif menu_option == "2":
                print(self.view_classes())
                print(self.view_students())

            elif menu_option == "3":
                print(self.view_classes())
                section_input = input("\nChoose section to grade: ").upper()
                selected_section = self.check_section(section_input)

                if selected_section:
                    period = self.choose_period()
                    if period:
                        self.input_edit_grade(period, selected_section)

            # elif menu_option == "10":
            #     print(self.view_classes())
            #     section_input = input("\nChoose section to grade: ").upper()
            #     selected_section = self.check_section(section_input)

            #     if selected_section:
            #         period = self.choose_period()
            #         if period:
            #             self.input_edit_grade(period, selected_section, edit=True)

            elif menu_option == "4":
                print(self.view_classes())
                print(self.view_students())
                student_input = input("Enter student full name: ")
                selected_student = self.check_student(student_input)

                if selected_student:
                    period = self.choose_period()
                    if period:
                        self.input_student_grade(period, selected_student)

            elif menu_option == "5":
                self._profile.setupProfile()
                self._profile.viewProfile()
                while True:
                    choice = input(
                        "\n\t(0) Go Back to Dashboard\n\t(1) Update Profile\n\n> "
                    )
                    if choice == "0":
                        break
                    elif choice == "1":
                        self._profile.updateProfile()
                        break
                    else:
                        print("\nInvalid option.\n")

            elif menu_option == "6":
                self.change_password()

            elif menu_option == "0":
                self.logout()
                break

            else:
                print("Invalid option, please try again.")
