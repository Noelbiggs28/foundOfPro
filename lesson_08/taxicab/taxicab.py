class Taxicab:
    '''FIRST CLASS EVER'''
    def __init__(self, x_coord, y_coord,):
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._odometer_reading = 0

    def get_x_coord(self):
        return self._x_coord

    def get_y_coord(self):
        return self._y_coord

    def get_odometer_reading(self):
        return self._odometer_reading
    
    def move_x(self, distance):
        self._x_coord += distance
        self._odometer_reading += abs(distance)

    def move_y(self, distance):
        self._y_coord += distance
        self._odometer_reading += abs(distance)

cab = Taxicab(5,-8)
cab.move_x(3)
cab.move_y(-4)
cab.move_x(-1)

print(cab.get_x_coord())
print(cab.get_y_coord())
print(cab.get_odometer_reading())