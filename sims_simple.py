import random

class Need:
    def __init__(self, name, value=100):
        self.name = name
        self.value = value

    def add(self, x):
        self.value = min(100, self.value + x)

    def sub(self, x):
        self.value = max(0, self.value - x)

    def __str__(self):
        return f"{self.name}: {self.value}"


class Sim:
    def __init__(self, name):
        self.name = name
        self.energy = Need("Енергія", 80)
        self.hunger = Need("Голод", 20)
        self.mood = Need("Настрій", 80)
        self.alive = True

    def eat(self):
        print(f"{self.name} їсть 🍎")
        self.hunger.sub(30)
        self.energy.add(10)
        self.mood.add(5)

    def sleep(self):
        print(f"{self.name} спить 😴")
        self.energy.add(40)
        self.hunger.add(10)

    def play(self):
        print(f"{self.name} грається 🎮")
        self.mood.add(20)
        self.energy.sub(10)
        self.hunger.add(10)

    def work(self):
        print(f"{self.name} працює 💼")
        self.energy.sub(20)
        self.mood.sub(15)
        self.hunger.add(20)

    def show_status(self):
        print(f"\n=== {self.name} ===")
        print(self.energy)
        print(self.hunger)
        print(self.mood)
        print("==================")

    def update(self):
        self.energy.sub(random.randint(0, 5))
        self.hunger.add(random.randint(0, 5))
        self.mood.sub(random.randint(0, 3))
        if self.energy.value == 0 or self.hunger.value == 100 or self.mood.value == 0:
            self.alive = False


def main():
    name = input("Введи ім’я персонажа: ")
    sim = Sim(name)

    while sim.alive:
        sim.show_status()
        print("\n1 - Їсти 🍎")
        print("2 - Спати 😴")
        print("3 - Грати 🎮")
        print("4 - Працювати 💼")
        print("0 - Вийти 🚪")

        action = input(">> ")

        if action == "0":
            print("До зустрічі!")
            break
        elif action == "1":
            sim.eat()
        elif action == "2":
            sim.sleep()
        elif action == "3":
            sim.play()
        elif action == "4":
            sim.work()
        else:
            print("Невідома команда!")

        sim.update()

    if not sim.alive:
        print(f"\n{sim.name} занадто виснажений... Гра закінчена!")



main()
