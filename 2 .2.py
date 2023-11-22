class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Manager(Person):
    manager_count = 0

    def __init__(self, first_name, last_name, employee_id, salary):
        super().__init__(first_name, last_name)
        self.employee_id = employee_id
        self.salary = salary
        Manager.manager_count += 1

    def __str__(self):
        return f"Manager: {super().__str__()}, Employee ID: {self.employee_id}, Salary: {self.salary}"


class Employee(Person):
    employee_count = 0

    def __init__(self, first_name, last_name, employee_id, rank):
        super().__init__(first_name, last_name)
        self.employee_id = employee_id
        self.rank = rank
        Employee.employee_count += 1

    def __str__(self):
        return f"Employee: {super().__str__()}, Employee ID: {self.employee_id}, Rank: {self.rank}"


class Intern(Person):
    intern_count = 0
    internship_duration = 12

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        Intern.intern_count += 1

    def __str__(self):
        return f"Intern: {super().__str__()}, Internship Duration: {Intern.internship_duration} months"


# نمونه‌هایی از هر کلاس
manager1 = Manager("John", "Doe", "M001", 5000)
employee1 = Employee("Alice", "Smith", "E001", "A")
intern1 = Intern("Bob", "Brown")

# ذخیره در لیست و نمایش
people = [manager1, employee1, intern1]
for person in people:
    print(person)

# نمایش تعداد نمونه‌ها برای هر کلاس
print(f"Number of Managers: {Manager.manager_count}")
print(f"Number of Employees: {Employee.employee_count}")
print(f"Number of Interns: {Intern.intern_count}")
