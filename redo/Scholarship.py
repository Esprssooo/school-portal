class Scholarship:
    def __init__(self, required_gwa, discount, type):
        self.required_gwa = required_gwa
        self.discount = discount
        self.type = type

    def apply(self, student):
        student.scholarship = self

    def verify_eligibility(self, gwa):
        return gwa <= self.required_gwa

    def deduct_tuition(self, total_tuition):
        return total_tuition * (1 - self.discount)
        # student.view_balance()
