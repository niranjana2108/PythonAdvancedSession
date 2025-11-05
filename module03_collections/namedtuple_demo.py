from collections import namedtuple

class NamedTupleDemo:
    def demo(self):
        Employee = namedtuple("Employee", ["name", "age", "department"])
        emp = Employee("Nina", 28, "QA Automation")
        print(f"Employee Name: {emp.name}, Age: {emp.age}, Department: {emp.department}")
        emp2 = Employee("Reena", 18, "QA Automation")
        print(f"Employee Name: {emp2.name}, Age: {emp2.age}, Department: {emp2.department}")


if __name__ == "__main__":
    print("=== NamedTuple Demo ===")
    NamedTupleDemo().demo()