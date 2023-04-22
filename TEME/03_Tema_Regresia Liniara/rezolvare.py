import pandas 
import matplotlib.pyplot as plot

plot.rcParams['figure.figsize'] = (5, 4)

salary_data = pandas.read_csv(r'D:\01_FACULTATE\03_SEM1\04_INTELIGENTA ARTIFICIALA\TEME\03_Tema_Regresia Liniara\Salary_data.csv')

x = salary_data.iloc[:, 0]
y = salary_data.iloc[:, 1]


w1 = 0
w2 = 0

w1_current = 1
w2_current = 1

length = len(salary_data)

c = 0.01 


while ((w1_current > 0.00001) or (w2_current > 0.00001)):
    dreapta_regresie = w1*x + w2  
    deriv_p1 = (-1/length) * sum(x * (y - dreapta_regresie))      #obtinuta din functia de eroare             
    deriv_p2 = (-1/length) * sum(y - dreapta_regresie)            #obtinuta din functia de eroare

    w1_old = w1
    w2_old = w2

    w1 -= c * deriv_p1  
    w2 -= c * deriv_p2  

    w1_current = abs(w1 - w1_old)
    w2_current = abs(w2 - w2_old)

    
print('w1 :', w1)
print('w2 :', w2)

plot.scatter(x, y) 

plot.plot([min(x), max(x)], [min(dreapta_regresie), max(dreapta_regresie)], color='pink')  

plot.xlabel('YearsExperience[x]')
plot.ylabel('Salary[y]')

plot.show()