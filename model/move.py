from directionorientation.direction import Direction


class Move(object):
    def __init__(self, vehicle_name, direction, count, heuristic):
        self.vehicle_name = vehicle_name
        self.move_direction = direction
        self.count = count
        self.heuristic = heuristic

    def get_vehicle_name(self):
        return self.vehicle_name

    def get_move_direction(self):
        return self.move_direction

    def get_count(self):
        return self.count

    def get_heuristic(self):
        return self.heuristic
