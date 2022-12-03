import os
import sys
import time
from controller.bloader import BLoader
from helper.search_instance_printer import *
from model.node import Node
from model.search_instance import SearchInstance
from move_finder import MoveFinder
from controller.bloader import BLoader
from node_searcher import NodeSearcher
from view.console_v import ConsoleView


def execute_all_algorithms_and_heuristics(start_node: Node) -> list[SearchInstance]:
    #Execute search using each algorithm and each heuristic
    solutions: list[SearchInstance] = []
    solutions.append(NodeSearcher("UCS").execute_search(start_node))
    for h in range(1, 5):
        solutions.append(NodeSearcher("GBFS", h).execute_search(start_node))
        solutions.append(NodeSearcher("A/A*", h).execute_search(start_node))
    return solutions


class RushHourSolver(object):
    def __init__(self):
        self.console_view = ConsoleView()
        self.run()

    def run(self):
        # Ask user which game board load
        board_name = self.console_view.load_board_prompt()
        params_name = self.console_view.load_params_prompt()

        # Create directory to store output files if it does not already exist
        current_dir_path = os.getcwd()
        output_dir_path = os.path.join(current_dir_path, r'output_files')
        if not os.path.exists(output_dir_path):
            os.mkdir(output_dir_path)

        if board_name:
            # Load game board from file
            loader = BLoader('./datatxt/%s.txt' % board_name, './datatxt/%s.txt' % params_name)
            puzzle_no = 1
            game_board = loader.get_game_board()

            # Display game board
            self.console_view.display_loaded_grid(game_board.get_grid(), game_board.get_height(), game_board.get_width())

            # Find the solution to the game board
            start: Node = Node(gameboard=game_board)
            solution = NodeSearcher("UCS").execute_search(start)
            solution.puzzle_number = puzzle_no
            write_solution_to_solution_file(solution, output_dir_path)


            # solutions = execute_all_algorithms_and_heuristics(start)
            # for solution in solutions:
            #     solution.puzzle_number = self.puzzle_number
            # self.puzzle_number += 1

            # if solution:
            #     self.console_view.display_statistics(len(solution), end_time - start_time)
            # else:
            #     self.console_view.display_statistics(time_delta=end_time - start_time)
            #
            # self.console_view.display_solution(solution)

        # Exit system
        self.console_view.display_exit_message()
        sys.exit()


if __name__ == "__main__":
    RushHourSolver()

