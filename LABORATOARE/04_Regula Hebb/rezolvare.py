import numpy as np


print("\n\n******************* EXERCITIU 1*******************")
print("*************** Exemplu 4/ pag. 43 ***************\n")

x = np.array([
    [1,-2,1.5,0],
    [1,-0.5,-2,-1.5],
    [0,1,-1,1.5],
])
w=np.array([1,-1,0,0.5])
c=1


# line = x[0,:]
# # print(line)

# net = np.sum(line*w)
# # print(net)
# if net < 0:
#     o = -1
# else: o = 1

# w=w+c*o*line
# # print(w)


# line = x[1,:]
# net = np.sum(line*w)
# # print(net)
# if net < 0:
#     o = -1
# else: o = 1
# w = w+c*o*line

# # print(line)

# # print(w)

# line = x[2,:]
# net = np.sum(line*w)
# # print(net)
# if net < 0:
#     o = -1
# else: o = 1
# w = w+c*o*line

# # print(line)

# line = x[0,:]

# w=[1,-1,0,0.5]
# net = np.sum(line*w)
# e = 2.71
# f = (1-e**net)/(1+e**net)
# # print(w)
# net = np.sum(line*w)
# # print(f)
# # print(net)
# w = w+c*f*o*line
# # print(w)


# # i = 0
# # while i < 10:
# #     j = 0
# #     for 


for index in range(3):
    line = x[index,:]
    net = np.dot(line,w)
    w = w + np.sign(net)*x[index]
    print("\nSe aplica x", index+1, "\nw: ", w)


w=np.array([1,-1,0,0.5])

for index in range(3):
    net = np.dot(x[index], w)
    f= 2 / (1 + np.exp(-net)) - 1
    w = w + f * x[index]
    print("\nSe aplica x", index+1, ":\n f(net) =  ", f, "* w^", index+1, " = ", w)


print("\n******************* EXERCITIU 2*******************")
print("*************** Exercitiul 7/ pag. 49 ***************\n")


x=np.array([
    [1,-2],
    [0,1],
    [2,3],
    [1,-1]
    ])
w=np.array([1,-1])


for index in range(4):
    line = x[index,:]
    net = np.dot(line,w)
    w = w + np.sign(net)*x[index]
    print("\nSe aplica x", index+1, "\nw: ",w)

w=np.array([1,-1])

for index in range(4):
    net = np.dot(x[index], w)
    f= 2 / (1 + np.exp(-net)) - 1
    w = w + f * x[index]
    print("\nSe aplica x", index+1, ":\n f(net) =  ", f, "* w^", index+1, " = ",w)
