class Grid:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle_to_remove):
        for vehicle in self.vehicles:
            if vehicle == vehicle_to_remove:
                self.vehicles.pop()

    def create_grid(self, line):
        row = []
        for i in range(6):
            row[i] = line[:6]
            



