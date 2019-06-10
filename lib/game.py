import numpy as np
import time

from . import utils


def draw_game_state(level_dict, agent_position, step, max_step):

    game_state = dict(level_dict)
    game_state[agent_position] = '*'

    print(step + 1, '/', max_step)
    for i in range(level_dict['props']['n_rows']):
        for j in range(level_dict['props']['n_cols']):
            print(game_state[(i, j)], end='')
    print()

    time.sleep(0.1)


def play(level_dict, agent, max_steps, *, do_draw_game_state=False):

    agent_position = level_dict['props']['S']  # set agent to starting position

    history_state = np.empty((max_steps + 1, 2))
    history_state[0] = agent_position
    for step in range(1, max_steps + 1):
        # an observation consists of the content of the current and reachable
        # positions
        obs = (level_dict[agent_position],
               level_dict[(agent_position[0], agent_position[1] + 1)],
               level_dict[(agent_position[0] - 1, agent_position[1])],
               level_dict[(agent_position[0], agent_position[1] - 1)],
               level_dict[(agent_position[0] + 1, agent_position[1])])
        move = agent.next_move(agent_position, obs)
        if move == 0:
            new_agent_position = (agent_position[0], agent_position[1] + 1)
        elif move == 1:
            new_agent_position = (agent_position[0] - 1, agent_position[1])
        elif move == 2:
            new_agent_position = (agent_position[0], agent_position[1] - 1)
        elif move == 3:
            new_agent_position = (agent_position[0] + 1, agent_position[1])
        elif move == 4:  # blow up fractured wall
            if level_dict[(agent_position[0], agent_position[1] + 1)] == '+':
                level_dict[(agent_position[0], agent_position[1] + 1)] = ' '
            if level_dict[(agent_position[0] - 1, agent_position[1])] == '+':
                level_dict[(agent_position[0] - 1, agent_position[1])] = ' '
            if level_dict[(agent_position[0], agent_position[1] - 1)] == '+':
                level_dict[(agent_position[0], agent_position[1] - 1)] = ' '
            if level_dict[(agent_position[0] + 1, agent_position[1])] == '+':
                level_dict[(agent_position[0] + 1, agent_position[1])] = ' '
            new_agent_position = agent_position  # blowing up a fractured wall does not move the agent
        else:
            assert False

        if level_dict[new_agent_position] not in ('#', '+'):  # not possible to walk through (fractured) walls
            agent_position = new_agent_position

        history_state[step] = agent_position

        if do_draw_game_state:
            draw_game_state(level_dict, agent_position, step, max_steps)

        if level_dict[agent_position] == 'E':  # reached the end
            return history_state[:step + 1]

    return history_state
