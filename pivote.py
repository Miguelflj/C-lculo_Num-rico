import numpy as np

#Aloca e lê a matriz
print("Entre com a dimensao do sistema");
n = int(input())
A = np.zeros((n,n))
print("Entre os valores do sistema Ex: x y z de cada linha")
for i in range(n):
	entrada = str(input())
	x,y,z = map(float,entrada.split())
	A[i][0] = x
	A[i][1] = y
	A[i][2] = z
# aloca vetor e lê vetor
b = np.zeros(n)
for i in range(n):
	print("b["+str(i)+"]= ",end="")
	b[i] = float(input())


# Implementa a eliminacao de Gauss sem pivoteamento parcial
for i in range(n-1):
	k = i + 1
	#pivoteamento parcial
	maior = A[k][i]
	pos = k
	for k in range(i+1,n):
		if(abs(maior) < abs(A[k][i]) ):
			maior = A[k][i]
			pos = k
	linhaAux = A[i].copy()
	A[i] = A[pos]
	A[pos] = linhaAux
	for k in range(i+1,n):
		m = A[k][i] / A[i][i]
		A[k][i] = 0
		for j in range(k,n):
			A[k][j] = A[k][j] - ( m*A[i][j] )
		b[k] = b[k] - m*b[i]


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