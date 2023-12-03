class Dog(object):
    def __init__(self, name, color):
        self.name = name
        # print("Nice you made a dog")
        self.color = color

    def speak(self):
        print("Hi I am", self.name, "and I'm a", self.color, "dog")

    def change_color(self, color):
        self.color = color

    def add_weight(self, weight):
        self.weight = weight


zeus = Dog("Zeus", "white")
bluey = Dog("Bluey", "blue")
zeus.change_color("orange")
zeus.add_weight(8)
zeus.speak()
bluey.speak()


# print(bluey.name)
# print(bluey.color)
print(zeus.weight)