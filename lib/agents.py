import itertools


class FixedStepAgent:

    def __init__(self, dna, _):
        self.dna = dna
        self.step = 0

    def next_move(self, *_):
        m = self.dna[self.step]
        self.step += 1
        return m


class PositionDependentAgent:

    def __init__(self, dna, level_dict):
        self.moves = {}
        for i, state in enumerate(level_dict):
            if state != 'props' and level_dict[state] not in ('#', '\n'):
                self.moves[state] = dna[i]

    def next_move(self, state, _):
        return self.moves[state]


# class SensorAgent:

#     def __init__(self, dna, env_states):
#         self.moves = {}
#         for i, obs in enumerate(itertools.product(env_states, repeat=4)):
#             self.moves[obs] = dna[i]

#     def next_move(self, _, obs):
#         return self.moves[obs]
