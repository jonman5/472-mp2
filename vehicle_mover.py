import copy
from model.game_board import GameBoard
from model.move import Move
from model.vehicle import Vehicle


def move_vehicle_on_board(gameboard: GameBoard, move: Move):
    vehicles = copy.deepcopy(gameboard.get_vehicles())
    vehicle_to_move: Vehicle = vehicles[move.get_vehicle_name()]
    moved_vehicle = __move_vehicle(vehicle_to_move, move)
    vehicles[moved_vehicle.get_name()] = moved_vehicle
    updated_gameboard = GameBoard(vehicles)
    return updated_gameboard


def __move_vehicle(vehicle: Vehicle, move: Move):
    start_location = vehicle.get_start_location()
    end_location = vehicle.get_end_location()
    count = move.get_count()
    match move.get_move_direction().name:
        case 'UP':
            start_location['y'] -= count
            end_location['y'] -= count
        case 'DOWN':
            start_location['y'] += count
            end_location['y'] += count
        case 'RIGHT':
            start_location['x'] += count
            end_location['x'] += count
        case 'LEFT':
            start_location['x'] -= count
            end_location['x'] -= count

    vehicle.set_fuel_level(vehicle.get_fuel_level() - count)
    return vehicle
