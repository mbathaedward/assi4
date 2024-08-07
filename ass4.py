# Base Class: Employee
class Employee:
    def __init__(self, name, employee_id, base_salary):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary

    def __str__(self):
        return f"Employee [Name: {self.name}, ID: {self.employee_id}, Base Salary: {self.base_salary}]"

    def calculate_salary(self):
        return self.base_salary

# Subclass: FullTimeEmployee
class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, benefits):
        super().__init__(name, employee_id, base_salary)
        self.benefits = benefits

    def __str__(self):
        return f"FullTimeEmployee [Name: {self.name}, ID: {self.employee_id}, Base Salary: {self.base_salary}, Benefits: {self.benefits}]"

    def calculate_salary(self):
        return self.base_salary + self.benefits

# Subclass: PartTimeEmployee
class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id, hourly_rate * hours_worked)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def __str__(self):
        return f"PartTimeEmployee [Name: {self.name}, ID: {self.employee_id}, Hourly Rate: {self.hourly_rate}, Hours Worked: {self.hours_worked}]"

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

# Class: Company
class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        if not self.employees:
            print("No employees in the company.")
        for employee in self.employees:
            print(employee)

    def calculate_total_salary(self):
        total_salary = sum(employee.calculate_salary() for employee in self.employees)
        return total_salary

# Usage
if __name__ == "__main__":
    # Create a company
    my_company = Company()

    # Add some employees
    emp1 = FullTimeEmployee("Edward", 200, 60000, 20000)
    emp2 = PartTimeEmployee("Daniel", 300, 80, 100)
    emp3 = FullTimeEmployee("Tom", 500, 80000, 20000)
    emp4 = FullTimeEmployee("joshua", 600, 90000, 10000)
    emp5 = FullTimeEmployee("martin", 500, 80000, 20000)


    # Add employees to the company
    my_company.add_employee(emp1)
    my_company.add_employee(emp2)
    my_company.add_employee(emp3)
    my_company.add_employee(emp4)
    my_company.add_employee(emp4)


    # Display all employees
    my_company.display_employees()

    # Calculate total salary expense
    total_salary = my_company.calculate_total_salary()
    print(f"Total Salary Expense: {total_salary}")