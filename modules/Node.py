# Node class represents a state in the maze
class Node:
    def __init__(self, state, parent, action, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
