# treasure-hunter

A variety of novelty search for agents evolving in grid worlds.

Novelty search (e.g., Lehman & Stanley, 2011) is based on the idea that instead of rewarding behavior leading to a specific goal the agents fitness is determined by their behavioral novelty with respect to past individuals. For the grid worlds considered here novelty can be defined simply as reaching grid positions that have been rarely visited by other agents before. This encourages the evolution of agents that are able to explore the grid more and more, causing them eventually to reach the goal position as a by product of generating novel behavior. To keep the search from moving away from such solutions that are indeed able to reach the specified goal, the novelty of the goal position constant, no matter how many agents have reached it. Note that this modification of the search might not be desirable if there would be multiple goals that should all be explored.

For simplicity we consider agents with innate behavior: each agents DNA defines a specific sequence of actions that are being executed one after the other, independent of the agents position within the grid world. Agents thus do not make use of any sensory information.

New levels can be defined via text files, with the following characters representing different elements of the grid world:
- ` `: open space
- `S`: start position
- `E`: goal position
- `#`: wall
- `+`: "fractured" wall that the agent can blow up

See `levels/` for example grid worlds.

Lehman, J., & Stanley, K. O. (2011). Abandoning objectives: Evolution through the search for novelty alone. Evolutionary computation, 19(2), 189-223.
