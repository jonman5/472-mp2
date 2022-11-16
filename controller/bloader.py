import re
from model.game_board import GameBoard
from model.vehicle import Vehicle


class BLoader(object):
    def __init__(self, game_filename, params_filename):
        self.game_filename = game_filename
        self.params_filename = params_filename
        self.game_board = None
        content = self.read()
        params = self.read_params(params_filename)
        self.validate(content)
        self.parse_to_objects(content, params)

    def read(self):
        try:
            with open(self.game_filename, 'r') as file:
                return file.read().splitlines()
        except FileNotFoundError:
            print('File with board data not found! Please enter correct file location.')

    def read_params(self, params_filename):
        parameters = {}
        try:
            with open(self.params_filename, 'r') as file:
                ps = file.readline().split(" ")
                if ps[0] == "" or ps[0] == "\n":
                    return None
                for p in ps:
                    letter = p[0]
                    fuel_level = p[1]
                    parameters[letter] = fuel_level
            return parameters
        except FileNotFoundError:
            print('File with parameters data not found! Please enter correct file location.')

    def parse_to_objects(self, content, params):
        vehicles = {}
        # BBBJCCH..J.KHAAJ.K..IDDLEEI..L....GG
        for row in range(6):
            for column in range(6):
                letter = content[0][(row*6)+column]
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
        if params is not None:
            for key, value in params.items():
                vehicles[key].set_fuel_level(value)

        board_width = 6
        board_height = 6
        self.game_board = GameBoard(board_height, board_width)

        for key, vehicle in sorted(vehicles.items()):
            self.game_board.add_vehicle(vehicle)

    def get_game_board(self):
        """Return the loaded game board."""
        return self.game_board

    @staticmethod
    def validate(content):
        """Validate the content of the game board file."""
        try:
            if len(content) == 0:
                raise ValueError('The file is empty! Please select a file with a correct data format.')

            line_length = len(content[0])
            red_car_size = 0
            for line in content:
                if line_length != len(line):
                    raise ValueError('The data format is not correct! All the text lines need to be the same length.')

                if re.sub(r'[A-Za-z.]+', '', line):
                    raise ValueError('The data format is not correct! Only letters and "." are allowed.')

                if 'A' in line:
                    red_car_size += 1

            if red_car_size == 0:
                raise ValueError('The data format is not correct! The red car is not set.')

        except ValueError as expression:
            print(expression)

