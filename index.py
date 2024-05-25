import sys

from Frontiers import *
from Maze import * 

# Main function to run the program
def main():
    # Check if filename is provided as command-line argument
    if len(sys.argv) != 2:
        sys.exit("Usage: python maze.py maze.txt")

    # Create a maze object
    m = Maze(sys.argv[1])

    # Prompt user to choose a search algorithm
    print("Choose a search algorithm:")
    print("1) DFS")
    print("2) BFS")
    print("3) UCS")
    print("4) A*")
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
        if heuristic_choice == "1":
            frontier = AStarFrontier(manhattan_distance, m.goal)
        elif heuristic_choice == "2":
            frontier = AStarFrontier(euclidean_distance, m.goal)
        else:
            sys.exit("Invalid heuristic choice")
    else:
        sys.exit("Invalid choice")

    # Solve the maze using the selected search algorithm
    print("Solving...")
    m.solve(frontier)
    print("States Explored:", m.num_explored)
    print("Solution:")
    m.print_M()
    m.output_image("maze.png", show_explored=True)


if __name__ == "__main__":
    main()
