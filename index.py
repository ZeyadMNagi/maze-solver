import sys

from modules.Frontiers import *
from modules.Maze import *
from modules.Heuristics import *


# Main function to run the program
def main():
    # Check if filename is provided as command-line argument
    if len(sys.argv) != 2:
        sys.exit("Usage: python main.py maze.txt")

    # Create a maze object
    m = Maze(sys.argv[1])

    # Prompt user to choose a search algorithm
    print("Choose a search algorithm:")
    print("1) DFS")
    print("2) BFS")
    print("3) UCS")
    print("4) A*")
    print("5) IDA*")
    print("6) Greedy Best First Search")
    choice = input("Enter the number of the algorithm: ")

    # Select the frontier based on the user's choice
    if choice == "1":
        frontier = StackFrontier()
    elif choice == "2":
        frontier = QueueFrontier()
    elif choice == "3":
        frontier = UCSFrontier()
    elif choice == "4":
        heuristic_choice = input(
            "Choose heuristic for A* (1: Manhattan Distance, 2: Euclidean Distance): "
        )
        heuristic = (
            manhattan_distance if heuristic_choice == "1" else euclidean_distance
        )
        frontier = AStarFrontier(heuristic, m.goal)
    elif choice == "5":
        heuristic_choice = input(
            "Choose heuristic for IDA* (1: Manhattan Distance, 2: Euclidean Distance): "
        )
        heuristic = (
            manhattan_distance if heuristic_choice == "1" else euclidean_distance
        )
        frontier = IDAStarFrontier(heuristic, m.goal)
    elif choice == "6":
        heuristic_choice = input(
            "Choose heuristic for Greedy Best First Search (1: Manhattan Distance, 2: Euclidean Distance): "
        )
        heuristic = (
            manhattan_distance if heuristic_choice == "1" else euclidean_distance
        )
        frontier = GreedyBestFirstSearchFrontier(heuristic, m.goal)

    else:
        sys.exit("Invalid choice")

    # Solve the maze
    print("Solving...")
    if choice == "5":
        # Special handling for IDA* as it uses a different solve mechanism
        solution_node = frontier.search(Node(state=m.start, parent=None, action=None))
        if solution_node:
            actions = []
            cells = []
            while solution_node.parent is not None:
                actions.append(solution_node.action)
                cells.append(solution_node.state)
                solution_node = solution_node.parent
            actions.reverse()
            cells.reverse()
            m.solution = (actions, cells)
    else:
        m.solve(frontier)

    # Output the results
    print("States Explored:", m.num_explored)
    print("Solution:")
    m.print_M()
    m.output_image("maze.png", show_explored=True)


if __name__ == "__main__":
    main()
