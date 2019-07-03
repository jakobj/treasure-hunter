import itertools


class FixedStepAgent:

    def __init__(self, dna, _):
        self.dna = dna
        self.step = 0

    def next_move(self, *_):
        m = self.dna[self.step]
        self.step += 1
        return m
