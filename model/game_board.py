from model.vehicle import Vehicle


class GameBoard(object):
    def __init__(self, vehicles: {}):
        self.grid = []
        self.height = 6
        self.width = 6
        self.vehicles = vehicles
        self.generate_grid()

    def generate_grid(self):
        for row in range(self.height):
            self.grid.append([])
            for column in range(self.width):
                self.grid[row].append('.')
        for vehicle in self.vehicles.values():
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

    def __eq__(self, other):
        return self.grid == other.grid
