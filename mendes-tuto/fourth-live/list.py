class CrazyList:
    def __init__(self, my_list):
        self.list = my_list or []

    def __add__(self, other):
        """ sum all the list values with other """
        return CrazyList([x + other for x in self.list])

    def __lshift__(self, other):
        """ Append on the list using << """
        self.list.append(other)

    def __rshift__(self, other):
        """ Remove item with >> """
        return self.list.pop(other)

    def __neg__(self):
        return CrazyList(reversed(self.list))

    # inplace operators
    # def __iadd__(self, other):
    #     """ sum all the list values with other and keep it in the obj """
    #     a = [x + other for x in self.list]
    #     self.list.clear()
    #     self.list.append(a)
