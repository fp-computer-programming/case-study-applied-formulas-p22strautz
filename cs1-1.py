# Author: SCT (ADMG) 10/12/21

x1 = int(input("Input your first x value.\n"))

y1 = int(input("Input your first y value.\n"))

x2 = int(input("Input your second x value.\n"))

y2 = int(input("Input your second y value.\n"))

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5

distance = str(distance)

print("distance = " + distance + " ")
