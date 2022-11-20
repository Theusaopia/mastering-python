"""If counts as a Sequence and has items as a Sequence
   So is a Sequence"""
from collections.abc import MutableSequence


class MyList(MutableSequence):
    def __init__(self, *vals):
        self.vals = vals

    def __getitem__(self, item):
        return self.vals[item]

    def __len__(self):
        return len(self.vals)

    def __delitem__(self, key):
        del self.vals[key]

    def __setitem__(self, key, value):
        self.vals[key] = value

    def insert(self, key, value):
        self.vals[key] = value
