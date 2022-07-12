class Animal:
    def __init__(self, color):
        self.num_eyes = 2
        self.color = color

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self, color):
        super().__init__(color)

    def breathe(self):
        super().breathe()
        print("doing this underwater")

    def swim(self):
        print("moving in water.")


monkey = Animal("brown")
nimo = Fish("red")


print(f"Fish color is {nimo.color}")

print(nimo.num_eyes)
nimo.breathe()
nimo.swim()
