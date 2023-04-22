import csv
import numpy as np

# **************************************************************************************************
# ***** 1. Încărcați fișierul de date Iris de la https://archive.ics.uci.edu/ml/datasets/iris. *****
# **************************************************************************************************

print("\n***********************************************************************************************************")
print("\n Prelucrarea datelor - NEAGU ELENA-ALEXANDRA 4LF701 B")
print("\n***********************************************************************************************************")

myList = []
with open("iris.data","r") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
            if len(row) == 5:
                myList.append([float(row[0]), float(row[1]), float(row[2]), float(row[3])])

npArray = np.array(myList)

# ***********************************************************************************************************
# ***** 2. Pentru fiecare coloană cu valori numerice calculați valoarea minima, maximă, medie, mediană. *****
# ***********************************************************************************************************

print("\n***********************************************************************************************************")
print("2. Pentru fiecare coloană cu valori numerice calculați valoarea minima, maximă, medie, mediană. ")
print("***********************************************************************************************************\n")
for i in range(0,4) :
    collumn_min = np.min(npArray[:,i])
    collumn_max = np.max(npArray[:,i])
    npArray[:,i].sort()
    if len(npArray[:,i])%2==1 :
        collumn_median = 0
        collumn_median = round(npArray[(len(npArray[:,i])-1)//2,i],2)
    else : 
        collumn_median1 = 0 
        collumn_median2 = 0
        collumn_median1 = round(npArray[(len(npArray[:,i])//2),i],2)
        collumn_median2 = round(npArray[(len(npArray[:,i])//2)+1,i],2)
    collumn_average = round(sum(npArray[:,i]) / len(npArray[:,i]),2 )

    print("\nCOLUMN ", i )
    print("min: ", collumn_min)
    print("max: ", collumn_max)
    if len(npArray[:,i])%2==1 :
      print("median value: ", collumn_median)
    else:
        print("median values: ", collumn_median1, collumn_median2)
    print("average: ", collumn_average )


# *****************************************************************************************
# 3. Normalizați valorile de pe fiecare coloană folosind formula 𝑥𝑛𝑜𝑟𝑚 = 𝑥−𝑚𝑖𝑛/(𝑚𝑎𝑥−𝑚𝑖𝑛).
# *****************************************************************************************

print("\n***********************************************************************************************************")
print("3. Normalizați valorile de pe fiecare coloană folosind formula 𝑥𝑛𝑜𝑟𝑚 = 𝑥−𝑚𝑖𝑛/(𝑚𝑎𝑥−𝑚𝑖𝑛). ")
print("***********************************************************************************************************\n")

norm_array = []
norm_matrix = []
for i in range(0,4) :
    collumn = npArray[:,i]
    norm_array = []
    for x in collumn:
        norm_x = round((x -min(npArray[:,0])) / (max(npArray[:,0])-min(npArray[:,0])),2)
        norm_array = np.append(norm_array,norm_x)
    if i == 0:
        norm_matrix = np.append(norm_matrix, norm_array)
    else:
         norm_matrix = np.column_stack((norm_matrix, norm_array))

print(norm_matrix)


    
# *****************************************************************************************
# 4. Calculați suma ponderată a valorilor numerice de pe fiecare linie înmulțind fiecare 
# valoare cu un coeficient pe care îl numim pondere și salvați rezultatele într-o nouă 
# coloană a tabelului vostru. Folosiți următoarele valori pentru ponderi: [0.2, 1.1, -0.9, 1].
# *****************************************************************************************

print("\n***********************************************************************************************************")
print("4. Calculați suma ponderată a valorilor numerice de pe fiecare linie înmulțind fiecare ")
print("valoare cu un coeficient pe care îl numim pondere și salvați rezultatele într-o nouă ")
print("coloană a tabelului vostru. Folosiți următoarele valori pentru ponderi: [0.2, 1.1, -0.9, 1]")
print("***********************************************************************************************************\n")

array=[]
for row in npArray:
    sum_pond = row[0]*0.2 + row[1]*1.1 + row[2]*(-0.9) + row[3]*1
    array.append(sum_pond)
array = np.vstack(array)
npArray = np.append(npArray,array, axis = 1)
print(npArray)



# *****************************************************************************************
# 5. Scalarea unei imagini digitale presupune redimensionarea acesteia prin mărirea sau 
# reducerea numărului de pixeli. Setul de date disponibil la 
# http://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits-orig.tra.Z
# conține imagini ale unor cifre scrise de mână reprezentate sub forma de matrice
# binare de dimensiune 32x32. Scrieți o metodă de scalare a unei astfel de imagini 
# prin reducerea dimensiunii la 16x16 pixeli. Folosiți o fereastră glisantă de 
# dimensiune 2x2 pe care o deplasați peste imaginea inițială. Dacă fereastra conține 3
# sau 4 valori de 0, aceasta se transformă într-o valoare de 0 în imaginea scalată, iar 
# altfel vom avea o valoare de 1. Evaluați vizual calitatea imaginilor obținute prin 
# această metodă.
# *****************************************************************************************

print("\n***********************************************************************************************************")
print("5. Scalarea unei imagini digitale presupune redimensionarea acesteia prin mărirea sau ")
print("reducerea numărului de pixeli. Setul de date disponibil la ")
print("http://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits-orig.tra.Z")
print("conține imagini ale unor cifre scrise de mână reprezentate sub forma de matrice")
print("binare de dimensiune 32x32. Scrieți o metodă de scalare a unei astfel de imagini ")
print("prin reducerea dimensiunii la 16x16 pixeli. Folosiți o fereastră glisantă de ")
print("dimensiune 2x2 pe care o deplasați peste imaginea inițială. Dacă fereastra conține 3")
print("sau 4 valori de 0, aceasta se transformă într-o valoare de 0 în imaginea scalată, iar ")
print("altfel vom avea o valoare de 1. Evaluați vizual calitatea imaginilor obținute prin ")
print("această metodă.")
print("\n***********************************************************************************************************")


i = 0
image = []
imageFound = False
file = open("image.tra","r")
x_prev = ""
for x in file:
    if x_prev.__contains__("lastparag = 0"):
        imageFound = True
    if x.__contains__(" 0\n"):
        imageFound = False
        # print(image)
    if imageFound == True:  
        arr = np.array(list(x))
        if len(image) == 0:
            image = arr
        else:
            image = np.append(image, arr)
            image = image[image != '\n']
    x_prev = x

rowsNum = len(image)//32
image = np.reshape(image, (rowsNum,32))
indX = 0
indY = 0
sum = 0
imageResized = []
while indX < rowsNum:
    indY = 0
    while indY < 32:
        sum = image[indX][indY].astype(int) + image[indX+1][indY].astype(int) + image[indX][indY+1].astype(int) + image[indX+1][indY+1].astype(int)
        if sum > 1:
            imageResized = np.append(imageResized, 1)
        else:
            imageResized =  np.append(imageResized, 0)
        indY = indY +2
    indX = indX +2


rowsNum2 = len(imageResized)//16
imageResized = np.reshape(imageResized, (rowsNum2,16))
print(imageResized)




