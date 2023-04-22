import numpy as np
import random

w  = np.array([0, 1, 0])
x1 = np.array([2, 1, -1])
d1 = -1
x2 = np.array([0, -1, -1])
d2 = 1
net1 = random.randint(0,100)
net2 = random.randint(-100,0)
c= 0.1


print("************** X1 ****************")
print("x1 = ", x1)
print("w1 = ", w)
print("net1 = ", net1)

while np.sign(net1) != d1: #daca d1 =  sign net1 => delta w = 0
    w = w + (-2)*c*x1
    net1 = np.dot(w,x1)
    print("net1 = ", np.round(net1,2))
    print(w)

print("sgn(net1) = d1 = -1, w1 = ", w)

w  = np.array([0, 1, 0])
print("\n************** X2 ****************")
print("x2 = ", x2)
print("w2 = ", w)
print("net2 = ", net2)
while np.sign(net2) != d2:
    w = w + 2*c*x2
    net2 = np.dot(w,x2)
    print("net2 = ", np.round(net2,2))
    print(w)
print("sgn(net2) = d2 = -1, w2 = ", w)
