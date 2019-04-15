
import numpy as np


def lagrangeInterp(pts,px):
	p = 0
	for k in range(len(pts)):
		L = 1
		for i in range(len(pts)):	
			if( i != k):
				L = (px -pts[i][0])/(pts[k][0] - pts[i][0]) * L
		
		p = p + (pts[k][1]) * L 
		
	return p

def main():
	ponts = [(-1,4),(0,1),(2,-1)]
	#ponts = [(0,2),(1,4),(2,8),(3,16)]

	print("Entre com o valor de interpolacao: ")
	x = float(input())

	y = lagrangeInterp(ponts,x)

	print("Valor interpolado: " + str(y) )
	





main()