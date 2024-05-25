# Define heuristic functions for A* Search
def manhattan_distance(state, goal):
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


def euclidean_distance(state, goal):
    return ((state[0] - goal[0]) ** 2 + (state[1] - goal[1]) ** 2) ** 0.5

