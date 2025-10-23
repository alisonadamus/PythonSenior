class Building():
    def __init__(self, height, weight, flor_number, material, address):
        self.height = height
        self.weight = weight
        self.area = self.get_area()
        self.flor_number = flor_number
        self.material = material
        self.address = address

    def get_area(self):
        return self.height * self.weight

    def info(self):
        print(f"Height: {self.height}, Weight: {self.weight}, Flor Number: {self.flor_number}, "
              f"Area: {self.area} Material: {self.material}, Address: {self.address}")


class School(Building):
    def __init__(self, height, weight, flor_number, material, address, name):
        super().__init__(height, weight, flor_number, material, address)
        self.name = name

school = School(100, 100, 1, "опілки", "ужгород", "IT STEP")
print(school.get_area())
print(school.info())

class Shop(Building):
    def __init__(self, height, weight, flor_number, material, address, name):
        pass
