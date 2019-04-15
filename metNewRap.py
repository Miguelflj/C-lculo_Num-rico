#UFMT - Ccomp
#Calculo Numerio - Prof: Linder
#Metodo Newton - Rhapson - 28/11

#Miguel Freitas
from math import e

def main():
	#fx = lambda x: x**3 - 27
	#flx = lambda x: 3*x**2 

	fx = lambda x: x*e**x - 2
	flx = lambda x: e**x + x*e**x
	print("Entre com o chute inicial e o erro toleravel: ")
	entrada = input()
	Xn,erro = map(float,entrada.split())
	Xk = Xn - (fx(Xn)/fl1x(Xn))
	while( (erro <= abs(Xk - Xn) ) or ( erro <= abs( fx(Xk) ) ) ):
		Xn = Xk
		Xk = Xn - ( fx(Xn)/flx(Xn) )

	print(Xk)

main()