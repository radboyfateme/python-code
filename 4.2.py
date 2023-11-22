class Applicant:
    def __init__(self, name, family_name, national_id, field_of_study, address):
        self.name = name
        self.family_name = family_name
        self.national_id = national_id
        self.field_of_study = field_of_study
        self.address = address

    def calculate_score(self):
        raise NotImplementedError("This method should be implemented by subclasses")

    def __str__(self):
        return f"Applicant {self.name} {self.family_name}, National ID: {self.national_id}, Field of Study: {self.field_of_study}, Address: {self.address}"


class FreeApplicant(Applicant):
    def __init__(self, name, family_name, national_id, field_of_study, address, written_exam_score, interview_score):
        super().__init__(name, family_name, national_id, field_of_study, address)
        self.written_exam_score = written_exam_score
        self.interview_score = interview_score

    def calculate_score(self):
        return (self.written_exam_score + self.interview_score) / 2


class GraduateApplicant(Applicant):
    def __init__(self, name, family_name, national_id, field_of_study, address, university_rank, gpa):
        super().__init__(name, family_name, national_id, field_of_study, address)
        self.university_rank = university_rank
        self.gpa = gpa

    def calculate_score(self):
        university_score = {1: 100, 2: 80, 3: 60}.get(self.university_rank, 0)
        gpa_score = 60 if 16 <= self.gpa <= 17.5 else 80 if 17.5 < self.gpa <= 18.5 else 100 if self.gpa > 18.5 else 0
        return (university_score + gpa_score) / 2


class ContractEmployeeApplicant(Applicant):
    def __init__(self, name, family_name, national_id, field_of_study, address, work_experience_years, performance_rating):
        super().__init__(name, family_name, national_id, field_of_study, address)
        self.work_experience_years = work_experience_years
        self.performance_rating = performance_rating

    def calculate_score(self):
        experience_coefficient = 0.1 if 1 < self.work_experience_years <= 5 else 0.2 if self.work_experience_years > 5 else 0
        return (self.performance_rating * experience_coefficient) + self.performance_rating


# برنامه اصلی
applicants = [
    FreeApplicant("John", "Doe", "123456", "Computer Science", "City A", 85, 90),
    GraduateApplicant("Jane", "Doe", "654321", "Electrical Engineering", "City B", 1, 19.0),
    ContractEmployeeApplicant("Mike", "Smith", "789123", "Mechanical Engineering", "City C", 6, 95),
    
]

# نمایش اسامی پذیرفته‌شدگان (نمره 90 و بالاتر)
accepted_applicants = [applicant for applicant in applicants if applicant.calculate_score() >= 90]
for applicant in accepted_applicants:
    print(applicant)
