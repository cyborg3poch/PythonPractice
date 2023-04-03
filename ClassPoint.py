class Point:
    # class attribute shared across all instance of class
    default_color = "red"

    # making constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # factory menthod to intantiate class's object with 0,0 values
    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point {self.y}, {self.x} , {self.z}")


point = Point(78, 89)
# Adding attributes on the go
point.z = 11
point.draw()

# this will change default color for all instance
Point.default_color = "blue"

# this will change default color for point instance
point.default_color = "yellow"

another_pt = Point(5, 8)
another_pt.z = 11
another_pt.draw()
# Prints blue
print(another_pt.default_color)

# initialising with factory method
zero_pt = Point.zero()
zero_pt.z = 0
zero_pt.draw()
