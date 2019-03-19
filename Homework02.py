import math

number = int(input("How many coordinates will you enter? "))
coordinates = []
for i in range(0,number):
    point = input("Please enter a point, i.e 1,2 for (1,2): ")
    points = point.split(",")
    coordinates.append((int(points[0]),int(points[1])))

print("Coordinates: ", coordinates)

for a in coordinates:
    listx = []
    listy = []
for a in coordinates:
    listx.append(a[0])
    listy.append(a[1])
    
#print("xs : ", listx)
#print("ys : ", listy)

def getavg(alist):
    size=len(alist)
    sum=0
    for item in alist:
        sum = sum + item
    avg = int (sum) / int (size)
    return avg

def centerofmass(listoftuple):
    listx, listy = zip(*listoftuple)
    avgx = getavg(listx)
    avgy = getavg(listy)
    list = (avgx,avgy)
    return list
xy = centerofmass(coordinates)
print("Center of mass: ", xy)

max=0 #Search until finding more starting from zero
min=999999 #Search until finding less starting from a number really big
maxCoordinate=(0,0)
minCoordinate=(0,0)
distances=[]
for i in coordinates:
    distance = math.sqrt((i[0]-xy[0])**2 + (i[1]-xy[1])**2)
    distances.append(distance)
    print("Distance for point", i, "is ", distance)
    if(distance>max):
        max = distance
        maxCoordinate=i
    if(distance<min):
        min=distance
        minCoordinate=i

print("Max distance and the farest coordinate: ", max, maxCoordinate)
print("Min distance and the closest coordinate: ", min, minCoordinate)