class Two:
    val = 2

    def __neg__(self):
        print('Unary, negating')
        return -self.val

    def __pos__(self):
        print('Unary, getting positive')
        return +self.val


class MyString:
    def __init__(self):
        self.s = 'Matthew'

    def __neg__(self):
        return self.s[::-1]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __pos__(self):
        return Point(+self.x, +self.y)

    def __repr__(self):
        return f'Ponto({self.x}, {self.y})'
