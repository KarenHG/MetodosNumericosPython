import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
x = sp.Symbol('x')
n=int(input("ingrese el valor de n:"))
xi=np.zeros(n)
A=np.zeros((n,n))
i=0
fa=0
fb=0
while i<n:
    xi[i]=float(input("ingrese el valor de x_i:"))
    i=i+1
a=np.zeros(n)
i=0
while i<n:
    a[i]=float(input("ingrese el valor de f_i:"))
    i=i+1
fa=float(input("ingrese el valor de S(a):"))
fb=float(input("ingrese el valor de S(b):"))
i=0
h=np.zeros(n-1)
while i<n-1:
    h[i]=xi[i+1]-xi[i]
    i=i+1
print("h=",h)
B=np.zeros(n)
B[0]=3*(a[1]-a[0])/h[0]-3*fa
i=0
while i<n-2:
    B[i+1]=3*(a[i+2]-a[i+1])/h[i+1]-3*(a[i+1]-a[i])/h[i]
    i=i+1
B[n-1]=3*fb-3*(a[n-1]-a[n-2])/h[n-2]
print("b=",B)
A[0][0]=2*h[0]
i=0
while i<n-2:
    A[i+1][i+1]=2*(h[i]+h[i+1])
    i=i+1
A[n-1][n-1]=2*h[n-2]
i=0
while i<n-1:
    A[i][i+1]=h[i]
    i=i+1
i=0
while i<n-1:
    A[i+1][i]=h[i]
    i=i+1
print("A=",A)
c=np.linalg.inv(A).dot(B)
print("x=",c)
d=np.zeros(n-1)
i=0
while i<n-1:
    d[i]=(c[i+1]-c[i])/3*h[i]
    i=i+1
print("d=",d)
b=np.zeros(n-1)
i=0
while i<n-1:
    b[i]=(a[i+1]-a[i])/h[i]-h[i]*(2*c[i]+c[i+1])/3
    i=i+1
print("bi=",b)
S=0
Ss=0
i=0
while i<n-1:
    S=a[i]+b[i]*(x-xi[i])+c[i]*(x-xi[i])**2+d[i]*(x-xi[i])**3
    Ss=S.expand()
    print("si=",S)
    print("si=",Ss)
    i=i+1
    Ss=0
    S=0
