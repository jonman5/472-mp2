from model.game_board import GameBoard
from model.vehicle import Vehicle
from model.move import Move
from directionorientation.direction import Direction
from directionorientation.orientation import Orientation


class MoveFinder(object):
    @classmethod
    # Find and return all possible moves
    def find_moves(cls, gameboard: GameBoard):
        moves = []
        current_grid = gameboard.get_grid()
        for row in current_grid:
            for col, spot in enumerate(row):
                if spot == '.':
                    if row != 0:
                        move_down = cls.__test_move_down(gameboard, row, col)
                        if move_down is not None:
                            moves.append(move_down)
                    if row != 5:
                        move_up = cls.__test_move_up(gameboard, row, col)
                        if move_up is not None:
                            moves.append(move_up)
                    # if col != 0:
                    #     move_right = cls.__test_move_right(gameboard, row, col)
                    #     if move_right is not None:
                    #         moves.append(move_right)
                    # if col != 5:
                    #     move_left = cls.__test_move_left(gameboard, col)
                    #     if move_left is not None:
                    #         moves.append(move_left)

    @classmethod
    # Check if the vehicle above spot(x, y) can move down, if so return that move
    def __test_move_down(cls, gameboard: GameBoard, x, y):
        # Find vehicle directly above spot of interest and return Move which moves it down to spot of interest
        spot_above = gameboard.get_spot_at(x - 1, y)
        if spot_above.isalpha():
            vehicle_above: Vehicle = gameboard.vehicles.get(spot_above)
            if vehicle_above.get_orientation() == Orientation.VERTICAL and vehicle_above.fuel_level > 0:
                heuristic = 1
                return Move(vehicle_above.name, Direction.DOWN, 1, heuristic)
            else:
                return None
        # If spot above is not a vehicle:
        # Find the closest vehicle above spot of interest and return Move which moves it down to spot of interest
        free_spots_above = 0
        while spot_above == '.' and (x - free_spots_above - 2) < 6:
            free_spots_above += 1
            spot_above = gameboard.get_spot_at(x - free_spots_above - 1, y)
        if spot_above.isalpha():
            vehicle_above: Vehicle = gameboard.vehicles.get(spot_above)
            if vehicle_above.get_orientation() == Orientation.VERTICAL and vehicle_above.fuel_level > free_spots_above:
                heuristic = 1
                return Move(vehicle_above.name, Direction.DOWN, free_spots_above + 1, heuristic)

    @classmethod
    # Check if the vehicle below spot(x, y) can move up, if so return that move
    def __test_move_up(cls, gameboard: GameBoard, x, y):
        # Find vehicle directly below spot of interest and return Move which moves it up to spot of interest
        spot_below = gameboard.get_spot_at(x + 1, y)
        if spot_below.isalpha():
            vehicle_below: Vehicle = gameboard.vehicles.get(spot_below)
            if vehicle_below.get_orientation() == Orientation.VERTICAL and vehicle_below.fuel_level > 0:
                heuristic = 1
                return Move(vehicle_below.name, Direction.UP, 1, heuristic)
            else:
                return None

        # If spot below is not a vehicle:
        # Find the closest vehicle below spot of interest and return Move which moves it up to spot of interest
        free_spots_below = 0
        while spot_below == '.' and (x + free_spots_below + 2) < 6:
            free_spots_below += 1
            spot_below = gameboard.get_spot_at(x + free_spots_below + 1, y)
        if spot_below.isalpha():
            vehicle_below: Vehicle = gameboard.vehicles.get(spot_below)
            if vehicle_below.get_orientation() == Orientation.VERTICAL and vehicle_below.fuel_level > free_spots_below:
                heuristic = 1
                return Move(vehicle_below.name, Direction.UP, free_spots_below+1, heuristic)
