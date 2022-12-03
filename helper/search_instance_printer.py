from model.search_instance import SearchInstance


def write_solution_to_solution_file(search_instance: SearchInstance):
    with open(create_file_name(search_instance), 'w') as solution_file:
        if search_instance.solved_state is None:
            solution_file.write("No solution found!")
            add_initial_configuration_to_solution_file(search_instance, solution_file)
            add_execution_time_to_solution_file(search_instance, solution_file)
            add_length_of_search_path_to_solution_file(search_instance, solution_file)
            return

        add_initial_configuration_to_solution_file(search_instance, solution_file)
        add_execution_time_to_solution_file(search_instance, solution_file)
        add_length_of_search_path_to_solution_file(search_instance, solution_file)
        add_length_of_solution_path_to_solution_file(search_instance, solution_file)
        add_list_moves_in_solution_path_to_solution_file(search_instance, solution_file)
        add_moves_to_solution_file(search_instance, solution_file)
        add_final_configuration_to_solution_file(search_instance, solution_file)

def add_initial_configuration_to_solution_file(search_instance: SearchInstance, solution_file):
    grid = search_instance.initial_state.grid
    temp = ""

    # board config one line
    for row in grid:
        for column in row:
            temp += column
    solution_file.write(temp)

    # board config matrix form
    temp = ""
    for row in grid:
        temp += row + "\n"
    solution_file.write(temp)

    # one line each car fuel level
    vehicles = search_instance.initial_state.vehicles.values()
    temp = "Car fuel available: "
    for v in vehicles:
        temp += v.get_name() + ":" + v.get_fuel_level()
        if v:
            temp += ", "
    temp += "\n"
    solution_file.write(temp)


def add_execution_time_to_solution_file(search_instance: SearchInstance, solution_file):
    solution_file.write("Runtime: %s\n" % search_instance)


def add_length_of_search_path_to_solution_file(search_instance: SearchInstance, solution_file):
    length = len(search_instance.search_path)

    solution_file.write("Search path length: %s\n" % search_instance.execution_time)


def add_length_of_solution_path_to_solution_file(search_instance, solution_file):
    length = len(search_instance.solution_path)
    solution_file.write("Solution path length: %s\n" % length)


def add_list_moves_in_solution_path_to_solution_file(search_instance, solution_file):
    temp = "Solution path: "
    for node in search_instance.solution_path:
        move = node.get_move()
        temp += move.vehicle_name + " " + str(move.move_direction) + " " + str(move.get_count()) + "; "
    solution_file.write(temp)


def add_moves_to_solution_file(search_instance, solution_file):
    for node in search_instance.solution_path:
        temp = ""
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
        solution_file.write(temp)


def add_final_configuration_to_solution_file(search_instance, solution_file):
    grid = search_instance.solved_state.grid
    temp = ""
    for row in grid:
        temp += row + "\n"
    solution_file.write(temp)


def create_file_name(search_instance: SearchInstance):
    return search_instance.algorithm + "-" + search_instance.heuristic + "-" + "sol" + "-" + search_instance.puzzle_number
