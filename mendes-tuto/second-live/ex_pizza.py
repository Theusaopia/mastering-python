class Pizza:
    pieces = 8

    def __init__(self, flavor):
        self.flavor = flavor

    def take_piece(self):
        self.pieces -= 1

    @classmethod
    def change_size(cls, pieces):
        cls.pieces = pieces

    @staticmethod
    def ingredients():
        return 'Tomato sauce, cheese, onion'
