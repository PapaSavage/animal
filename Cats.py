import Animal

class Cat(Animal):
    def init(self, name, age, breed):
        super().init(name, age)  # Call the constructor of the base class
        self.breed = breed

    def make_sound(self):
        return "Meow!"

    def info(self):
        return f"{super().info()}, breed: {self.breed}"