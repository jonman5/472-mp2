import string

from model.game_board import GameBoard
from model.node import Node
from model.vehicle import Vehicle


class Search(object):
    algorithm: string
    heuristic: string
    execution_time: int
    search_path: [Node]
    solution_path: list[Node]
    initial_state: GameBoard
    solved_state: GameBoard
    puzzle_number: int

    def __init__(self, algo, heuristic):
        self.filename = str()
        self.algorithm = algo
        self.heuristic = heuristic
        self.execution_time = 0
        self.search_path = []
        self.solution_path = []
        self.initial_state = None
        self.solved_state = None
        self.puzzle_number = 0
        self.set_file_name()

    def add_initial_configuration_to_solution_file(self):
        grid = self.initial_state.grid
        temp = str()

        # board config one line
        for row in grid:
            for column in row:
                temp += column

        with open(self.filename, 'w') as file:
            file.write(temp)

        # board config matrix form
        temp = str()
        for row in grid:
            temp += row + "\n"

        with open(self.filename, 'w') as file:
            file.write(temp)

        # one line each car fuel level
        vehicles = self.initial_state.vehicles.values()
        temp = str()
        for v in vehicles:
            temp += v.get_name() + ":" + v.get_fuel_level()
            if v:
                temp += ", "
        temp += "\n"

        with open(self.filename, 'w') as file:
            file.write(temp)

    def add_execution_time_to_solution_file(self, time):

        with open(self.filename, 'w') as file:
            file.write("Runtime: %s\n" % time)

    def add_length_of_search_path_to_solution_file(self):
        length = len(self.search_path)

        with open(self.filename, 'w') as file:
            file.write("Search path length: %s\n" % length)

    def add_length_of_solution_path_to_solution_file(self):
        length = len(self.solution_path)

        with open(self.filename, 'w') as file:
            file.write("Solution path length: %s\n" % length)

    def add_list_moves_in_solution_path_to_solution_file(self, some_list):
        move = None
        temp = str()
        temp = "Solution path: "
        for node in self.solution_path:
            move = node.get_move()
            temp += move.vehicle_name + " " + str(move.move_direction) + " " + str(move.get_count()) + "; "

        with open(self.filename, 'w') as file:
            file.write(temp)

    def add_one_move_to_solution_file(self):
        move = None
        temp = str()

        for node in self.solution_path:
            move = node.get_move()
            fuel_level = node.get_state().get_vehicles()[move.vehicle_name].get_fuel_level()
            grid = node.get_state().grid

            # vehicle name to move
            # direction to move
            temp += move.vehicle_name + " " + str(move.move_direction) + " "

            # number of positions to move
            # vehicle fuel after move
            temp += str(move.get_count()) + "\t" + str(fuel_level) + "  "

            # new configuration after the move one line
            for row in grid:
                for column in row:
                    temp += column
                    temp += "\n"

        with open(self.filename, 'w') as file:
            file.write(temp)

    def add_final_configuration_to_solution_file(self, source):
        grid = self.solved_state.grid
        temp = str()
        for row in grid:
            temp += row + "\n"

    def set_file_name(self):
        self.filename = self.algorithm + "-" + self.heuristic + "-" + "sol" + "-" + self.puzzle_number
