class Student():
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    def printStudent(self):
        print(f"Name: {self.name}, Age: {self.age}, Hobby: {self.hobby}")

    def send_homework(self):
        pass

    def get_homework_mark(self):
        pass

    def get_class_mark(self):
        pass


student1 = Student("Харчок Fox", 228, "опілок")
student2 = Student("Sophia", 13, "studing reading")
student3 = Student("Опілок Skizy", 245, "харчок")
student4 = Student("Діма", 1488, "programming")
student5 = Student("Кашка", 1, "хоббі")

print(student1)
student2.printStudent()
student4.printStudent()

