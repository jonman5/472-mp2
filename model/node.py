from vehicle_mover import *


class Node(object):
    def __init__(self, move=None, parent_node=None, *, gameboard=None):
        if gameboard is not None:
            self.state = gameboard
            self.move = None
            self.parent_node = None
            self.depth = 0
            self.heuristic = 0
            self.is_goal = self.__check_is_goal()
            return
        self.state = move_vehicle_on_board(parent_node.get_state(), move)
        self.move_step_count = move.get_count()
        self.parent_node = parent_node
        self.depth = parent_node.get_depth() + 1
        self.heuristic = 0
        self.is_goal = self.__check_is_goal()

    def get_state(self):
        return self.state

    def get_move(self):
        return self.move

    def get_step_count(self):
        return self.path_cost

    def get_depth(self):
        return self.depth

    def get_heuristic(self):
        return self.heuristic

    def get_is_goal(self):
        return self.is_goal

    def set_heuristic(self, heuristic):
        self.heuristic = heuristic

    def __check_is_goal(self):
        A_locations = self.state.get_vehicles()['A'].get_occupied_locations()
        for location in A_locations:
            if location['x'] == 5 and location['y'] == 2:
                return True
        return False

    def set_depth(self, depth):
        self.depth = depth
