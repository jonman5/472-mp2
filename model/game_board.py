from model.vehicle import Vehicle


class GameBoard(object):
    def __init__(self, height, width):
        self.grid = []
        self.height = height
        self.width = width
        self.generate_grid()
        self.vehicles = {}

    def generate_grid(self):
        for row in range(self.height):
            self.grid.append([])
            for column in range(self.width):
                self.grid[row].append('.')

    def get_grid(self):
        return self.grid

    def add_vehicle(self, vehicle):
        if self.vehicles.get(vehicle.name) is None:
            self.vehicles[vehicle.name] = vehicle
        for location in vehicle.get_occupied_locations():
            x = location['x']
            y = location['y']
            self.grid[x][y] = vehicle.name

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_spot_at(self, x, y):
        return self.grid[x][y]
