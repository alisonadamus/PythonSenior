class Phone:
    def call(self, number):
        print(f"Дзвінок на номер {number}...")

class Camera:
    def take_photo(self):
        print("Фото зроблено!")

class Smartphone(Phone, Camera):
    def browse_internet(self):
        print("Відкриття браузера...")

my_phone = Smartphone()

my_phone.call("123-456")
my_phone.take_photo()
my_phone.browse_internet()
