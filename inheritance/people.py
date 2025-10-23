class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Привіт! Мене звати {self.name}, мені {self.age} років.")

    def celebrate_birthday(self):
        self.age += 1
        print(f"{self.name} святкує день народження! Тепер йому/їй {self.age}!")


class Student(Person):
    def __init__(self, name, age, specialty, course, group):
        super().__init__(name, age)
        self.specialty = specialty
        self.course = course
        self.group = group
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)
        print(f"{self.name} отримав оцінку {grade}")

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def introduce(self):
        super().introduce()
        print(f"Я студент спеціальності '{self.specialty}', {self.course}-го курсу, група {self.group}.")


class Worker(Person):
    def __init__(self, name, age, position, salary, experience):
        super().__init__(name, age)
        self.position = position
        self.salary = salary
        self.experience = experience

    def introduce(self):
        super().introduce()
        print(f"Я працюю як {self.position}. Мій стаж — {self.experience} років, зарплата {self.salary} грн.")


    def increase_salary(self, percent):
        old_salary = self.salary
        self.salary += self.salary * percent / 100
        print(f"Зарплата {self.name} збільшена з {old_salary} до {self.salary}")




student = Student("Віталік", 19, "МКА", 3, "1321")
worker = Worker("Олег", 35, "Інженер-програміст", 25000, 10)

student.introduce()
student.add_grade(95)
student.add_grade(80)
print(f"Середній бал {student.name}: {student.average_grade():.1f}")
student.celebrate_birthday()
print()
worker.introduce()
worker.increase_salary(10)
worker.celebrate_birthday()
