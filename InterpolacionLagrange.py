import matplotlib.pyplot as plt
import numpy as np
import sympy as sp 
x = sp.Symbol('x') 
n=int(input("ingrese el valor de n:"))
y=np.zeros(n)
i=0
p=0
ps=0
while i<n:
    y[i]=float(input("ingrese el valor de x_i:"))
    i=i+1
f=np.zeros(n)
i=0
while i<n:
    f[i]=float(input("ingrese el valor de f_i:"))
    i=i+1
i=0
j=0
l=1
while i<n:
    while j<n:
        if i!=j:
            l=l*(x-y[j])/(y[i]-y[j])
            j=j+1
        else:
            j=j+1
    print("l_i=",l)
    p=p+f[i]*l
    l=1
    i=i+1
    j=0
ps=p.expand()
print("El polinomio es: ",ps)
