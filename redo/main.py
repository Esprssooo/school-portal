from classes import *

student_id_counter = 1
facaulty_id_counter = 1

portal = SchoolPortal()

# create sections
ccis3a = Section("CCIS3A", 2, 1)

# create subjects
iml = Subject("IML", "Information Management", 3)
osl = Subject("OSL", "Operating Systems", 3)

# create users
student1 = Student("Vince Randall", "David", student_id_counter, ccis3a)
