class Pizza:
    pieces = 8

    @classmethod
    def change_size(cls, pieces):
        cls.pieces = pieces


class Mussarela(Pizza):
    ...


class Calabresa(Pizza):
    ...


class MeioAMeio(Mussarela, Calabresa):
    ...
