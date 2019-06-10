import collections
import itertools
import matplotlib.pyplot as plt
import numpy as np
import pickle
import sys
import time

sys.path.insert(0, '../python-gp')
import gp

from lib import agents, game, utils


if __name__ == '__main__':

    params = {
        'level': 3,
        'max_steps': 100,
        'agent_class': agents.FixedStepAgent,
        # 'agent_class': agents.SensorAgent,
    }

    pop_params = {
        'seed': 123,
        'n_parents': 5,
        'n_offsprings': 5,
        'max_generations': 500,
        'n_breeding': 5,
        'tournament_size': 6,
        'mutation_rate': 0.05,
        'min_fitness': 1e12,
    }

    genome_params = {
        'genome_length': params['max_steps'],
        # 'genome_length': len(list(itertools.product(utils.env_states, repeat=4))),
        'primitives': list(range(5)),
    }

    np.random.seed(pop_params['seed'])

    level_dict = utils.parse_level(f'levels/level_{params["level"]}.txt')
    inverse_novelty = collections.defaultdict(lambda: 1)
    def objective(individual):

        agent = params['agent_class'](individual.genome.dna)
        # agent = SensorAgent(individual.genome.dna, utils.env_states)

        history_state = game.play(level_dict, agent, params['max_steps'])

        individual.fitness = 0.
        for s in history_state:
            s = tuple(s)
            individual.fitness += 1. / inverse_novelty[s]
            if level_dict[s] != 'E':
                inverse_novelty[s] += 1.
        individual.fitness *= 1. / len(history_state)

        return individual

    pop = gp.BinaryPopulation(
        pop_params['n_parents'], pop_params['n_offsprings'], pop_params['n_breeding'],
        pop_params['tournament_size'], pop_params['mutation_rate'], pop_params['seed'], genome_params)

    def record_history(pop, history):
        if 'fitness' not in history: history['fitness'] = []
        history['fitness'].append(pop.champion.fitness)
        if 'dna' not in history: history['dna'] = []
        history['dna'].append(pop.champion.genome.dna)

    history = gp.evolve(pop, objective, pop_params['max_generations'], pop_params['min_fitness'], record_history=record_history)
    history['params'] = params

    fn = f'results-{params["level"]}.pkl'
    print(f'saving to {fn}')
    with open(fn, 'wb') as f:
        pickle.dump(history, f)
