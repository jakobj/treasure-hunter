import matplotlib.pyplot as plt
import numpy as np
import pickle
import sys

from lib import agents, game, utils


def visualize_fitness(history):

    plt.yscale('log')
    plt.ylim(1e-5, 2e0)
    plt.plot(history['fitness'])
    plt.show()


if __name__ == '__main__':

    fn = sys.argv[1]

    with open(fn, 'rb') as f:
        history = pickle.load(f)

    visualize_fitness(history)

    for i in range(0, 500, 50):
        agent = agents.FixedStepAgent(history['dna'][i])
        level_dict = utils.parse_level(f'levels/level_{history["params"]["level"]}.txt')
        game.play(level_dict, agent, history['params']['max_steps'], do_draw_game_state=True)
