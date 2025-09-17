#Write your code here
import math

class Vector:
    @staticmethod
    def add(v1, v2):
        """Returns Addition of Two Vectors"""
        return tuple(a + b for a, b in zip(v1, v2))

    @staticmethod
    def subtract(v1, v2):
        """Returns Subtraction of Two Vectors (v1 - v2)"""
        return tuple(a - b for a, b in zip(v1, v2))

    @staticmethod
    def dot_product(v1, v2):
        """Returns Dot Product of Two Vectors"""
        return sum(a * b for a, b in zip(v1, v2))

    @staticmethod
    def cross_product(v1, v2):
        """Returns Cross Product of Two 3D Vectors"""
        if len(v1) != 3 or len(v2) != 3:
            raise ValueError("Cross product is only defined for 3D vectors.")
        return (
            v1[1]*v2[2] - v1[2]*v2[1],
            v1[2]*v2[0] - v1[0]*v2[2],
            v1[0]*v2[1] - v1[1]*v2[0]
        )

    @staticmethod
    def magnitude(v):
        """Returns Magnitude of a Vector"""
        return math.sqrt(sum(a**2 for a in v))

    @staticmethod
    def unit_vector(v):
        """Returns Unit Vector in the Direction of v"""
        mag = Vector.magnitude(v)
        if mag == 0:
            raise ValueError("Zero vector does not have a unit vector.")
        return tuple(a/mag for a in v)

    @staticmethod
    def projection(v1, v2):
        """Returns Projection of v1 on v2"""
        dot = Vector.dot_product(v1, v2)
        mag_v2 = Vector.magnitude(v2)
        if mag_v2 == 0:
            raise ValueError("Cannot project onto a zero vector.")
        scale = dot / (mag_v2**2)
        return tuple(scale * a for a in v2)


if __name__ == '__main__':
    while True:
        print("----Vector Calculations----\n")
        print("Enter Choice to Proceed")
        print("1. Vector Addition")
        print("2. Vector Subtraction")
        print("3. Dot Product")
        print("4. Cross Product")
        print("5. Magnitude of a Vector")
        print("6. Unit Vector")
        print("7. Projection of v1 on v2")
        print("8. Back to Main Menu")

        choice = int(input("\nEnter Your choice: "))

        if choice == 1:
            v1 = tuple(map(float, input("Enter Vector 1 (comma separated): ").split(',')))
            v2 = tuple(map(float, input("Enter Vector 2 (comma separated): ").split(',')))
            print(f"Addition = {Vector.add(v1, v2)}\n")

        elif choice == 2:
            v1 = tuple(map(float, input("Enter Vector 1 (comma separated): ").split(',')))
            v2 = tuple(map(float, input("Enter Vector 2 (comma separated): ").split(',')))
            print(f"Subtraction = {Vector.subtract(v1, v2)}\n")

        elif choice == 3:
            v1 = tuple(map(float, input("Enter Vector 1 (comma separated): ").split(',')))
            v2 = tuple(map(float, input("Enter Vector 2 (comma separated): ").split(',')))
            print(f"Dot Product = {Vector.dot_product(v1, v2)}\n")

        elif choice == 4:
            v1 = tuple(map(float, input("Enter Vector 1 (comma separated, 3 values): ").split(',')))
            v2 = tuple(map(float, input("Enter Vector 2 (comma separated, 3 values): ").split(',')))
            try:
                print(f"Cross Product = {Vector.cross_product(v1, v2)}\n")
            except ValueError as e:
                print(f"Error: {e}\n")

        elif choice == 5:
            v = tuple(map(float, input("Enter Vector (comma separated): ").split(',')))
            print(f"Magnitude = {Vector.magnitude(v)}\n")

        elif choice == 6:
            v = tuple(map(float, input("Enter Vector (comma separated): ").split(',')))
            try:
                print(f"Unit Vector = {Vector.unit_vector(v)}\n")
            except ValueError as e:
                print(f"Error: {e}\n")

        elif choice == 7:
            v1 = tuple(map(float, input("Enter Vector 1 (comma separated): ").split(',')))
            v2 = tuple(map(float, input("Enter Vector 2 (comma separated): ").split(',')))
            try:
                print(f"Projection of v1 on v2 = {Vector.projection(v1, v2)}\n")
            except ValueError as e:
                print(f"Error: {e}\n")

        elif choice == 8:
            print("Thank You...\n")
            break

        else:
            print("Invalid Choice\n")
