import random
import math
import numpy as np


patterns = [
    [45, 85],
    [50, 43],
    [40, 80],
    [55, 42],
    [200, 43],
    [48, 40],
    [195, 41],
    [43, 87],
    [190, 40]
    ]

# centroizi initiali
c1 = patterns[random.randint(0,8)]
c2 = patterns[random.randint(0,8)]
c3 = patterns[random.randint(0,8)]

while c1 == c2 or c1 == c3 or c2 == c3:
    c1 = patterns[random.randint(0,8)]
    c2 = patterns[random.randint(0,8)]
    c3 = patterns[random.randint(0,8)]
  
c1_old = c1
c2_old = c2
c3_old = c3

distances =[]

epoca = 0 

def dist(A,B):
    return abs(A[0] - B[0]) + abs(A[1] - B[1])

while True:
    print("Epoca: ", epoca)
    cluster1 = []
    cluster2 = []
    cluster3 = []
    for x in patterns:
        # d1 = math.sqrt((x[0]-c1[0])**2+(x[1]-c1[1])**2)
        # d2 = math.sqrt((x[0]-c2[0])**2+(x[1]-c2[1])**2)
        # d3 = math.sqrt((x[0]-c3[0])**2+(x[1]-c3[1])**2) 
        distances.append(dist(x, c1))
        distances.append(dist(x, c2))
        distances.append(dist(x, c3))
        min_dist = np.argmin(distances)
        if min_dist  == 0:
            cluster1.append(x)
        elif min_dist == 1:
            cluster2.append(x)
        elif min_dist == 2:
            cluster3.append(x)
        distances.clear()
        # if d1 > d2 and d1 > d3:
        #     cluster1.append(x)
        # if d2 > d1 and d2 > d3:
        #     cluster2.append(x)
        # if d3 > d1 and d3 > d2:
        #     cluster3.append(x)

    # new_c = [0,0]

    c1_old = c1
    if len(cluster1) != 0:
        c1 = [0,0]
        for point in cluster1: 
            c1 = [c1[0] + point[0], c1[1] + point[1] ]
        #     new_c[0] += point[0]
        #     new_c[1] += point[1]         
        # new_c[0] /= len(cluster1)
        # new_c[1] /= len(cluster1)
        # new_c[0] = round(new_c[0],2)
        # new_c[1] = round(new_c[1],2)
        # c1 = new_c
        c1 = [c1[0]/len(cluster1),round(c1[1]/len(cluster1),2) ]


    c2_old = c2
    if len(cluster2) != 0:
        c2 = [0,0]
        for point in cluster2:
            c2 = [c2[0] + point[0], c2[1] + point[1] ]
        c2 = [round(c2[0]/len(cluster2),2),round(c2[1]/len(cluster2),2) ]

    c3_old = c3
    if len(cluster3) != 0:
        c3 = [0,0]
        for point in cluster3:
            c3 = [c3[0] + point[0], c3[1] + point[1] ]
        c3 = [round(c3[0]/len(cluster3),2),round(c3[1]/len(cluster3),2) ]

    # print(c1_old,c2_old,c3_old)
    print(c1,c2,c3)

    epoca +=1

    if c1 == c1_old and c2 == c2_old and c3 == c3_old:
        break

print("Clusteri finali")
print(c1, c2, c3)
print("Puncte asociate:")
print("Cluster 1: ", cluster1)
print("Cluster 2: ", cluster2)
print("Cluster 3: ", cluster3)

