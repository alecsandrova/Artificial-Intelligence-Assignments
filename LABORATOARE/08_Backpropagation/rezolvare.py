
import random
import math
import numpy as np
from random import uniform
# "*****************************************************************
# Se citesc pattern-urile de instruire z1, z2,...,zn şi ieşirile dorite d1, d2,...,dn.Pattern-urile
# sunt extinse cu o componentă suplimentară cu valoarea -1. Se stabileşte numărul de
# intrări şi numărul de perceptroni. Se iniţializează aleator ponderile vji şi wkj. Se
# iniţializează constanta de instruire c. Pentru a accelera instruirea puteţi sa iniţializaţi
# constanta de instruire c cu o valoare mare, de exemplu c=50, şi să o scădeţi treptat. Se
# stabileşte eroarea maximă Emax. Se iniţializează E=0.
# *****************************************************************


#patternuri
pattern = np.array([[45,  85,  -1], 
     [50,  43,  -1], 
     [40,  80,  -1],
     [187, 107, -1], 
     [55,  42,  -1],
     [200, 43,  -1],
     [48,  40,  -1], 
     [195, 41,  -1],
     [43,  87,  -1],
     [192, 105, -1],
     [190, 40,  -1],
     [188, 100, -1]])


z = []

col0_norm = (pattern[:,0]-min(pattern[:,0])) / (max(pattern[:,0])- min(pattern[:,0]))
col1_norm = (pattern[:,1]-min(pattern[:,1])) / (max(pattern[:,1])- min(pattern[:,1]))
for i in range(12):
    z.append([col0_norm[i], col1_norm[i], -1])
print(z)


# datele de iesire dorite
d = [1,-1,1,-1,-1,1,-1,1,1,-1,1,-1]

# ponderi (y -> o)   wy
w = [uniform(-1,1), #w1
    uniform(-1,1),  #w2
    uniform(-1,1),  #w3
    uniform(-1,1)]  #w4 

# ponderi (z -> y)   vyz
v =[[uniform(-1,1), #v11
    uniform(-1,1),  #v12
    uniform(-1,1)], #v13

    [uniform(-1,1), #v21
    uniform(-1,1),  #v22
    uniform(-1,1)],  #v23

    [uniform(-1,1), #v31
    uniform(-1,1),  #v32
    uniform(-1,1)]] #v33 

# constanta de instruire
c = 0.1

#erori
E = 0
Emax = 1

# functia de activare bipolara continua
def f(net): 
     return 2/(1+math.e**(-net))-1

y = [0,0,0,-1] #iesiri perceptroni ascunsi
o = 0          #iesire retea

while True:
     # *****************************************************************
     # Având un pattern zp dintre cele n, se calculează ieşirile fiecărui perceptron
     # *****************************************************************
     E=0
     for p in range (len(z)):
          # print(p)
          for j in range (3):
               y[j] = f(np.dot(v[j],z[p]))
               # print('y', j,' =', y)
          o = f(np.dot(w,y))
          # print('o = ', o)

          # *****************************************************************
          # Se calculează semnalele de eroare:
          # *****************************************************************

          dy = [0,0,0,0]
          do = 0.5*(d[p]-o)*(1-o**2) 
          for j in range (4):
                dy[j] = 0.5*(1-y[j]**2)*(do*w[0] + do*w[1] + do*w[2] + do*w[3])
         

          # *****************************************************************
          # Se actualizează toate ponderile reţelei conform regulii:
          # *****************************************************************

          for j in range (3):
               for i in range (3):
                    v[j][i] += c * dy[j] * z[p][i]
          for j in range (4):
               w[j] += c * do*y[j]
     
          # *****************************************************************
          # Se calculează eroarea cumulată:
          # *****************************************************************
          
          E += 0.5*(d[p] - o)**2

          # c -= 1
     if E < Emax:
        print(E)
        break
     print(E)
print(w)


result=[0,0,0,0,0,0,0,0,0,0,0,0]
for p in range (len(z)):
     # print(p)
     for j in range (3):
          y[j] = f(np.dot(v[j],z[p]))
     o = f(np.dot(w,y))
     y[3] = -1

     net = 0
     for j in range(4):
          net += w[j] * y[j]
     
     result[p] = f(net)

for p in range (len(z)):
     if np.sign(result[p]) == 1:
          print("Patternul ", p, " apartine clasei 1")
     if np.sign(result[p]) == -1:
            print("Patternul ", p, " apartine clasei -1")
