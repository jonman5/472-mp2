from directionorientation.orientation import Orientation


class Vehicle(object):

    def __init__(self, name, main_vehicle=False):
        self.name = name
        self.start_location = {}
        self.end_location = {}
        self.main_vehicle = main_vehicle
        self.occupied_locations = []
        self.fuel_level = 100
        self.orientation = None
        self.removed_by_valet = False

    def set_fuel_level(self, level):
        self.fuel_level = level

    def get_fuel_level(self):
        return self.fuel_level

    def set_start_location(self, x, y):
        """Set start location of the object."""
        self.start_location['x'] = x
        self.start_location['y'] = y

    def get_start_location(self):
        """Get start location of the object."""
        return self.start_location

    def set_end_location(self, x, y):
        """Set end location of the object."""
        self.end_location['x'] = x
        self.end_location['y'] = y
        self.__set_orientation()

    def get_end_location(self):
        """Get end location of the object."""
        return self.end_location

    def get_occupied_locations(self):
        """Get the locations that are being occupied by the objects."""
        occupied_locations = []

        if self.orientation == Orientation.HORIZONTAL:
            delta = self.end_location['x'] - self.start_location['x']
            for index in range(0, delta + 1):
                location = {'x': self.start_location['x'] + index, 'y': self.start_location['y']}
                occupied_locations.append(location)

        if self.orientation == Orientation.VERTICAL:
            delta = self.end_location['y'] - self.start_location['y']
            for index in range(0, delta + 1):
                location = {'x': self.start_location['x'], 'y': self.start_location['y'] + index}
                occupied_locations.append(location)

        self.occupied_locations = occupied_locations
        return occupied_locations

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def is_main_vehicle(self):
        return self.main_vehicle

    def __set_orientation(self):
        if self.start_location['y'] == self.end_location['y']:
            self.orientation = Orientation.HORIZONTAL

        if self.start_location['x'] == self.end_location['x']:
            self.orientation = Orientation.VERTICAL

    def get_orientation(self):
        return self.orientation

    def move_forward(self):
        if self.get_orientation() == Orientation.HORIZONTAL:
            self.start_location['x'] += 1
            self.end_location['x'] += 1

        if self.get_orientation() == Orientation.VERTICAL:
            self.start_location['y'] += 1
            self.end_location['y'] += 1

    def move_backward(self):
        if self.get_orientation() == Orientation.HORIZONTAL:
            self.start_location['x'] -= 1
            self.end_location['x'] -= 1

        if self.get_orientation() == Orientation.VERTICAL:
            self.start_location['y'] -= 1
            self.end_location['y'] -= 1

    def __repr__(self):
        return '%s - %s - %s' % (self.name, self.start_location, self.end_location)