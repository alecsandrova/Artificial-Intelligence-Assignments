import numpy as np
from numpy.linalg import norm


print("\n******************* EXERCITIU 1*******************\n")
x = np.array([2, 1, 2])
y = np.array([1, -1, 4])
cos = np.dot(x,y)/(norm(x)*norm(y))

p_scalar = np.dot(x,y)

print("Produs Scalar: ",p_scalar)

print("Lungime x " ,len(x))

print("Lungime y " ,len(x))

print("Cosinus ", cos)

print("\n******************* EXERCITIU 2*******************\n")

P0 = [-1, -1, -1]
P1 = [-1, -1, 1]
P2 = [-1, 1, -1]
P3 = [-1, 1, 1]
P4 = [1, -1, 1]
P5 = [1, -1, 1]
P6 = [1, 1, -1]
P7 = [1, 1, 1]



def clasificator(P):
    suma_ponderata = P[0]*1 + P[1]*1 + P[2]*1
    if suma_ponderata >= 1 :
        return "1"
    else :
        return "2"


print("P0: " + clasificator(P0))
print("P1: " + clasificator(P1))
print("P2: " + clasificator(P2))
print("P3: " + clasificator(P3))
print("P4: " + clasificator(P4))
print("P5: " + clasificator(P5))
print("P6: " + clasificator(P6))
print("P7: " + clasificator(P7))


print("\n******************* EXERCITIU 3*******************\n")

def step_function(a):
    return 1 if a > 0 else 0

pattern = np.array([
    [1,1,1,1,0,1,1,1,1],
    [0,1,0,1,0,1,0,1,0],
    [0,1,0,0,1,0,0,1,0],
    [1,1,0,0,1,0,0,1,0],
])

weights = np.array([-0.14, 0.06, -0.28, -0.93, -0.08, -0.28, -0.64, 0.47, -0.85])

line = pattern.shape[0]
col = pattern.shape[1]


for i in range(0,col):
    linie = pattern[0,:]
    sum =  linie[i]*weights[i]
print(step_function(sum))


print("\n******************* EXERCITIU 4*******************\n")


o1_prev = 1
o2_prev = 1
o3_prev = 1
while (True): 
    if o2_prev - o3_prev == 0 :
        o1 = o1_prev
    else:
        o1 = np.sign(o2_prev - o3_prev)
    if o1_prev - o3_prev == 0 :
        o2 = o2_prev
    else:
         o2 = np.sign(o1_prev - o3_prev)
    if -o1_prev - o2_prev == 0 :
        o3 = o3_prev
    else:
      o3 = np.sign(-o1_prev - o2_prev)

    if (o1_prev == o1 and o2_prev == o2 and o3_prev == o3):
        break
    o1_prev = o1
    o2_prev = o2
    o3_prev = o3
print(o1, " ", o2, " ", o3, " ")