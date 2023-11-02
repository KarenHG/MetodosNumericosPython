# Método de Bisección 
# Programa 1: Temas selectos de la física matemática
# Métodos numéricos
from math import*
############# Datos ##############################
print("Método de bisección\n")
ecuacion = input("Ingrese la función f(x)= ")
print("Ingrese un intervalo [a,b]:\n ")
a = float(input("a= "))
b = float(input("b= "))
############### Definimos a la función #############
def f(x):
	return eval(ecuacion)
####################################################
intervalos = int(input("Ingresar el número de subintervalos: "))
puntos = intervalos + 1
ancho = (b-a)/intervalos
#################### Tabla ################################
print('{:^10}{:^10}'.format('p','f(p)')) # Encabezado de tabla
while a<=b:
	print('{:^10f}{:^10f}'.format(a,f(a)))
	a=a+ancho
###########################################################
respuesta = input("Desea iniciar el método de bisección S/N: ")
if respuesta == 'S':
	print("Método de bisección iniciado")
	print("Ingrese el intervalo adecuado \n")
	a = float(input("a= "))
	b = float(input("b= "))
	if f(a)*f(b)<0:
		tol = float(input("Ingrese la tolerancia permitida: "))
		r = (a+b)/2
		e = abs(f(r))
		iteraciones = 1
		print('{:^10}{:^10}{:^10}{:^10}'.format('iteraciones','Raíz','f(r)','Error'))
		print('{:^10}{:^10f}{:^10f}{:^10f}'.format(iteraciones,r,f(r),e))
		while e>tol:
			if f(a)*f(r)<0:
				b=r
			else:
				a=r
			r = (a+b)/2
			e = abs(f(r))
			iteraciones = iteraciones +1
			print('{:^10}{:^10f}{:^10f}{:^10f}'.format(iteraciones,r,f(r),e))
		print("\nLa aproximación de la raíz es: ")
		print(r)
		print("\nEl número de iteraciones es: ")
		print(iteraciones)
	else:
		print("No se puede aplicar el método de bisección pues el intervalo no es adecuado")
else:
	print("Programa terminado")