import collections
import matplotlib.pyplot as plt
import numpy as np
import pickle
import sys
import time

sys.path.insert(0, '../python-gp')
import gp

from lib import utils

LEVEL = 4


def draw_game_state(level_dict, position, step, max_step):

    game_state = dict(level_dict)
    game_state[position] = '*'

    print(step + 1, '/', max_step)
    for i in range(level_dict['n_rows']):
        for j in range(level_dict['n_cols']):
            print(game_state[(i, j)], end='')
    print()

    time.sleep(0.1)


inverse_novelty = collections.defaultdict(int)


def play(level_fn, moves, *, do_draw_game_state=False):

    level_dict = utils.parse_level(level_fn)

    position = level_dict['S']
    novelty = 0.
    for step, move in enumerate(moves):
        if move == 0:
            new_position = (position[0], position[1] + 1)
        elif move == 1:
            new_position = (position[0] - 1, position[1])
        elif move == 2:
            new_position = (position[0], position[1] - 1)
        elif move == 3:
            new_position = (position[0] + 1, position[1])
        else:
            assert False

        if level_dict[new_position] != '#':
            position = new_position

        if do_draw_game_state:
            draw_game_state(level_dict, position, step, len(moves))

        if inverse_novelty[position] > 0.:
            novelty += 1. / inverse_novelty[position]
        else:
            novelty += 1.

        if level_dict[position] == 'E':
            return novelty / step

        inverse_novelty[position] += 1.

    return novelty / len(moves)


def objective(individual):

    individual.fitness = play(f'levels/level_{LEVEL}.txt', individual.genome.dna)

    return individual


if __name__ == '__main__':

    pop_params = {
        'seed': 1234,
        'n_parents': 5,
        'n_offsprings': 5,
        'max_generations': 500,
        'n_breeding': 5,
        'tournament_size': 6,
        'mutation_rate': 0.1,
        'min_fitness': 1e12,
    }

    genome_params = {
        'genome_length': 100,
        'primitives': list(range(4)),
    }

    np.random.seed(pop_params['seed'])

    pop = gp.BinaryPopulation(
        pop_params['n_parents'], pop_params['n_offsprings'], pop_params['n_breeding'],
        pop_params['tournament_size'], pop_params['mutation_rate'], pop_params['seed'], genome_params)

    def record_history(pop, history):
        if 'fitness' not in history: history['fitness'] = []
        history['fitness'].append(pop.champion.fitness)
        if 'dna' not in history: history['dna'] = []
        history['dna'].append(pop.champion.genome.dna)

    history = gp.evolve(pop, objective, pop_params['max_generations'], pop_params['min_fitness'], record_history=record_history)
    history['level_fn'] = f'levels/level_{LEVEL}.txt'

    with open(f'results-{LEVEL}.pkl', 'wb') as f:
        pickle.dump(history, f)
