from data import sections_data
from Faculty import Faculty
from Portal import Portal
from Section import Section
from Student import Student
from Subject import Subject
from Scholarship import Scholarship


# populate data
portal = Portal()
for section_data in sections_data:
    # create section object
    section = Section(
        section_data["section_name"], section_data["year"], section_data["semester"]
    )
    portal.add_section(section)

    # create faculty objects
    for subject_data in section_data["subjects"]:
        if subject_data["instructor"]["faculty_id"] not in portal.get_faculties():
            faculty = Faculty(
                subject_data["instructor"]["first_name"],
                subject_data["instructor"]["last_name"],
                subject_data["instructor"]["faculty_id"],
            )
            portal.add_faculty(faculty)
        else:
            faculty = portal.get_faculty(subject_data["instructor"]["faculty_id"])

        # create subject objects
        subject = Subject(
            subject_data["subject_code"],
            subject_data["subject_name"],
            subject_data["units"],
            subject_data["tuition_per_unit"],
            faculty,
        )
        section.add_subject(subject)

        faculty.handle_classes(subject.get_subject_name(), section)

    # create student objects
    for student in section_data["students"]:
        student = Student(
            student["first_name"],
            student["last_name"],
            student["student_id"],
            student["program"],
            section,
        )
        section.add_student(student)
        portal.add_student(student)

portal.add_scholarship(Scholarship(1.1, 1, "Academic"))
portal.add_scholarship(Scholarship(1.3, 0.75, "Academic"))
portal.add_scholarship(Scholarship(1.5, 0.5, "Academic"))


while True:
    # check_sections()
    print("\n-------- SPCF Portal --------")
    print("[1] Login")
    print("[0] Exit")
    choice = input("Choose a menu option [1, 0]: ")

    if choice == "1":
        username = input("Username (ID): ")
        password = input("Password: ")
        current_user = portal.login(username, password)

        if current_user:
            current_user.dashboard(portal)

    elif choice == "0":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
