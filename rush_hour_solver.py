import os
import sys
import time
from controller.bloader import BLoader
from helper.search_instance_printer import *
from model.node import Node
from model.search_instance import SearchInstance
from controller.bloader import BLoader
from node_searcher import NodeSearcher
from view.console_v import ConsoleView


def execute_all_algorithms_and_heuristics(start_node: Node) -> list[SearchInstance]:
    #Execute search using each algorithm and each heuristic
    solutions: list[SearchInstance] = []
    solutions.append(NodeSearcher("UCS").execute_search(start_node))
    for h in range(1, 5):
        solutions.append(NodeSearcher("GBFS").execute_search(start_node, h))
        solutions.append(NodeSearcher("A_Astar").execute_search(start_node, h))
    return solutions


class RushHourSolver(object):
    def __init__(self):
        self.console_view = ConsoleView()
        self.run()

    def run(self):
        # Ask user which game board load
        file_name = self.console_view.load_board_prompt()
 
        # Create directory to store output files if it does not already exist
        current_dir_path = os.getcwd()
        output_dir_path = os.path.join(current_dir_path, r'output_files')
        if not os.path.exists(output_dir_path):
            os.mkdir(output_dir_path)

        if file_name:
            # Load game board from file
            loader = BLoader('./datatxt/%s.txt' % file_name)
            puzzle_no = 1
            game_boards = loader.get_game_boards()

            for game_board in game_boards:
                # Find the solution to the game board for each algorithm and each heuristic
                start: Node = Node(gameboard=game_board)
                solutions = execute_all_algorithms_and_heuristics(start)
                for solution in solutions:
                    solution.puzzle_number = puzzle_no
                    write_solution_to_solution_file(solution, output_dir_path)
                puzzle_no += 1

            # Display game board
            #self.console_view.display_loaded_grid(game_board.get_grid(), game_board.get_height(), game_board.get_width())

            # Find the solution to the game board
            # start: Node = Node(gameboard=game_board)
            # solution = NodeSearcher("A_Astar").execute_search(start, 4)
            # solution.puzzle_number = puzzle_no
            # write_solution_to_solution_file(solution, output_dir_path)


        # Exit system
        self.console_view.display_exit_message()
        sys.exit()


if __name__ == "__main__":
    RushHourSolver()

