import string
from model.game_board import GameBoard
from model.vehicle import Vehicle


class BLoader(object):
    def __init__(self, game_filename):
        self.game_filename = game_filename
        self.game_boards = []
        self.content = self.read()
        self.parse()

    def read(self):
        try:
            with open(self.game_filename, 'r') as file:
                lines = file.read().splitlines()
                if len(lines) == 0:
                    print('The file is empty! Please select a file with a correct data format.')
                return lines
        except FileNotFoundError:
            print('File with board data not found! Please enter correct file location.')

    def parse(self):
        for line in self.content:
            self.parse_to_objects(line)

    def read_params(self, line):
        parameters = {}

        split_line = line.split(" ")
        for i in range(1, len(split_line)):
            vehicle_name = split_line[i][0]
            fuel_level = split_line[i][1]
            parameters[vehicle_name] = fuel_level
        return parameters


    def parse_to_objects(self, line):
        if self.validate(line):
            vehicles = {}
            split_line = line.split(" ")
            for row in range(6):
                for column in range(6):
                    letter = split_line[0][(row * 6) + column]
                    if letter != '.' and letter != 'A':
                        if letter not in vehicles:
                            vehicle = Vehicle(name=letter)
                            vehicle.set_start_location(column, row)
                            vehicles[letter] = vehicle
                        else:
                            vehicle = vehicles[letter]
                            vehicle.set_end_location(column, row)

                    if letter == 'A':
                        if letter not in vehicles:
                            vehicle = Vehicle(name=letter, main_vehicle=True)
                            vehicle.set_start_location(column, row)
                            vehicles[letter] = vehicle
                        else:
                            vehicle = vehicles[letter]
                            vehicle.set_end_location(column, row)

            # set fuel level
            params = self.read_params(line)
            if params is not None:
                for key, value in params.items():
                    vehicles[key].set_fuel_level(int(value))

            # Initialize gameboard with vehicles
            self.game_boards.append(GameBoard(vehicles))

    def get_game_boards(self):
        """Return the loaded game board."""
        return self.game_boards

    @staticmethod
    def validate(line: string):
        """Validate the line of the game board file."""
        if line is not None and line != "":
            split_line = line.split(" ")
            if ('#' not in split_line[0]) and (len(split_line[0]) > 35):
                ambulance_size = 0
                for char in split_line[0]:
                    if 'A' in char:
                        ambulance_size += 1
                if ambulance_size == 0:
                    print('The input format is not correct! The ambulance vehicle is not present.')
                    return False
                else:
                    return True
        return False



