import matplotlib.pyplot as plt
import numpy as np
import pickle
import sys

from lib import agents, game, utils


def visualize_fitness(history):

    plt.yscale('log')
    plt.plot(history['fitness'])
    plt.show()


if __name__ == '__main__':

    fn = sys.argv[1]

    with open(fn, 'rb') as f:
        history = pickle.load(f)

    visualize_fitness(history)

    level_dict = utils.parse_level(f'levels/level_{history["params"]["level"]}.txt')
    agent = agents.FixedStepAgent(history['dna'][-1], level_dict)
    game.play(level_dict, agent, history['params']['max_steps'], do_draw_game_state=True)
