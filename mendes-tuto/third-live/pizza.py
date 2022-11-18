class Pizzeria:
    def __init__(self):
        self._pizza_maker = PizzaMaker()

    def order(self, pizza):
        self._pizza_maker.make_pizza(pizza)


class Oven:
    def __init__(self):
        self.pizzas = []
        self.firewood = None

    def cook(self, pizza):
        if not self.firewood:
            print('Theres no firewood')


class PizzaMaker:
    def __init__(self):
        self._oven = Oven()

    def make_pizza(self, pizza):
        self._oven.cook(pizza)
