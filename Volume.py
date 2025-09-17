#Write your code here
from math import pi,pow;

class Volume:
    @staticmethod
    def sphere(radius):
        """Returns Volume of Sphere"""
        return (4 * pi * pow(radius,3))/3


    @staticmethod
    def cylinder(radius,height):
        """Returns Volume of Cylinder"""
        return pi*(radius * radius )*height

    @staticmethod
    def cone(radius,height):
        """Returns Volume of Cone"""
        return pi*(radius * radius )*height/3

    @staticmethod
    def cube(a):
        """Returns Volume of Cube"""
        return a**3

    @staticmethod
    def cuboid(length,breadth,height):
        """Returns Volume of Cuboid"""
        return length*breadth*height
    
    @staticmethod
    def hemisphere(radius):
        """Returns Volume of Hemisphere"""
        return (2/3)*(22/7)*(radius**3)
    

if __name__ == '__main__':
    while True:
        print("----Volume Calculations----\n")
        print("Enter Choice to Proceed")
        print("1. Volume of Sphere")
        print("2. Volume of Cylinder")
        print("3. Volume of Cone")
        print("4. Volume of Cube")
        print("5. Volume of Cuboid")
        print("6. Volume of Hemisphere")
        print("7. Back to Main Menu");
        
        choice = int(input("\nEnter Your choice: "))

        if(choice == 1):
            radius = float(input("\nEnter the radius: "))
            print(f"Volume of Sphere of radius({radius}) = {Volume.sphere(radius)}\n")

        elif(choice == 2):
            radius = float(input("\nEnter the radius: "))
            height = float(input("Enter the height: "))
            print(f"Volume of Cylinder of radius({radius}) and height({height}) = {Volume.cylinder(radius,height)}\n")

        elif(choice == 3):
            radius = float(input("\nEnter the radius: "))
            height = float(input("Enter the height: "))
            print(f"Volume of Cone of radius({radius}) and height({height}) = {Volume.cone(radius,height)}\n")

        elif(choice == 4):
            side = float(input("\nEnter Length of the side:"))
            print(f"Volume of Cube of side({side}) = {Volume.cube(side)}\n")

        elif(choice == 5):
            length = float(input("\nEnter the length: "))
            breadth = float(input("\nEnter the breadth: "))
            height = float(input("Enter the height: "))
            print(f"Volume of Cuboid of length({length}), breadth({breadth}) and height({height}) = {Volume.cuboid(length,breadth,height)}\n")

        elif(choice == 6):
            radius = float(input("\nEnter the radius: "))
            print(f"Volume of Hemisphere of radius({radius}) = {Volume.hemisphere(radius)}\n")

        elif(choice == 7):
            print("Thank You...\n")
            break;
        else:
            print("Invalid Choice\n")
