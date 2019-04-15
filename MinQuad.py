
import numpy as np




def elGauss(A , b):
	n = 2
	# Implementa a eliminacao de Gauss sem pivoteamento parcial
	for k in range(n-1):
		for i in range(k+1,n):

			m = A[i][k] / A[k][k]
			A[i][k] = 0
			for j in range(k,n):
				A[i][j] = A[i][j] - ( m*A[k][j] )
			b[i] = b[i] - m*b[k]


	#retro substituicao

	X = np.zeros(2)
	X[n-1] = b[n-1]/A[n-1][n-1]
	for k in range(n-1,-1,-1):
		s = 0.0
		for j in range(k+1,n):
			s += (A[k][j]*X[j])
			X[k] = (b[k]-s)/A[k][k]

	print("a : " + str(X[0]) )
	print("b : " + str(X[1]) )













def MinQuadReta(ponts):
	x2 = 0
	x = 0
	n = 0
	xy = 0
	y = 0

	for i in range(len(ponts)):
		x2 = ( x2  + ( (ponts[i][0])*(ponts[i][0]) ))
		x = x + ponts[i][0]
		n += 1
		xy = (xy + ( (ponts[i][0]) * (ponts[i][1]) ) )
		y = y + ponts[i][1]

	mtz = np.zeros((2,2))
	r = np.zeros(2)

	mtz[0][0] = x2
	mtz[0][1] = x
	mtz[1][0] = x
	mtz[1][1] = n

	r[0] = xy
	r[1] = y

	elGauss(mtz,r)


def main():


	ponts = [(1.5,2),(2,3.2),(3,5.4),(4,4.9),(5,6.5),(6,10),(7,12),(8,13),(9,13.7),(10,15)]
	MinQuadReta(ponts)




main()



