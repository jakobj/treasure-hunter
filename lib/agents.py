import itertools


class FixedStepAgent:

    def __init__(self, dna):
        self.dna = dna
        self.step = 0

    def next_move(self, _):
        m = self.dna[self.step]
        self.step += 1
        return m


class SensorAgent:

    def __init__(self, dna, env_states):
        self.moves = {}
        for i, obs in enumerate(itertools.product(env_states, repeat=4)):
            self.moves[obs] = dna[i]

    def next_move(self, obs):
        return self.moves[obs]
