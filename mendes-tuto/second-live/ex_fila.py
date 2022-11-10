class Fila:
    c_fila = []  # is available for all instances as well as the class

    @classmethod
    def c_entrar(cls, obj):
        cls.c_fila.append(obj)
        print(cls.c_fila)

    def __init__(self):  # somehow it's different from a constructor
        self.s_fila = []  # only available in object instances

    def s_entrar(self, obj):
        self.s_fila.append(obj)
        print(self.s_fila)
