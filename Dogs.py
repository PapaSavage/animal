import Animal

class Dog(Animal):
    def init(self, name, age, breed):
        super().init(name, age)
        self.breed = breed

    def make_sound(self):
        return "Woof!"

    def info(self):
        return f"{super().info()}, breed: {self.breed}"