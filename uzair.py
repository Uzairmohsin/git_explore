class Employee:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"The name of the employee is {self.name} and the age is {self.age} years old"