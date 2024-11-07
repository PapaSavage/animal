class Animal:
    def init(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("The make_sound method should be implemented in a subclass")

    def info(self):
        return f"{self.name} — {self.age} years old"
