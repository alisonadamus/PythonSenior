import random

class Human:
    def __init__(self, name):
        self.name = name
        self.money = 100
        self.hunger = 50
        self.happiness = 50
        self.car = Car()
        self.home = House()
        self.job = Job()

    def eat(self):
        if self.home.food <= 0:
            print("Немає їжі — йду в магазин 🛒")
            self.shop("food")
        else:
            print("Їм 🍽️")
            self.hunger += 20
            self.home.food -= 10
        self.hunger = min(100, self.hunger)

    def work(self):
        if not self.car.drive():
            print("Машина зламалась, треба ремонтувати 🔧")
            self.repair_car()
            return
        print(f"Працюю як {self.job.name} 💼")
        self.money += self.job.salary
        self.hunger -= 15
        self.happiness -= 10

    def relax(self):
        print("Відпочиваю 🎮")
        self.happiness += 15
        self.hunger -= 5

    def clean(self):
        print("Прибираю вдома 🧹")
        self.home.mess = max(0, self.home.mess - 20)
        self.happiness -= 5

    def repair_car(self):
        print("Ремонтую машину 🔧")
        self.money -= 30
        self.car.strength += 40

    def shop(self, item):
        if item == "food":
            print("Купую їжу 🍞")
            self.money -= 20
            self.home.food += 30
        elif item == "fun":
            print("Купую смаколики 🍰")
            self.money -= 10
            self.happiness += 10

    def show_status(self, day):
        print(f"\n===== День {day}: {self.name} =====")
        print(f"Гроші: {self.money}")
        print(f"Голод: {self.hunger}")
        print(f"Щастя: {self.happiness}")
        print(f"Їжа вдома: {self.home.food}")
        print(f"Безлад у домі: {self.home.mess}")
        print(f"Машина — паливо: {self.car.fuel}, стан: {self.car.strength}")

    def live_day(self, day):
        self.show_status(day)

        if self.hunger < 20:
            self.eat()
        elif self.money < 20:
            self.work()
        elif self.happiness < 30:
            self.relax()
        else:
            action = random.choice(["work", "relax", "clean", "shop"])
            if action == "work":
                self.work()
            elif action == "relax":
                self.relax()
            elif action == "clean":
                self.clean()
            elif action == "shop":
                self.shop("fun")

        self.hunger -= random.randint(2, 5)
        self.happiness -= random.randint(1, 3)
        self.home.mess += random.randint(0, 5)


        if self.hunger <= 0:
            print("💀 Ви зголодніли...")
            return False
        if self.happiness <= 0:
            print("💀 Ви в депресії...")
            return False
        if self.money < -100:
            print("💀 Ви збанкрутіли...")
            return False
        return True


class Car:
    def __init__(self):
        self.fuel = 50
        self.strength = 80

    def drive(self):
        if self.strength > 10 and self.fuel >= 5:
            self.fuel -= 5
            self.strength -= 5
            return True
        return False


class House:
    def __init__(self):
        self.food = 20
        self.mess = 0


class Job:
    def __init__(self):
        jobs = {
            "Програміст": 50,
            "Вчитель": 40,
            "Таксист": 30,
            "Дизайнер": 45
        }
        self.name, self.salary = random.choice(list(jobs.items()))


name = input("Введи ім'я персонажа: ")
person = Human(name)

for day in range(1, 7):
    if not person.live_day(day):
        break

print("\nКінець гри")
