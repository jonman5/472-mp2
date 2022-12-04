from directionorientation.orientation import Orientation
from model.node import Node
from model.vehicle import Vehicle

# h1: The number of blocking vehicles.
# h2: The number of blocked positions.
# h3: The value of h1 multiplied by a constant λ of your choice, where λ > 1.
# h4: The number of blocking vehicles + number of vertical blocking vehicles that are blocked on both sides
h3_lambda = 2


def calculate_heuristic(heuristic_to_use, node: Node):
    calculated_heuristic = 0
    match heuristic_to_use:
        case 1:
            calculated_heuristic = __calculate_h1(node)
        case 2:
            calculated_heuristic = __calculate_h2(node)
        case 3:
            calculated_heuristic = __calculate_h3(node)
        case 4:
            calculated_heuristic = __calculate_h4(node)
    return calculated_heuristic


def __calculate_h1(node: Node):
    row_3: list = node.get_state().get_grid()[2]
    row_3_reversed = row_3.copy()
    row_3_reversed.reverse()
    end_of_A_reverse_index = row_3_reversed.index('A')
    blocking_vehicles_count = 0
    for i in range(1, end_of_A_reverse_index + 1):
        if i > 1 and row_3[-i] != '.':
            if row_3[-i] != row_3[-(i - 1)]:
                blocking_vehicles_count += 1
        elif row_3[-i] != '.':
            blocking_vehicles_count += 1
    return blocking_vehicles_count


def __calculate_h2(node: Node):
    row_3: list = node.get_state().get_grid()[2]
    row_3_reversed = row_3.copy()
    row_3_reversed.reverse()
    end_of_A_reverse_index = row_3_reversed.index('A')
    blocking_positions_count = 0
    for i in range(1, end_of_A_reverse_index + 1):
        if row_3[-i] != '.':
            blocking_positions_count += 1
    return blocking_positions_count


def __calculate_h3(node: Node):
    h2 = __calculate_h2(node)
    return h2 * h3_lambda


def __calculate_h4(node: Node):
    grid = node.get_state().get_grid()
    row_3: list = grid()[2]
    row_3_reversed = row_3.copy()
    row_3_reversed.reverse()
    end_of_A_reverse_index = row_3_reversed.index('A')
    blocking_vehicles: list[Vehicle] = []
    for i in range(1, end_of_A_reverse_index + 1):
        if i > 1 and row_3[-i] != '.':
            if row_3[-i] != row_3[-(i - 1)]:
                blocking_vehicles.append(node.state.vehicles[row_3[-i]])
        elif row_3[-i] != '.':
            blocking_vehicles.append(node.state.vehicles[row_3[-i]])

    count_blocking_vehicles_totally_blocked = 0
    for blocking_vehicle in blocking_vehicles:
        if blocking_vehicle.orientation == Orientation.VERTICAL:
            if blocking_vehicle.end_location['y'] > blocking_vehicle.start_location['y']:
                start_spot_to_check = {}
                start_spot_to_check['x'] = blocking_vehicle.start_location['x']
                start_spot_to_check['y'] = blocking_vehicle.start_location['y'] - 1
                end_spot_to_check = {}
                end_spot_to_check['x'] = blocking_vehicle.end_location['x']
                end_spot_to_check['y'] = blocking_vehicle.end_location['y'] + 1
                if not start_spot_to_check['y'] < 0:
                    if grid[start_spot_to_check['y']][start_spot_to_check['x']] == '.':
                        continue
                if not end_spot_to_check['y'] > 5:
                    if grid[end_spot_to_check['y']][end_spot_to_check['x']] == '.':
                        continue
            else:
                start_spot_to_check = {}
                start_spot_to_check['x'] = blocking_vehicle.start_location['x']
                start_spot_to_check['y'] = blocking_vehicle.start_location['y'] + 1
                end_spot_to_check = {}
                end_spot_to_check['x'] = blocking_vehicle.end_location['x']
                end_spot_to_check['y'] = blocking_vehicle.end_location['y'] - 1
                if not start_spot_to_check['y'] > 5:
                    if grid[start_spot_to_check['y']][start_spot_to_check['x']] == '.':
                        continue
                if not end_spot_to_check['y'] < 0:
                    if grid[end_spot_to_check['y']][end_spot_to_check['x']] == '.':
                        continue
        else:
            continue
            # if blocking_vehicle.end_location['x'] > blocking_vehicle.start_location['x']:
            #     start_spot_to_check = {}
            #     start_spot_to_check['x'] = blocking_vehicle.start_location['x'] - 1
            #     start_spot_to_check['y'] = blocking_vehicle.start_location['y']
            #     end_spot_to_check = {}
            #     end_spot_to_check['x'] = blocking_vehicle.end_location['x'] + 1
            #     end_spot_to_check['y'] = blocking_vehicle.end_location['y']
            #     if not start_spot_to_check['x'] < 0:
            #         if grid[start_spot_to_check['y']][start_spot_to_check['x']] == '.':
            #             continue
            #     if not end_spot_to_check['x'] > 5:
            #         if grid[end_spot_to_check['y']][end_spot_to_check['x']] == '.':
            #             continue
            # else:
            #     start_spot_to_check = {}
            #     start_spot_to_check['x'] = blocking_vehicle.start_location['x'] + 1
            #     start_spot_to_check['y'] = blocking_vehicle.start_location['y']
            #     end_spot_to_check = {}
            #     end_spot_to_check['x'] = blocking_vehicle.end_location['x'] - 1
            #     end_spot_to_check['y'] = blocking_vehicle.end_location['y']
            #     if not start_spot_to_check['x'] > 5:
            #         if grid[start_spot_to_check['y']][start_spot_to_check['x']] == '.':
            #             continue
            #     if not end_spot_to_check['x'] < 0:
            #         if grid[end_spot_to_check['y']][end_spot_to_check['x']] == '.':
            #             continue
        count_blocking_vehicles_totally_blocked += 1
    return count_blocking_vehicles_totally_blocked + len(blocking_vehicles)
