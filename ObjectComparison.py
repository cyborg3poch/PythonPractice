# https://rszalski.github.io/magicmethods/
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


point = Point(1,3)
point_another = Point(1,3)
print(point == point_another)
