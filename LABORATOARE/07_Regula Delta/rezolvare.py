import numpy as np

# ("\n// *****************************************************************")
# ("// 1. Se citesc pattern-urile de instruire y1, y2,...,yN şi ieşirile dorite d1, d2,...,dN. Se scalează
# toate valorile din setul de date. Se stabileşte numărul M de intrări şi numărul K de 
# perceptroni. Se iniţializează ponderile wji cu valori aleatoare din intervalul [-1;1]. Se 
# iniţializează constanta de instruire c. Se stabileşte eroarea maximă Emax. Se iniţializează 
# E=0")
# ("// *****************************************************************\n")


# Întotdeauna se adaugă o intrare suplimentară cu valoarea  constantă -1.
y = [[45, 85, -1], 
     [50, 43, -1], 
     [40, 80, -1], 
     [55, 42, -1],
     [200, 43, -1],
     [48, 40, -1], 
     [195, 41, -1],
     [43, 87, -1],
     [190, 40, -1]]

# iesirile dorite
d = [[1, -1, -1],
     [-1, 1, -1],
     [1, -1, -1],
     [-1, 1, -1],
     [-1, -1, 1],
     [-1, 1, -1],
     [-1, -1, 1],
     [1, -1, -1],
     [-1, -1, 1]]

d=np.array(d)


min=1000000
max=0

arr = [[],
[],
[],
[],
[],
[],
[],
[],
[]]


for x in y:
    for val in range(len(x)-1):                       
        if x[val]>max:
            max=x[val]
        elif x[val]<min:
            min=x[val]
i=0

 #scalare
for x in y:
    for val in range(len(x)-1):
        arr[i].append((x[val]-min)/(max-min))      
    arr[i].append(-1)
    i=i+1
    

arr=np.array(arr)

#functia de activare a perceptronilor
def f(net):
    return ((2 / (1 + np.exp(-net))) - 1)         


w =2 * np.random.random((3,3))-1            
K = 3 #numar perceptroni
c = 1 #constanta de instruire
Emax = 0.0005 #eroarea maxima
E = 0

while True:

# ("\n// *****************************************************************")
# ("//2. Având un pattern yp=[yp1,…,ypi,…,ypM] dintre cele n, se calculează ieşirile fiecărui 
# perceptron: ")
# ("// *****************************************************************\n")
    o = []
    for i in range(9):
        o.append(f(np.dot(w, arr[i]))) #se calculeaza iesirile fiecarui perceptron
    o=np.array(o)


# ("\n// *****************************************************************")
# ("// Se actualizează toate ponderile reţelei conform regulii")
# ("// *****************************************************************\n")


    for l in range(0, len(arr)):
        for j in range(0, len(o[0])):
            for i in range(0, len(arr[0])):
                w[j, i] += c * (d[l, j] - o[l][j]) * (1 - o[l][j] ** 2) * arr[l, i]
                # se actualizeaza ponderile retelei


# ("\n// *****************************************************************")
# ("// 4. Se calculează eroarea cumulată:")
# ("// *****************************************************************\n")


    E = 0
    for j in range(0, len(arr)):
        for i in range(0, len(d[0]) - 2):
            E += (d[j, i] - o[j][i]) ** 2 #eroarea cumulata
    if E < Emax:
        break




o_new=[]
for i in range(9):
    o_new.append(f(np.dot(w, arr[i])))


def afisare(pattern, response, object):
    print("\nPattern: ", pattern)
    print(response)
    print("Found object: ", object)

for i in range(len(o_new)):
    if np.sign(o_new[i][0]) == -1:
        if np.sign(o_new[i][1]) == -1:
            afisare(arr[i], o_new[i],"bed" )
        else:
            afisare(arr[i], o_new[i],"table" )
    else:
        afisare(arr[i], o_new[i],"chair" )