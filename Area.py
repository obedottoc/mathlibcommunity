import math

class AreaCalculator:
    def rectangle(self, length, width):
        """Return the area of a rectangle."""
        return length * width

    def square(self, side):
        """Return the area of a square."""
        return side * side

    def circle(self, radius):
        """Return the area of a circle."""
        return math.pi * radius * radius

    def cylinder(self, radius, height):
        """Return the surface area of a cylinder (2πr(r + h))."""
        return 2 * math.pi * radius * (radius + height)


if __name__ == "__main__":
    calc = AreaCalculator()
    print("Rectangle area:", calc.rectangle(5, 10))
    print("Square area:", calc.square(6))
    print("Circle area:", calc.circle(7))
    print("Cylinder surface area:", calc.cylinder(3, 8))
