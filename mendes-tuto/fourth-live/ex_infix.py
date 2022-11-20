class Number:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return self.val + other

    def __radd__(self, other):
        return self.val + other

