import math

# hypothenuse = √(a² + b²)

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))

c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

print(f"The hypothenuse is: {round(c, 2)}")



