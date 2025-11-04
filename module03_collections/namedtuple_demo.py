from collections import namedtuple

class NamedTupleDemo:
    def demo(self):
        Employee = namedtuple("Employee", ["name", "age", "department"])
        emp = Employee("Nina", 28, "QA Automation")
        print(f"Employee Name: {emp.name}, Age: {emp.age}, Department: {emp.department}")
