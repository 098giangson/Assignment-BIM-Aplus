#Nguyen Giang Son BIM APLUS
# it changed
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

Ax = 0
for i in range(n):
    xi = coordinates[i][0]
    xi1 = coordinates[(i+1) % n][0]

    yi = coordinates[i][1]
    yi1 = coordinates[(i+1) % n][1]

    first = xi1 + xi
    second = yi1 - yi
    Ax += first * second
Ax = Ax/2
print (f"Ax: {Ax}")

Sx = 0
for i in range(n):
    first = coordinates[(i+1) % n][0] - coordinates[i][0]
    second = (coordinates[(i+1) % n][1])**2 + coordinates[i][1]*coordinates[(i+1) % n][1] + (coordinates[i][1])**2
    Sx += first * second
Sx = -Sx/6
print (f"Sx: {Sx}")

Sy = 0
for i in range(n):
    xi = coordinates[i][0]
    xi1 = coordinates[(i+1) % n][0]

    yi = coordinates[i][1]
    yi1 = coordinates[(i+1) % n][1]

    first = yi1 - yi
    second = xi1**2 + xi*xi1 + xi**2
    Sy += first * second
Sy = Sy/6
print (f"Sy: {Sy}")

Ix = 0
for i in range(n):
    xi = coordinates[i][0]
    xi1 = coordinates[(i+1) % n][0]

    yi = coordinates[i][1]
    yi1 = coordinates[(i+1) % n][1]

    first = xi1 - xi
    second = yi1**3 + (yi1**2)*yi + yi1*(yi1**2) + yi**3
    Ix += first * second
Ix = -Ix/12
print (f"Ix: {Ix}")

Iy = 0
for i in range(n):
    xi = coordinates[i][0]
    xi1 = coordinates[(i+1) % n][0]

    yi = coordinates[i][1]
    yi1 = coordinates[(i+1) % n][1]

    first = yi1 - yi
    second = xi1**3 + (xi1**2)*xi + xi1*xi**2 + xi**3
    Iy += first * second
Iy = Iy/12
print (f"Iy: {Iy}")

Ixy = 0
for i in range(n):
    xi = coordinates[i][0]
    xi1 = coordinates[(i+1) % n][0]

    yi = coordinates[i][1]
    yi1 = coordinates[(i+1) % n][1]

    first = yi1 - yi
    second = yi1*((3*xi1**2 + 2*xi1*xi + xi**2) + yi*(3*xi**2 + 2*xi1*xi + xi1**2))
    Ixy += first * second
Ixy = -Ixy/24
print (f"Ixy: {Ixy}")

xt = Sy/Ax
print (f"xt: {xt}")

yt = Sx/Ax
print (f"yt: {yt}")

Ixt = Ix - yt**2*Ax
print (f"Ixt: {Ixt}")

Iyt = Iy - xt**2*Ax
print (f"Iyt: {Iyt}")

Ixyt = Ixy + xt*yt*Ax
print (f"Ixyt: {Ixyt}")

print ("Nguyen Giang Son BIM Aplus 2022") 