import math


# area = pi * r^2

radius = float(input("Enter the radius of the circle: "))
area = math.pi * math.pow(radius, 2)
print(f"The area of the circle is: {round(area, 2)} cm²")