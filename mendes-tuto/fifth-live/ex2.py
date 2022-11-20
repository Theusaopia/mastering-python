"""If counts as a Sequence and has items as a Sequence
   So is a Sequence"""
from collections.abc import Sequence


class MyTuple(Sequence):
    def __init__(self, *vals):
        self.vals = vals

    def __getitem__(self, item):
        return self.vals[item]

    def __len__(self):
        return len(self.vals)
