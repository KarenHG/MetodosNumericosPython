print('Efrain Soto Olmos')
print('Metodo de Rungen Kuta para 4 orden, en sistema de ecuaciones')
from sympy import *
from sympy.abc import _clash1
import math
t = Symbol('t')
y = Symbol('y')
x = Symbol('x')
#Captura de datos
F = input('Escribe la funcion f(t,x,y) =')
G = input('Escribe la funcion g(t,x,y) =')
n = int(input('Numero de iteraciones ='))
a = float(input('tiempo inicial t0 ='))
b = float(input('tiempo final tf ='))
y0 = float(input('condicion inicial y0 ='))
x0 = float(input('condicion inicial x0 ='))
h = (b-a)/n
print('tiempo de paso =',h)
#Transformacion de la funcion de tipo str a _clash1
fun = sympify(F , locals=_clash1)
gun = sympify(G , locals=_clash1)
#Metodo de Euler
print('Metodo de Rungen 4 orden')
#Sumas
w = 0
v = 0
k1 = 0
k2 = 0
k3 = 0
k4 = 0
l1 = 0
l2 = 0
l3 = 0
l4 = 0
for i in range(0,n):
     t0 = a +i*h
     print("valor de t{} = ".format(i),t0,)
     #Valores constantes K y L
     k1 = h*(fun.subs([(t,t0),(x,x0),(y,y0)]))
     l1 = h*(gun.subs([(t,t0),(x,x0),(y,y0)]))
     k2 = h*(fun.subs([(t,t0+h/2),(x,x0+h*k1/2),(y,y0+h*l1/2)]))
     l2 = h*(gun.subs([(t,t0+h/2),(x,x0+h*k1/2),(y,y0+h*l1/2)]))
     k3 = h*(fun.subs([(t,t0+h/2),(x,x0+h*k2/2),(y,y0+h*l2/2)]))
     l3 = h*(gun.subs([(t,t0+h/2),(x,x0+h*k2/2),(y,y0+h*l2/2)]))
     k4 = h*(fun.subs([(t,t0+h),(x,x0+h*k3),(y,y0+h*l3)]))
     l4 = h*(gun.subs([(t,t0+h),(x,x0+h*k3),(y,y0+h*l3)]))
     #Sustitucion de los valores
     w = x0 + (1/6)*(k1 + 2*k2 + 2*k3 +k4) 
     v = y0 + (1/6)*(l1 + 2*l2 + 2*l3 +l4)
     x0 = w
     y0 = v
     print('valor de x{} ='.format(i+1),w,'valor de y{} ='.format(i+1),v)
