class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def give_raise(self, amount):
        if amount > 0:
            self._salary += amount
            return f"{self.name} got a raise of {amount}. New salary: {self._salary}"
        return "Invalid raise amount!"

    def get_salary(self):
        return f"{self.name}'s salary: {self._salary}"



emp1 = Employee("Mary", 50000)
emp2 = Employee("Bob", 60000)

print(emp1.give_raise(5000))
print(emp2.get_salary())
print(emp1._salary)
