from model.node import Node

# h1: The number of blocking vehicles.
# h2: The number of blocked positions.
# h3: The value of h1 multiplied by a constant λ of your choice, where λ > 1.
# h4: The number of blocking vehicles + number of vertical blocking vehicles that are blocked on both sides
h3_lambda = 2


def calculate_heuristic(heuristic_to_use, node: Node):
    match heuristic_to_use:
        case 'h1':
            h1 = __calculate_h1(node)
            node.set_heuristic(h1)
        case 'h2':
            h2 = __calculate_h2(node)
            node.set_heuristic(h2)
        case 'h3':
            h3 = __calculate_h3(node)
            node.set_heuristic(h3)
        case 'h4':
            pass
    return 0


def __calculate_h1(node: Node):
    row_3: list = Node.get_state().get_grid()[2]
    row_3_reversed = row_3.copy().reverse()
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
    row_3: list = Node.get_state().get_grid()[2]
    row_3_reversed = row_3.copy().reverse()
    end_of_A_reverse_index = row_3_reversed.index('A')
    return end_of_A_reverse_index


def __calculate_h3(node: Node):
    h2 = __calculate_h2(node)
    return h2*h3_lambda
