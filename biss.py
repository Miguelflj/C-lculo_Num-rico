
'''
Calc Num - Prof.: Linder



Algoritmo 1 - Metodo Bissecoes
Aluno: MIGUEL FREITAS
'''
def main():

	print("Entre com Xa Xb Erro")		
	#fx = lambda x: x**2 - 4
	fx = lambda x: x**3 - 27
	entrada = str(input())
	
	Xa,Xb,erro = map(float,entrada.split())
	while( abs(Xb-Xa) > erro):

		Xm = (Xa+Xb)/2
		if(fx(Xa)*fx(Xm) < 0 ):
			Xb = Xm

		elif(fx(Xa)*fx(Xm) > 0 ):
			Xa = Xm
		else:
			#Xm eh a raiz
			break 

	print((Xa + Xb)/2)


main()