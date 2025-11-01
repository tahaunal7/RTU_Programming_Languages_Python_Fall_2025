import math

def circle_area(radius):
    return math.pi * (radius ** 2)

if __name__ == "__main__":
    radius = float(input("Enter the radius: "))
    area = circle_area(radius)
    print(f"Area of the circle: {area:.2f}")

