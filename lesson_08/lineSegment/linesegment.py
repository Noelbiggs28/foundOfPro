class Point:
    def __init__(self, x_coord, y_coord):
        self._x_coord = x_coord
        self._y_coord = y_coord
    
    def get_x_coord(self):
        return self._x_coord
    
    def get_y_coord(self):
        return self._y_coord
    
    def distance_to(self, point_object):
        x1 = self._x_coord
        y1 = self._y_coord
        x2 = point_object.get_x_coord()
        y2 = point_object.get_y_coord()
        distance = (((x2-x1)**2) + ((y2-y1)**2))**0.5
        return distance

class LineSegment:
    def __init__(self, endpoint_1, endpoint_2):
        self._endpoint_1 = endpoint_1
        self._endpoint_2 = endpoint_2

    def get_endpoint_1(self):
        return self._endpoint_1
        # member1 = (self._endpoint_1.get_x_coord(),self._endpoint_1.get_y_coord())
        # return member1

    def get_endpoint_2(self):
        return self._endpoint_2
        # member2 = (self._endpoint_2.get_x_coord(),self._endpoint_2.get_y_coord())
        # return member2

    def length(self):
        return self._endpoint_1.distance_to(self._endpoint_2)
    
    def slope(self):
        # slope formula: y2-y1/x2-x1
        x1 = self._endpoint_1.get_x_coord()
        x2 = self._endpoint_2.get_x_coord()
        y1 = self._endpoint_1.get_y_coord()
        y2 = self._endpoint_2.get_y_coord()
        slope= (y2-y1)/(x2-x1)
        return slope

    def is_parallel_to(self, to_line):
        return self.slope()==to_line.slope()


# these go in linesegment
point_1 = Point(7,4)
point_2 = Point(-6,18)
line = LineSegment(point_1,point_2)

point_3 = Point(-2,2)
point_4 = Point(24, 12)
line2 = LineSegment(point_3, point_4)

point_5 = Point (9,6)
point_6 = Point(-4,20)
line3 = LineSegment(point_5, point_6)
print(point_1.distance_to(point_2))
print(line.length())
print(line.slope())
print(line.is_parallel_to(line2))
print(line.is_parallel_to(line3))