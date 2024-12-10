class Scholarship:
    def __init__(self, required_gwa, discount, type):
        self.__required_gwa = required_gwa
        self.__discount = discount
        self.__type = type

    def get_type(self):
        return self.__type

    def get_discount(self):
        return self.__discount

    def apply(self, student):
        student.scholarship = self

    def verify_eligibility(self, gwa):
        return gwa <= self.__required_gwa

    def deduct_tuition(self, total_tuition):
        return total_tuition * (1 - self.__discount)
        # student.view_balance()
