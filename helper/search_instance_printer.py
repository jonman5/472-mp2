import os
from model.node import Node
from model.search_instance import SearchInstance


def write_solution_to_solution_file(search_instance: SearchInstance, output_path):
    output_file_path = os.path.join(output_path, create_file_name(search_instance, "sol"))
    with open(output_file_path, 'w') as solution_file:
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
        solution_file.close()


def write_search_to_search_file(search_instance: SearchInstance, output_path):
    output_file_path = os.path.join(output_path, create_file_name(search_instance, "search"))
    with open(output_file_path, 'w') as search_file:
        for searched_node in search_instance.search_path:
            line = "0 "
            if search_instance.algorithm == "A_Astar":
                line = str(searched_node.get_depth() + searched_node.heuristic) + " "
            line += str(searched_node.get_depth())
            if search_instance.algorithm == "UCS":
                line += "0  "
            else:
                line += str(searched_node.heuristic) + "  "
            for row in searched_node.state.grid:
                for column in row:
                    line += column
            line += "\n"
            search_file.write(line)
        search_file.close()



def add_initial_configuration_to_solution_file(search_instance: SearchInstance, solution_file):
    grid = search_instance.initial_state.grid
    temp = "Initial board configuration: "

    # board config one line
    for row in grid:
        for column in row:
            temp += column
    temp += "\n\n"
    solution_file.write(temp)

    # board config matrix form
    temp = ""
    for row in grid:
        string_row = "".join(row)
        temp += string_row + "\n"
    temp += "\n"
    solution_file.write(temp)

    # one line each car fuel level
    vehicles = search_instance.initial_state.vehicles.values()
    temp = "Car fuel available: "
    for v in vehicles:
        temp += v.get_name() + ":" + str(v.get_fuel_level())
        if v:
            temp += ", "
    temp += "\n\n"
    solution_file.write(temp)


def add_execution_time_to_solution_file(search_instance: SearchInstance, solution_file):
    solution_file.write("Runtime: %s\n" % search_instance.execution_time)


def add_length_of_search_path_to_solution_file(search_instance: SearchInstance, solution_file):
    length = len(search_instance.search_path)
    solution_file.write("Search path length: %s\n" % length)


def add_length_of_solution_path_to_solution_file(search_instance, solution_file):
    length = len(search_instance.solution_path)
    solution_file.write("Solution path length: %s\n" % length)


def add_list_moves_in_solution_path_to_solution_file(search_instance, solution_file):
    temp = "Solution path: "
    for node in search_instance.solution_path:
        if node.get_move() is not None:
            move = node.get_move()
            temp += move.vehicle_name + " " + move.move_direction.value.lower() + " " + str(move.get_count()) + "; "
    temp += "\n\n"
    solution_file.write(temp)


def add_moves_to_solution_file(search_instance, solution_file):
    temp = ""
    for node in search_instance.solution_path:
        if node.get_move() is not None:
            move = node.get_move()
            fuel_level = node.get_state().get_vehicles()[move.vehicle_name].get_fuel_level()
            grid = node.get_state().grid

            # vehicle name to move
            # direction to move
            temp += move.vehicle_name + " " + move.move_direction.value.lower() + " "

            # number of positions to move
            # vehicle fuel after move
            temp += str(move.get_count()) + "\t\t" + str(fuel_level) + " "

            # new configuration after the move one line
            for row in grid:
                for column in row:
                    temp += column
            temp += "\n"
    temp += "\n"
    solution_file.write(temp)


def add_final_configuration_to_solution_file(search_instance, solution_file):
    grid = search_instance.solved_state.grid
    temp = "Final board configuration:\n"
    for row in grid:
        string_row = "".join(row)
        temp += string_row + "\n"
    solution_file.write(temp)


def create_file_name(search_instance: SearchInstance, filetype):
    return search_instance.algorithm + "-h" + str(search_instance.heuristic) + "-" + filetype + "-" + str(
        search_instance.puzzle_number)
