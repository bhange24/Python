class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
            return 0.5 * (self.base + self.height)


obj = Triangle(125, 50)


print("Area of triangle is:", (obj.get_area()))

