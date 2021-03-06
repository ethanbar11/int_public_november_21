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

    def bla(self):
        print(self.x)


class Rectangle:
    # upper_point and lower_point are of type Point
    def __init__(self, upper_point, lower_point):
        self.upper_point = upper_point
        self.lower_point = lower_point
        # self.width = width
        # self.height = height

    def get_area(self):
        width = self.upper_point.x - self.lower_point.x
        height = self.lower_point.y - self.upper_point.y
        return width * height


class Triangle:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def get_perimeter(self):
        distance1 = self.point1.get_distance_from_other_point(self.point2)
        distance2 = self.point2.get_distance_from_other_point(self.point3)
        distance3 = self.point3.get_distance_from_other_point(self.point1)
        return distance1 + distance2 + distance3


point1 = Point(4, 5)
point2 = Point(2, 9)
point3 = Point(10, 15)
# distance = point1.get_distance_from_other_point(point2)

# rectangle = Rectangle(point1, point2)
# print(rectangle.get_area())

triangle = Triangle(point1, point2, point3)
print(triangle.get_perimeter())
