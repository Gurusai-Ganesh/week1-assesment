#Task 1

#Bonus Function

from unicodedata import name


def bonus(salary, rate=0.1, *extras, **options):
    total = salary * rate
    total = total + sum(extras)
    if "cap" in options:
        total = min(total, options["cap"])
    return total
print("Bonus:", bonus(50000))
print("Bonus with extras:", bonus(50000, 0.1, 1000, 2000))
print("Bonus with cap:", bonus(50000, 0.1, 1000, 2000, cap=5000))

#Employee and Manager Classes

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def annual_salary(self):
        return self.salary * 12
    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}, Team Size: {self.team_size}"


emp = Employee("Arun", 30000)
manager = Manager("Rahul", 60000, 5)
print(emp.get_details())
print("Annual Salary:", emp.annual_salary())
print(manager.get_details())

#Custom Exception

class InvalidSalaryError(Exception):
    pass
try:
    salary = -5000
    if salary < 0:
        raise InvalidSalaryError("Invalid salary: Salary cannot be negative")
    print("Salary is valid")
except InvalidSalaryError as e:
    print("Error:", e)
finally:
    print("Transaction finished")

#List Comperhension

import csv

with open("data/employee18.csv", "r") as file:
    reader = csv.DictReader(file)
    employees = list(reader)

high_salary_names = [
    emp["employee_name"]
    for emp in employees
    if int(emp["salary"]) > 50000
]
print("Above 50000:", high_salary_names)

increased_salaries = list(
    map(
        lambda emp: int(emp["salary"]) * 1.10,
        employees
    )
)
print("10% Increased Salaries:", increased_salaries)

chennai_employees = list(
    filter(
        lambda emp: emp["city"] == "chennai",
        employees
    )
)
print("Chennai:", [emp["employee_name"] for emp in chennai_employees])

#For loop, continue and break

for emp in employees:
    salary = int(emp["salary"])
    if salary == 0:
        continue
    print(emp["employee_name"], salary)
    if salary > 85000:
        print("Salary above 85000 found")
        break