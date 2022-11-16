class Pizza:
    pieces = 8

    @classmethod
    def change_size(cls, pieces):
        cls.pieces = pieces

    @staticmethod
    def ingredientes():
        return 'Ingredientes'


class Mussarela(Pizza):
    @staticmethod
    def ingredientes():
        return ['Queijo', 'Tomate']
