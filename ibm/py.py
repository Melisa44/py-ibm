points = [(1,5),(5,8),(8,1),(9,5)]
def euclideanDistance(coordinate1,coordinate2):
    return pow(pow(coordinate1[0] - coordinate2[0] , 2) + pow(coordinate1[1] - coordinate2[1] , 2), 0.5)

distances=[]

for i in range(len(points)):
    for j in range(i+1, len(points)):
                distances.append(euclideanDistance(points[i], points[j]))

print(min(distances))