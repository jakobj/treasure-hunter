import matplotlib.pyplot as plt
import numpy as np
import pickle
import sys

from lib import utils
from main import play


def visualize_fitness(history):

    plt.plot(history['fitness'])
    plt.yscale('log')
    plt.ylim(1e-4, 1e0)
    plt.show()


if __name__ == '__main__':

    fn = sys.argv[1]

    with open(fn, 'rb') as f:
        history = pickle.load(f)

    # visualize_fitness(history)
    play(history['level_fn'], history['dna'][490], do_draw_game_state=True)
