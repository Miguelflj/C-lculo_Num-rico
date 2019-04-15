


import numpy as np

def LU(A,b,n):
	p = np.zeros(n)
	y = np.zeros(n)
	x = np.zeros(n)
	c = np.zeros(n)
	for i in range(n):
		p[i] = i

	#percorre os pivos da matriz
	for k in range(n-1):
		pv = abs(A[k][k])
		r = k
		for i in range(k+1,n):
			if(abs(A[i][k]) > pv):
				pv = abs(A[i][k])
				r = i

		if( pv == 0):
			#A matriz é singular
			break

		if(r != k):
			#atualiza o vetor de permutação
			aux = p[k]
			p[k] = p[r]
			p[r] = aux

			#troca as linhas da matriz
			aux = A[k].copy()
			A[k] = A[r]
			A[r] = aux

		for i in range(k+1,n):
			m = A[i][k]/A[k][k]
			A[i][k] = m
			for j in range(k+1,n):
				A[i][j] = A[i][j] - m*A[k][j]


	for i in range(n):
		r = p[i]
		c[i] = b[int(r)]

	for i in range(n):
		soma = 0
		for j in range(i):
			soma = soma + A[i][j]*y[j]
		y[i] = c[i] - soma


	for i in range(n-1,-1,-1):
		soma = 0
		for j in range(i+1,n):
			soma = soma + A[i][j]*x[j]
		x[i] = (y[i] - soma) /A[i][i]

	print("X1: " + str(x[0]))
	print("X2: " + str(x[1]))
	print("X3: " + str(x[2]))




def main():
	#Aloca matriz zerada nXn
	print("Entre com a dimensao do sistema");
	n = int(input())
	A = np.zeros((n,n))

	#Preenche matriz
	print("Entre os valores do sistema Ex: x y z de cada linha")
	for i in range(n):
		entrada = str(input())
		x,y,z = map(float,entrada.split())
		A[i][0] = x
		A[i][1] = y
		A[i][2] = z

	# aloca vetores zerados que vao ser utilizados
	b = np.zeros(n)
	
	#Valores depois do igual e preenche o vetor p de permutação
	for i in range(n):
		print("b["+str(i)+"]= ",end="")
		b[i] = float(input())
	LU(A,b,n)
main()

