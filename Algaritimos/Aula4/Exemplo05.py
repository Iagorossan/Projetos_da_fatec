from math import pow, sqrt

X1 = float(input('Entre com X1:'))
X2 = float(input('Entre com X2:'))
Y1 = float(input('Entre com Y1:'))
Y2 = float(input('Entre com Y2'))

DX = float(X2 - X1)
DY = float(Y2 -Y1)
Dist = sqrt(pow(DX, 2) + pow(DY, 2))
print ('Distancia', Dist)