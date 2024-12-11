class Subject:
    def __init__(self, subject_code, subject_name, units, tuition_per_unit, instructor):
        self.__subject_code = subject_code
        self.__subject_name = subject_name
        self.__units = units
        self.__tuition_per_unit = tuition_per_unit
        self.__instructor = instructor

    def get_subject_code(self):
        return self.__subject_code

    def get_subject_name(self):
        return self.__subject_name

    def get_units(self):
        return self.__units

    def get_tuition(self):
        return self.__tuition_per_unit

    def get_instructor(self):
        return self.__instructor

    def view_details(self):
        return f"{[self.__subject_code]} {self.__subject_name}\n  Units: {self.__units}\n  Instructor: {self.__instructor.get_full_name()}"
