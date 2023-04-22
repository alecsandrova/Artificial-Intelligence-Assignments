x_prev = 0
x_current = 10
c = 0.01

while abs(x_current-x_prev) > 0.00001:
    aux = x_current
    x_current = x_prev-c*(12*x_prev-12)
    x_prev = aux
    print("1. Functia este 6*", x_current,"^2 - 12* ", x_current,"+ 1 = ", 6*x_current**2-12*x_current+1 )

# print(x_current, x_prev)
print("1. Functia minima este 6*", x_current,"^2 - 12* ", x_current,"+ 1 = ", 6*x_current**2-12*x_current+1 )

x_prev = 0
x_current = 10
y_prev = 0
y_current = 10
c = 0.01


while abs(x_current-x_prev) > 0.00001 and (abs(y_current-y_prev) > 0.00001):
    aux_x = x_current
    x_current = x_prev-c*2*x_prev
    x_prev = aux_x

    aux_y = y_current
    y_current = y_prev-c*4*y_prev
    y_prev = aux_y
    print("2.1 Functia este ", x_current, "^2 + 2*", y_current, "^2 = ", x_current**2+2*y_current**2)

# print(x_current, x_prev)
# print(y_current, y_prev)
print("2.1 Functia minima este ", x_current, "^2 + 2*", y_current, "^2 = ", x_current**2+2*y_current**2)

x_prev = 0
x_current = 10
y_prev = 0
y_current = 10
c = 0.01

# while abs(x_current-x_prev) > 0.00001 and (abs(y_current-y_prev) > 0.00001):
#     aux_x = x_current
#     x_current = x_prev-c*(2*(1-x_prev)+200*(x_prev-y_prev**2))
#     x_prev = aux_x

#     aux_y = y_current
#     y_current = y_prev-c*200*(x_prev-y_prev**2)*(-2*y_prev)
#     y_prev = aux_y
#     print("2.2 Functia este (1 - ",x_current,")^2 + 100(", x_current," - ", y_current,"^2)^2 = ",(1-x_current)**2 + 100*(x_current - y_current**2)**2)


# print("2.2 Functia  minima este (1 - ",x_current,")^2 + 100(", x_current," - ", y_current,"^2)^2 = ",(1-x_current)**2 + 100*(x_current - y_current**2)**2)
