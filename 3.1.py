class CourseLanguageProgramming:
    def __init__(self, course_code, start_date, end_date, level, fee, instructor):
        self.course_code = course_code
        self.start_date = start_date
        self.end_date = end_date
        self.level = level
        self.fee = fee
        self.instructor = instructor
        self.days = []

    def add_day(self, day):
        self.days.append(day)

    def __str__(self):
        days_str = ', '.join(self.days)
        return (f"Course Code: {self.course_code}, Level: {self.level}, Instructor: {self.instructor}, "
                f"Fee: {self.fee}, Days: {days_str}")


class PythonCourse(CourseLanguageProgramming):
    def __init__(self, course_code, start_date, end_date, level, fee, instructor):
        super().__init__(course_code, start_date, end_date, level, fee, instructor)


class JavaCourse(CourseLanguageProgramming):
    def __init__(self, course_code, start_date, end_date, level, fee, instructor):
        super().__init__(course_code, start_date, end_date, level, fee, instructor)


class PHPCourse(CourseLanguageProgramming):
    def __init__(self, course_code, start_date, end_date, level, fee, instructor):
        super().__init__(course_code, start_date, end_date, level, fee, instructor)


# نمونه‌هایی از هر کلاس
python_basic = PythonCourse("PY101", "2023-01-01", "2023-03-01", "Basic", 200, "John Doe")
python_basic.add_day("Monday")
python_basic.add_day("Wednesday")

python_advanced = PythonCourse("PY201", "2023-04-01", "2023-06-01", "Advanced", 300, "Jane Smith")
python_advanced.add_day("Tuesday")
python_advanced.add_day("Thursday")

java_basic = JavaCourse("JV101", "2023-01-01", "2023-03-01", "Basic", 200, "Mike Johnson")
java_basic.add_day("Monday")
java_basic.add_day("Wednesday")

java_advanced = JavaCourse("JV201", "2023-04-01", "2023-06-01", "Advanced", 300, "Emily Davis")
java_advanced.add_day("Tuesday")
java_advanced.add_day("Thursday")

php_basic = PHPCourse("PHP101", "2023-01-01", "2023-03-01", "Basic", 200, "Chris Brown")
php_basic.add_day("Monday")
php_basic.add_day("Wednesday")

php_advanced = PHPCourse("PHP201", "2023-04-01", "2023-06-01", "Advanced", 300, "Laura Wilson")
php_advanced.add_day("Tuesday")
php_advanced.add_day("Thursday")

# لیست دوره‌ها
courses = [python_basic, python_advanced, java_basic, java_advanced, php_basic, php_advanced]

# نمایش لیست دوره‌ها
for course in courses:
    print(course)

