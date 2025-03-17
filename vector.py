import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return round(math.sqrt(self.x ** 2 + self.y ** 2))

    def __getitem__(self, index):
        return (self.x, self.y)[index]



v1 = Vector(2, 4)
v2 = Vector(3, 1)

print(v1)           # Output: Vector(2, 4)
print(v1 + v2)      # Output: Vector(5, 5)
print(v1 - v2)      # Output: Vector(-1, 3)
print(v1 * 3)       # Output: Vector(6, 12)
print(v1 == Vector(2, 4))  # Output: True
print(len(v1))      # Output: 4 (rounded of root 17)
print(v1[0])        # Output: 2
print(v1[1])        # Output: 4
