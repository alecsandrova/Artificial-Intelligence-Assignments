import numpy as np
import math

print("\n// *****************************************************************")
print("// b. Initializarea populaţiei. Se generează aleator 50 de cromozomi")
print("// *****************************************************************\n")
cromozomi = [[0]*10]*50
for i in range(50):
    cromozomi[i] =  np.random.randint(0,2,10)

for i in range(50):
    print(cromozomi[i])

    epoci = 0
    breakBool = False
    ok = True
while(ok): 
    
    epoci=epoci+1
    print("\n// *****************************************************************")
    print("// c. Evaluarea cromozomilor. Se calculează valoarea functiei obiectiv \n// pentru fiecare cromozom")
    print("// *****************************************************************\n")

    sum = [0]*50
    prod = [1]*50
    # f_obj = [[0]*2]*50
    f_shape = (50,2)
    f_obj = np.zeros(f_shape)
    # print(sum)

    for i in range(50):
        for j in range(10):
            if cromozomi[i][j] == 0: 
                sum[i] += j+1
            else:  
                if cromozomi[i][j] == 1:
                    prod[i] *= j+1

    for i in range(50):
        f_obj[i][1] = int(i)
        f_obj[i][0] = round((abs(sum[i]-36))/36 + (abs(prod[i]-360))/360,2)
        if(f_obj[i][0] == 0.00):
            breakBool = True
        print("Funtia obiectiv nr. ", i+1, " :", f_obj[i])
        if breakBool == True:
            print("S-a gasit cromozomul ", i, " cu functia obiectiv = 0 ", cromozomi[i],": ", f_obj[i][0])
            ok = False
        
    
    print("\n// *****************************************************************")
    print("// d. Selecţia cromozomilor pentru generaţia următoare.")
    print("// *****************************************************************\n")


    # for i in range(50):
    #     print(f_obj[i])
    # f_obj = np.array(f_obj)
    # f_obj.sort()
    # f_obj = np.array(f_obj)
    f_obj = f_obj[f_obj[:,0].argsort()]
    f_obj[48] = f_obj[0]
    f_obj[49] = f_obj[1]
    # for i in range(50):
    #     print(f_obj[i])
    # f_obj[48] = f_obj[0]
    # f_obj[49] = f_obj[1]
    # print(f_obj)

    # for i in range(50):
    #     print(cromozomi[i])


    # print("new")
    # for i in range(50):
    #     print(cromozomi[i])

    print("\n// *****************************************************************")
    print("// e. Aplicarea operaţiilor genetice.")
    print("// *****************************************************************\n")

    cromozomi_old = cromozomi
    for i in range(50):
        cromozomi[i] = cromozomi_old[int(f_obj[i][1])]

    cromozomi_old = cromozomi

    # for i in range(50):
    #     if i == 25:
    #         print("---")
    #     print(cromozomi[i])

    for i in range(2):
        rand_i = np.random.randint(0,50)
        rand_j = np.random.randint(0,50)
        aux = cromozomi [rand_i][5:]
        cromozomi[rand_i] = np.concatenate((cromozomi[rand_i][:5] , cromozomi[rand_j][5:]), axis=0)
        cromozomi[rand_j] = np.concatenate((cromozomi[rand_j][:5] , aux), axis=0)

    # print("new")
    # for i in range(50):
    #     print(cromozomi[i])

    for i in range(5):
        rand_i = np.random.randint(0,50)
        rand_j = np.random.randint(0,10)
        if cromozomi[rand_i][rand_j] == 1:
            cromozomi[rand_i][rand_j] = 0
        else:
            cromozomi[rand_i][rand_j] = 1
    # print("new")

    for i in range(50):
        print(cromozomi[i])

    if epoci == 50:
            print("\nCromozomi finali:")
            for i in range(50):
                print(cromozomi[i], "suma: ", sum[i], " produs: ", prod[i], " f_obj: ", f_obj[i][0])
            ok=False


