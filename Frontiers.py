# Node class represents a state in the maze
class Node:
    def __init__(self, state, parent, action, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost


# Frontier class for implementing various frontier types
class Frontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        pass

    def remove(self):
        pass

    def empty(self):
        return len(self.frontier) == 0

    def contain_state(self, state):
        return any(node.state == state for node in self.frontier)


# StackFrontier class for implementing a stack-based frontier
class StackFrontier(Frontier):
    def add(self, node):
        self.frontier.append(node)

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            return self.frontier.pop()


# QueueFrontier class for implementing a queue-based frontier
class QueueFrontier(Frontier):
    def add(self, node):
        self.frontier.append(node)

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            return self.frontier.pop(0)


# UCSFrontier class for implementing Uniform Cost Search
class UCSFrontier(Frontier):
    def add(self, node):
        self.frontier.append(node)
        self.frontier.sort(key=lambda x: x.path_cost)

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            return self.frontier.pop(0)


# AStarFrontier class for implementing A* Search
class AStarFrontier(Frontier):
    def __init__(self, heuristic, goal):
        super().__init__()
        self.heuristic = heuristic
        self.goal = goal

    def add(self, node):
        self.frontier.append(node)
        self.frontier.sort(
            key=lambda x: x.path_cost + self.heuristic(x.state, self.goal)
        )

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            return self.frontier.pop(0)
