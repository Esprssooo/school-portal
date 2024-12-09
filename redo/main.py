from data import sections_data
from Faculty import Faculty
from Portal import Portal
from Section import Section
from Student import Student
from Subject import Subject
from Scholarship import Scholarship

student_id_counter = 1
faculty_id_counter = 1

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
        if subject_data["instructor"]["faculty_id"] not in portal.faculties:
            faculty = Faculty(
                subject_data["instructor"]["first_name"],
                subject_data["instructor"]["last_name"],
                subject_data["instructor"]["faculty_id"],
            )
            faculty_id_counter += 1
            portal.add_faculty(faculty)
        else:
            faculty = portal.faculties[subject_data["instructor"]["faculty_id"]]

        # create subject objects
        subject = Subject(
            subject_data["subject_code"],
            subject_data["subject_name"],
            subject_data["units"],
            subject_data["tuition_per_unit"],
            faculty,
        )
        section.add_subject(subject)

        if subject.subject_name not in faculty.classes:
            faculty.classes[subject.subject_name] = []
        faculty.classes[subject.subject_name].append(section)
        # if subject not in faculty.classes:
        #     faculty.classes[subject] = []
        # faculty.classes[subject].append(section)

    # create student objects
    for student in section_data["students"]:
        student = Student(
            student["first_name"],
            student["last_name"],
            student["student_id"],
            student["program"],
            section,
        )
        student_id_counter += 1
        section.add_student(student)
        portal.add_student(student)

portal.add_scholarship(Scholarship(1.1, 1, "Academic"))
portal.add_scholarship(Scholarship(1.3, 0.75, "Academic"))
portal.add_scholarship(Scholarship(1.5, 0.5, "Academic"))

portal.students["S2"].grades["PROG1L"]["Prelim"] = 97.65
portal.students["S2"].grades["PROG1L"]["Midterm"] = 98.95
portal.students["S2"].grades["PROG1L"]["Final"] = 98.99
portal.students["S2"].grades["ITC"]["Prelim"] = 88
portal.students["S2"].grades["ITC"]["Midterm"] = 90
portal.students["S2"].grades["ITC"]["Final"] = 94


while True:
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


# # create sections
# ccis3a = Section("CCIS3A", 2, 1)
# ccis1a = Section("CCIS1A", 1, 1)

# # create faculty
# harold_henthorn = Faculty("Harold", "Henthorn", 1)
# jhulyna_rubio = Faculty("Jhulyna", "Rubio", 2)

# # create subjects
# iml = Subject("IML", "Information Management", 3, 2000, jhulyna_rubio)
# osl = Subject("OSL", "Operating Systems", 3, 1500, harold_henthorn)

# ccis3a.add_subject(iml)
# ccis3a.add_subject(osl)

# # create users
# student1 = Student("Vince Randall", "David", 1, ccis3a)
# student2 = Student("Bins", "David", 2, ccis1a)
