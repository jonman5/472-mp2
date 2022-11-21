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
        for row_index, row in enumerate(current_grid):
            for col, spot in enumerate(row):
                if spot == '.':
                    if row_index != 0:
                        move_down = cls.__test_move_down(gameboard, col, row_index)
                        if move_down is not None:
                            vehicle_fuel_level = gameboard.get_vehicles()[move_down.get_vehicle_name()].get_fuel_level()
                            if vehicle_fuel_level - move_down.get_count() >= 0:
                                moves.append(move_down)
                    if row_index != 5:
                        move_up = cls.__test_move_up(gameboard, col, row_index)
                        if move_up is not None:
                            vehicle_fuel_level = gameboard.get_vehicles()[move_up.get_vehicle_name()].get_fuel_level()
                            if vehicle_fuel_level - move_up.get_count() >= 0:
                                moves.append(move_up)
                    if col != 0:
                        move_right = cls.__test_move_right(gameboard, col, row_index)
                        if move_right is not None:
                            vehicle_fuel_level = gameboard.get_vehicles()[move_right.get_vehicle_name()].get_fuel_level()
                            if vehicle_fuel_level - move_right.get_count() >= 0:
                                moves.append(move_right)
                    if col != 5:
                        move_left = cls.__test_move_left(gameboard, col, row_index)
                        if move_left is not None:
                            vehicle_fuel_level = gameboard.get_vehicles()[move_left.get_vehicle_name()].get_fuel_level()
                            if vehicle_fuel_level - move_left.get_count() >= 0:
                                moves.append(move_left)
        return moves

    @classmethod
    # Check if the vehicle above spot(x, y) can move down, if so return that move
    def __test_move_down(cls, gameboard: GameBoard, x, y):
        # Find adjacent vehicle above spot of interest and return Move which moves it down to spot of interest
        spot_above = gameboard.get_spot_at(x, y - 1)
        if spot_above.isalpha():
            vehicle_above: Vehicle = gameboard.vehicles.get(spot_above)
            if vehicle_above.get_orientation() == Orientation.VERTICAL and vehicle_above.fuel_level > 0:
                heuristic = 1
                return Move(vehicle_above.name, Direction.DOWN, 1, heuristic)
            else:
                return None
        # If adjacent spot above is not a vehicle:
        # Find the closest vehicle above spot of interest and return Move which moves it down to spot of interest
        free_spots_above = 0
        while spot_above == '.' and (y - free_spots_above - 2) >= 0:
            free_spots_above += 1
            spot_above = gameboard.get_spot_at(x, y - free_spots_above - 1)
        if spot_above.isalpha():
            vehicle_above: Vehicle = gameboard.vehicles.get(spot_above)
            if vehicle_above.get_orientation() == Orientation.VERTICAL and vehicle_above.fuel_level > free_spots_above:
                heuristic = 1
                return Move(vehicle_above.name, Direction.DOWN, free_spots_above + 1, heuristic)

    @classmethod
    # Check if the vehicle below spot(x, y) can move up, if so return that move
    def __test_move_up(cls, gameboard: GameBoard, x, y):
        # Find adjacent vehicle below spot of interest and return Move which moves it up to spot of interest
        spot_below = gameboard.get_spot_at(x, y + 1)
        if spot_below.isalpha():
            vehicle_below: Vehicle = gameboard.vehicles.get(spot_below)
            if vehicle_below.get_orientation() == Orientation.VERTICAL and vehicle_below.fuel_level > 0:
                heuristic = 1
                return Move(vehicle_below.name, Direction.UP, 1, heuristic)
            else:
                return None

        # If adjacent spot below is not a vehicle:
        # Find the closest vehicle below spot of interest and return Move which moves it up to spot of interest
        free_spots_below = 0
        while spot_below == '.' and (y + free_spots_below + 2) < 6:
            free_spots_below += 1
            spot_below = gameboard.get_spot_at(x, y + free_spots_below + 1)
        if spot_below.isalpha():
            vehicle_below: Vehicle = gameboard.vehicles.get(spot_below)
            if vehicle_below.get_orientation() == Orientation.VERTICAL and vehicle_below.fuel_level > free_spots_below:
                heuristic = 1
                return Move(vehicle_below.name, Direction.UP, free_spots_below+1, heuristic)

    @classmethod
    # Check if the adjacent vehicle left of spot(x, y) can move right, if so return that move
    def __test_move_right(cls, gameboard: GameBoard, x, y):
        # Find adjacent vehicle left of spot of interest and return Move which moves it right to spot of interest
        spot_above = gameboard.get_spot_at(x - 1, y)
        if spot_above.isalpha():
            vehicle_above: Vehicle = gameboard.vehicles.get(spot_above)
            if vehicle_above.get_orientation() == Orientation.HORIZONTAL and vehicle_above.fuel_level > 0:
                heuristic = 1
                return Move(vehicle_above.name, Direction.RIGHT, 1, heuristic)
            else:
                return None
        # If adjacent spot to left is not a vehicle:
        # Find the closest vehicle left of spot of interest and return Move which moves it right to spot of interest
        free_spots_to_left = 0
        while spot_above == '.' and (x - free_spots_to_left - 2) >= 0:
            free_spots_to_left += 1
            spot_above = gameboard.get_spot_at(x - free_spots_to_left - 1, y)
        if spot_above.isalpha():
            vehicle_above: Vehicle = gameboard.vehicles.get(spot_above)
            if vehicle_above.get_orientation() == Orientation.HORIZONTAL and vehicle_above.fuel_level > free_spots_to_left:
                heuristic = 1
                return Move(vehicle_above.name, Direction.RIGHT, free_spots_to_left + 1, heuristic)

    @classmethod
    # Check if the adjacent vehicle right of spot(x, y) can move left, if so return that move
    def __test_move_left(cls, gameboard: GameBoard, x, y):
        # Find adjacent vehicle right of spot of interest and return Move which moves it left to spot of interest
        spot_below = gameboard.get_spot_at(x + 1, y)
        if spot_below.isalpha():
            vehicle_below: Vehicle = gameboard.vehicles.get(spot_below)
            if vehicle_below.get_orientation() == Orientation.HORIZONTAL and vehicle_below.fuel_level > 0:
                heuristic = 1
                return Move(vehicle_below.name, Direction.LEFT, 1, heuristic)
            else:
                return None

        # If spot to right is not a vehicle:
        # Find the closest vehicle right of spot of interest and return Move which moves it left to spot of interest
        free_spots_to_right = 0
        while spot_below == '.' and (x + free_spots_to_right + 2) < 6:
            free_spots_to_right += 1
            spot_below = gameboard.get_spot_at(x + free_spots_to_right + 1, y)
        if spot_below.isalpha():
            vehicle_below: Vehicle = gameboard.vehicles.get(spot_below)
            if vehicle_below.get_orientation() == Orientation.HORIZONTAL and vehicle_below.fuel_level > free_spots_to_right:
                heuristic = 1
                return Move(vehicle_below.name, Direction.LEFT, free_spots_to_right+1, heuristic)
