import numpy as np
import random
import math

w1 = [random.randint(0,100),random.randint(0,100)]    

w2= [random.randint(0,100),random.randint(0,100)]

w3 = [random.randint(0,100),random.randint(0,100)]

c =0.1

e = 100

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

for i in range(e):
    for x in patterns:
        d1 = math.sqrt((x[0]-w1[0])**2+(x[1]-w1[1])**2)
        d2 = math.sqrt((x[0]-w2[0])**2+(x[1]-w2[1])**2)
        d3 = math.sqrt((x[0]-w3[0])**2+(x[1]-w3[1])**2) 

        if d1 < d2 and d1 < d3:
            w1 = np.array(w1)
            w1 = w1 + c*np.array((x-w1)) 
            w1 = np.round(w1,2)
            # print(w1)   

        if d2 < d1 and d2 < d3:
            w2 = np.array(w2)
            w2 = w2 + c*np.array((x-w2)) 
            w2 = np.round(w2,2)
            # print(w2)   

        if d3 < d1 and d3 < d2:
            w3 = np.array(w3)
            w3 = w3 + c*np.array((x-w3)) 
            w3 = np.round(w3,2)
            # print(w3)

i = 0
for x in patterns:
    d1 = math.sqrt((x[0]-w1[0])**2+(x[1]-w1[1])**2)
    d2 = math.sqrt((x[0]-w2[0])**2+(x[1]-w2[1])**2)
    d3 = math.sqrt((x[0]-w3[0])**2+(x[1]-w3[1])**2) 

    if d1 < d2 and d1 < d3:
     print("Patternul " + str(i) + " apartine prototipului 1")   

    if d2 < d1 and d2 < d3:
        print("Patternul " + str(i) + " apartine prototipului 2")   

    if d3 < d1 and d3 < d2:
         print("Patternul " + str(i) + " apartine prototipului 3")

    i = i+1