import random

class Weather:
    conditions = ["☀️ Сонячно", "🌧️ Дощ", "⛅ Хмарно", "❄️ Сніг", "🌪️ Вітер"]

    def __init__(self, city):
        self.city = city
        self.temperature = random.randint(-10, 35)
        self.condition = random.choice(self.conditions)

    def show(self):
        print(f"{self.city}: {self.temperature}°C, {self.condition}")


w1 = Weather("Ужгород")
w2 = Weather("Київ")
w3 = Weather("Львів")

w1.show()
w2.show()
w3.show()