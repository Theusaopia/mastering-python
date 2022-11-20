class CrazyList(list):
    def __add__(self, other):
        """ sum all the list values with other """
        return CrazyList([x + other for x in self])

    def __lshift__(self, other):
        """ Append on the list using << """
        self.append(other)

    def __rshift__(self, other):
        """ Remove item with >> """
        return self.pop(other)

    def __neg__(self):
        return CrazyList(reversed(self))
