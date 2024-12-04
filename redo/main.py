from Faculty import Faculty
from Portal import Portal
from Section import Section
from Student import Student
from Subject import Subject

student_id_counter = 1
faculty_id_counter = 1


# create sections
ccis3a = Section("CCIS3A", 2, 1)
ccis1a = Section("CCIS1A", 1, 1)

# create faculty
harold_henthorn = Faculty("Harold", "Henthorn", 1)
jhulyna_rubio = Faculty("Jhulyna", "Rubio", 2)

# create subjects
iml = Subject("IML", "Information Management", 3, 2000, jhulyna_rubio)
osl = Subject("OSL", "Operating Systems", 3, 1500, harold_henthorn)

ccis3a.add_subject(iml)
ccis3a.add_subject(osl)

# create users
student1 = Student("Vince Randall", "David", 1, ccis3a)
student2 = Student("Bins", "David", 2, ccis1a)


portal = Portal()

# while True:
#     print("\n-------- SPCF Portal --------")
#     print("[1] Login")
#     print("[0] Exit")
#     choice = input("Choose a menu option [1, 0]: ")

#     if choice == "1":
#         pass
#     elif choice == "0":
#         print("Exiting program...")
#         exit()
#     else:
#         print("Invalid choice. Please try again.")
