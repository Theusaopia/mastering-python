"""Implementing a container"""
from collections.abc import Container, Sized, Collection


class Box(Collection):
    def __init__(self, seq):
        self.seq = seq

    def __contains__(self, item):
        return item in list(self.seq)

    def __len__(self):
        return len(self.seq)

    def __iter__(self):
        return self

