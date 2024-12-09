class Scholarship:
    def __init__(self, required_gwa, discount, type):
        self.required_gwa = required_gwa
        self.discount = discount
        self.type = type

    def apply(self, student):
        student.scholarship = self

    def verify_eligibility(self, gwa):
        return gwa <= self.required_gwa

    def deduct_tuition(self, student):
        student.view_balance()
