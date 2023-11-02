import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
x = sp.Symbol('x')
n=int(input("ingrese el valor de n:"))
xi=np.zeros(n)
A=np.zeros((n,n))
i=0
while i<n:
    xi[i]=float(input("ingrese el valor de x_i:"))
    i=i+1
b=np.zeros(n)
i=0
while i<n:
    b[i]=float(input("ingrese el valor de f_i:"))
    i=i+1
i=0
while i<n:
    A[i][0]=1
    i=i+1
i=0
j=0
while j<n-1:
    while i<n:
        A[i][j+1]=xi[i]**(j+1)
        i=i+1
    j=j+1
    i=0
print(A)
print("b=",b)
a=np.zeros(n)
a = np.linalg.inv(A).dot(b)
print("a=",a)
p=0
ps=0
i=0
while i<n:
    p=p+a[i]*x**i
    i=i+1
ps=p.expand()
print("p=",ps)

