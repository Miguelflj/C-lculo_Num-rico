'''
	UFMT - CCOMP
	Professor: Linder
	Calculo Numerico - Eliminacao de Gauss
	Miguel Freitas
'''


import numpy as np

#Aloca e lê a matriz
print("Entre com a dimensao do sistema");
n = int(input())
A = np.zeros((n,n))
print("Entre os valores do sistema Ex: x y z de cada linha")
for i in range(n):
	entrada = str(input())
	x,y,z = map(float,entrada.split())
	#x,y = map(float,entrada.split())
	A[i][0] = x
	A[i][1] = y
	A[i][2] = z


# aloca vetor e lê vetor
b = np.zeros(n)
for i in range(n):
	print("b["+str(i)+"]= ",end="")
	b[i] = float(input())


# Implementa a eliminacao de Gauss sem pivoteamento parcial
for k in range(n-1):
	for i in range(k+1,n):

		m = A[i][k] / A[k][k]
		A[i][k] = 0
		for j in range(k,n):
			A[i][j] = A[i][j] - ( m*A[k][j] )
		b[i] = b[i] - m*b[k]


#retro substituicao

X = np.zeros(n)
X[n-1] = b[n-1]/A[n-1][n-1]
for k in range(n-1,-1,-1):
	s = 0.0
	for j in range(k+1,n):
		s += (A[k][j]*X[j])
		X[k] = (b[k]-s)/A[k][k]

print(X[0])
print(X[1])
print(X[2])