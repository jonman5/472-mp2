import string

from model.game_board import GameBoard
from model.node import Node


class Search(object):
    algorithm: string
    heuristic: string
    execution_time: int
    search_path: [Node]
    solution_path: list[Node]
    initial_state: GameBoard
    solved_state: GameBoard

    def __init__(self, algo, heuristic):
        self.algorithm = algo
        self.heuristic = heuristic
        self.execution_time = 0
        self.search_path = []
        self.solution_path = []
        self.initial_state = None
        self.solved_state = None

    def add_initial_configuration_to_solution_file(source, filename):
        # one line read from file
        # board config matrix form
        # one line each car fuel level
        pass

    def add_execution_time_to_solution_file(time, filename):
        with open(filename, 'w') as file:
            file.write("Runtime: %s\n" % time)

    def add_length_of_search_path_to_solution_file(length, filename):
        with open(filename, 'w') as file:
            file.write("Search path length: %s\n" % length)

    def add_length_of_solution_path_to_solution_file(length, filename):
        with open(filename, 'w') as file:
            file.write("Solution path length %s\n" % length)

    def add_list_moves_in_solution_path_to_solution_file(some_list, filename):
        with open(filename, 'w') as file:
            for move in some_list:
                file.write(move)

    def add_one_move_to_solution_file(self, list_moves, filename):
        # vehicle name to move
        # direction to move
        # number of positions to move
        # vehicle fuel after move
        # new configuration after the move
        with open(filename, 'w') as file:
            file.write()

    def add_final_configuration_to_solution_file(source, filename):
        pass

