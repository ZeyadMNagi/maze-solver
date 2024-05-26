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


class IDAStarFrontier(Frontier):
    def __init__(self, heuristic, goal):
        super().__init__()
        self.heuristic = heuristic
        self.goal = goal
        self.threshold = float("inf")

    def add(self, node):
        self.frontier.append(node)

    def search(self, start_node):
        self.threshold = self.heuristic(start_node.state, self.goal)
        while True:
            result = self._search_recursive(start_node, 0)
            if result is not None:
                return result
            self.threshold *= 2

    def _search_recursive(self, node, cost):
        f = cost + self.heuristic(node.state, self.goal)
        if f > self.threshold:
            return None
        if node.state == self.goal:
            return node
        self.frontier.append(node)
        while self.frontier:
            next_node = self.frontier.pop()
            result = self._search_recursive(next_node, cost + 1)
            if result is not None:
                return result
        return None


class GreedyBestFirstSearchFrontier(Frontier):
    def __init__(self, heuristic, goal):
        super().__init__()
        self.heuristic = heuristic
        self.goal = goal

    def add(self, node):
        self.frontier.append(node)
        self.frontier.sort(key=lambda x: self.heuristic(x.state, self.goal))

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            return self.frontier.pop(0)
