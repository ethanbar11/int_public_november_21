import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # other_point is variable of type ***Point***
    def get_distance_from_other_point(self, other_point):
        distance_in_x = (self.x - other_point.x) ** 2
        distance_in_y = (self.y - other_point.y) ** 2

        # Math.sqrt = שורש
        return math.sqrt(distance_in_x + distance_in_y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return '({},{})'.format(self.x, self.y)

    def add(self, other):
        return Point(self.x + other.x, self.y + other.y)


# point1 = Point(1, 1)
# point2 = Point(2, 2)
# point3 = point1 + point2
# point3 = point1.add(point2) # This is the same as last row, only with uglier syntax
# x = 3 + 5
# print('The new point position is :', point3)


p1 = Point(1, 1)
p2 = Point(1, 1)
print(type(p1))
if p1 == p2:
    print('They are the same!')
else:
    print('NO NO NO!')
