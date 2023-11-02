# Método del punto fijo 
# Programa 3: Temas selectos de la física matemática
# Métodos numéricos
from math import*
############# Datos ##############################
print("Método del punto fijo\n")
ecuacion = input("Ingrese la función f(x)= ")
print("Ingrese un valor inicial:\n ")
x0 = float(input("x_0= "))
############### Definimos a la función #############
def f(x):
	return eval(ecuacion)
####################################################
print("Ingrese la tolerancia:\n ")
tol = float(input("Tol = "))
e = 1
iteraciones=1
while e>tol:
	xn = f(x0)
	print('{:^10}{:^10f}'.format(iteraciones,xn))
	e = abs(xn-x0)
	x0=xn
	iteraciones = iteraciones+1