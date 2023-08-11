# Задание No6
# 📌 Доработайте задачу 5.
# 📌 Вынесите общие свойства и методы классов в класс Животное.
# 📌 Остальные классы наследуйте от него.
# 📌 Убедитесь, что в созданные ранее классы внесены правки.

class Animal:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

    def get_info(self):
        return f'{type(self).__name__}: {self.name}, {self.color}, {self.size}'


class Fish(Animal):
    def __init__(self, name: str, color: str, size: float, max_depth: float):
        super().__init__(name, color, size)
        self.max_depth = max_depth

    def get_info(self):
        return super().get_info() + f', {self.max_depth}'


class Bird(Animal):
    def __init__(self, name, color, size, habitat):
        super().__init__(name, color, size)
        self.habitat = habitat

    def get_info(self):
        return super().get_info() + f', {self.habitat}'


class Cat(Animal):
    def __init__(self, name, color, size, hairy: bool):
        super().__init__(name, color, size)
        self.hairy = hairy

    def get_info(self):
        return super().get_info() + f', {self.hairy}'


if __name__ == '__main__':
    fish = Fish('Flounder', 'orange', 10.2, 15.0)
    bird = Bird('Chichi', 'white', 82.3, 'forest')
    cat = Cat('Tom', 'black and white', 11, True)

    animals = (fish, bird, cat)
    for animal in animals:
        print(animal.get_info())

        # Fish: Flounder, orange, 10.2, 15.0
        # Bird: Chichi, white, 82.3, forest
        # Cat: Tom, black and white, 11, True
