class Bird:
    def __init__(self, name):
        self.name = name


class AngryBird(Bird):
    def __init__(self, name, shirt):
        super().__init__(name)
        self.shirt = shirt

    def __str__(self):
        return f'AngryBird(name="{self.name}", shirt="{self.shirt}")'
