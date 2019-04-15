

import numpy as np


mtz1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
mtz2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
mtz3 = np.zeros((3,3))
soma = 0;


for i in range(3):
	for k in range(3):
		soma = 0;
		for j in range(3):
			soma = soma + (mtz1[i][j]  * mtz2[j][k])
		mtz3[i][k] = soma

print(mtz1.dot(mtz2) )
print("\n")
print(mtz3)