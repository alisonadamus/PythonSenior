import random

class Hero:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.attack_power = random.randint(10, 30)

    def attack(self, other):
        damage = random.randint(5, self.attack_power)
        other.health -= damage
        print(f"{self.name} атакує {other.name} на {damage}!")

    def is_alive(self):
        return self.health > 0

hero1 = Hero("Arthur")
hero2 = Hero("John", health=120)

while hero1.is_alive() and hero2.is_alive():
    hero1.attack(hero2)
    if not hero2.is_alive():
        print(f"{hero2.name} переможений")
        break
    hero2.attack(hero1)
    if not hero1.is_alive():
        print(f"{hero1.name} переможений")
        break

