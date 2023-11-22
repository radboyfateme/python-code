class Company:
    def __init__(self, name, manager, address, num_employees, revenue):
        self.name = name
        self.manager = manager
        self.address = address
        self.num_employees = num_employees
        self.revenue = revenue

    def calculate_productivity(self):
        if self.num_employees == 0:
            return 0
        return self.revenue / self.num_employees

    def __str__(self):
        return (f"Company Name: {self.name}\n"
                f"Manager: {self.manager}\n"
                f"Address: {self.address}\n"
                f"Number of Employees: {self.num_employees}\n"
                f"Revenue: {self.revenue}\n"
                f"Productivity per Employee: {self.calculate_productivity()}")

# نمونه ای از کلاس
xyz_company = Company("XYZ", "John Doe", "123 Main St", 100, 500000)

# نمایش نمونه
print(xyz_company)
