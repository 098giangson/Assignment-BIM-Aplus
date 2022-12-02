#Nguyen Giang Son BIM APLUS
from shapely.geometry import Polygon

#Number of the polygon pointS
n=int(input("Enter the number of point: "))
#this is the loop
while n < 3:
    print("Invalid")
    n=int(input("Please enter the number of points not less than 3: "))

print("Valid")
#points coordinates
coordinates = []

for i in range(n):
    point = input(f"Point {i+1}: ")
    coords = point.split(" ")
    coords = [float(c) for c in coords]
    coordinates.append(coords)
    #the string 
polygon = Polygon(coordinates)
print(polygon.is_valid)

A = 0
for i in range(n):
    first = coordinates[(i+1) % n][0] + coordinates[i][0]
    second = coordinates[(i+1) % n][1] - coordinates[i][1]
    A += first * second
A = A/2
print (f"Ax: {A}")

Sx = 0
for i in range(n):
    first = coordinates[(i+1) % n][0] - coordinates[i][0]
    second = (coordinates[(i+1) % n][1])**2 + coordinates[i][1]*coordinates[(i+1) % n][1] + (coordinates[i][1])**2
    Sx += first * second
Sx = -Sx/6
print (f"Sx: {Sx}")