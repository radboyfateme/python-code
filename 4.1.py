class Student:
    school_name = "Downtown Elementary School"

    def __init__(self, student_id, first_name, last_name, grade):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade

    def __eq__(self, other):
        return self.student_id == other.student_id

    def __hash__(self):
        return hash(self.student_id)

    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name

    @staticmethod
    def display_subjects(grade):
        subjects = {
            1: ["Math", "Science"],
            2: ["Math", "Science", "Art"],
            3: ["Math", "Science", "Art", "History"],
            # ... و غیره
        }
        return subjects.get(grade, [])

    def display(self):
        return f"Student ID: {self.student_id}, Name: {self.first_name} {self.last_name}, Grade: {self.grade}"

# تعریف 10 نمونه دانش‌آموز
students = [
    Student(1, "John", "Doe", 1),
    Student(2, "Jane", "Doe", 2),
    # ... سایر دانش‌آموزان
]

# نمایش اطلاعات دانش‌آموزان
for student in students:
    print(student.display())

# فراخوانی استاتیک متد
print("Subjects for Grade 1:", Student.display_subjects(1))

# تغییر و نمایش نام دبستان
Student.change_school_name("New Elementary School")
print("New School Name:", Student.school_name)
