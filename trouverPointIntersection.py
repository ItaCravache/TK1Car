from __future__ import division

import numpy as np


##permet de trouver le point d'intersection de deux droites
# avec d = [[x1,y1],[x2,y2]]
# ou d1=np.array([[x1,y1],[x2,y2]])
def trouverIntersection(d1, d2):
	# verification si 1ere droite est verticale
	if (d1[0][0] == d1[1][0] and d2[0][0] != d2[1][0]):
		A2 = (d2[0][1] - d2[1][1]) / (d2[0][0] - d2[1][0])
		B2 = d2[0][1] - (A2 * d2[0][0])
		XA = d1[0][0]
		YA = A2 * XA + B2

	# verification si 2eme droite est verticale
	elif (d1[0][0] != d1[1][0] and d2[0][0] == d2[1][0]):
		A1 = (d1[0][1] - d1[1][1]) / (d1[0][0] - d1[1][0])
		B1 = d1[0][1] - (A1 * d1[0][0])
		XA = d2[1][0]
		YA = A1 * XA + B1

	# verification si 2 droites est verticale
	elif (d1[0][0]==d1[1][0] and d2[0][0] == d2[1][0]):
		return False

	else:
		A1 = (d1[0][1] - d1[1][1]) / (d1[0][0] - d1[1][0])
		A2 = (d2[0][1] - d2[1][1]) / (d2[0][0] - d2[1][0])
		B1 = d1[0][1] - (A1 * d1[0][0])
		B2 = d2[0][1] - (A2 * d2[0][0])
		# si les deux sont paralleles (meme coeff directeur)
		if A1 == A2:
			return False

		else:

		    XA = (B2 - B1) / (A1 - A2)
		    YA = A1 * XA + B1

	if (XA <= min(max(d1[0][0],d1[1][0]),max(d2[0][0],d2[1][0])) and XA >= max(min(d1[0][0],d1[1][0]),min(d2[0][0],d2[1][0]))) and (YA <= min(max(d1[0][1],d1[1][1]),max(d2[0][1],d2[1][1])) and YA >= max(min(d1[0][1],d1[1][1]),min(d2[0][1],d2[1][1]))) :

		return True
	else:
		return False


###################### MAIN

if __name__ == '__main__':
    d = np.array([[10, 1], [10, 50]])
    d3 = np.array([[4, 6], [10, 25]])

    A = trouverIntersection(d, d3)
    print A

# cv2.waitKey(0)
