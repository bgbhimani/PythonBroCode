import math

x = 144
print(math.pi)
print(math.e)

result = math.sqrt(x)
result = math.ceil(9.1)  # Round Up
result = math.floor(9.1)  # Round Down

# print(result)

# Excerise

# r = float(input("Enter the radius of the circle: "))

# cirfrrence = 2 * math.pi * r
# print(f"The Cirference is: {round(cirfrrence,2)}")
# area = math.pi * r
# print(f"The Area is {round(area,2)} cm²")


# Right Angle Triangle
# c² = a² + b²

a = float(input("Enter The Side A: "))
b = float(input("Enter The Side B: "))
c = math.sqrt(a**2 + b**2)
print(c)