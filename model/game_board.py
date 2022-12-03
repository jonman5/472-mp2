from directionorientation.orientation import Orientation
from model.vehicle import Vehicle


class GameBoard(object):
    vehicles: dict[str, Vehicle]

    def __init__(self, vehicles: {}):
        self.grid = []
        self.height = 6
        self.width = 6
        self.vehicles = vehicles
        self.generate_grid()
        self.__call_valet_service()


    def generate_grid(self):
        self.grid = []
        for row in range(self.height):
            self.grid.append([])
            for column in range(self.width):
                self.grid[row].append('.')
        for vehicle in self.vehicles.values():
            if not vehicle.removed_by_valet:
                self.add_vehicle(vehicle)

    def get_grid(self):
        return self.grid

    def add_vehicle(self, vehicle):
        if self.vehicles.get(vehicle.name) is None:
            self.vehicles[vehicle.name] = vehicle
        for location in vehicle.get_occupied_locations():
            x = location['x']
            y = location['y']
            self.grid[y][x] = vehicle.name

    def get_vehicles(self):
        return self.vehicles

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_spot_at(self, x, y):
        return self.grid[y][x]

    def __call_valet_service(self):
        if not self.grid[2][5] == ".":
            vehicle_name = self.grid[2][5]
            if self.vehicles[vehicle_name].orientation == Orientation.HORIZONTAL and (not vehicle_name == 'A'):
                self.vehicles[vehicle_name].removed_by_valet = True
                self.vehicles[vehicle_name].start_location['x'] = 0
                self.vehicles[vehicle_name].start_location['y'] = 0
                self.vehicles[vehicle_name].end_location['x'] = 0
                self.vehicles[vehicle_name].end_location['y'] = 0
                self.generate_grid()


    def __eq__(self, other):
        return self.grid == other.grid
