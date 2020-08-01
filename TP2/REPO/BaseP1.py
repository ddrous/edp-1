from GmeshRead import *
import numpy as np
np.set_printoptions(precision = 3)

# Element de reference
a_1 = np.array([0, 0])
a_2 = np.array([1, 0])
a_3 = np.array([0, 1])

# Aire totale du traingle de reference
u = a_2 - a_1
v = a_3 - a_1
area_ref = abs(u[0]*v[1] - u[1]*v[0]) / 2

# Fonctions de base et leur derivees
def psi_1(x, y):
    return 1-(x+y)
def derpsi_1(x, y):
    return -1, -1

def psi_2(x, y):
    return x
def derpsi_2(x, y):
    return 1, 0

def psi_3(x, y):
    return y
def derpsi_3(x, y):
    return 0, 1

# Convertit les coordonnes barycentriques en coordonnes cartesiennes
def coord(ld):
    return ld[0]*a_1 + ld[1]*a_2 + ld[2]*a_3

# Permet	d’effectuer	les	quadratures	sur	l’élément de référence.
def base_psiref():
    pts = np.zeros((7, 3), dtype=float) 
    wght = np.zeros((7,), dtype=float)
    psi = np.zeros((3, 7), dtype=float) 
    derpsi = np.zeros((3, 7, 2), dtype=float) 

    # Les points et leurs poids
    pts[0], wght[0] = (1, 0, 0), 1/20
    pts[1], wght[1] = (0, 1, 0), 1/20
    pts[2], wght[2] = (0, 0, 1), 1/20
    pts[3], wght[3] = (1/2, 1/2, 0), 2/15
    pts[4], wght[4] = (1/2, 0, 1/2), 2/15
    pts[5], wght[5] = (0, 1/2, 1/2), 2/15
    pts[6], wght[6] = (1/3, 1/3, 1/3), 9/20

    # Evaluation des fonctions et derivees
    for k in range(7):
        # Coordonnes du point de quadrature k
        x_k, y_k = coord(pts[k])

        psi[0, k] = psi_1(x_k, y_k)
        derpsi[0, k] = derpsi_1(x_k, y_k)

        psi[1, k] = psi_2(x_k, y_k)
        derpsi[1, k] = derpsi_2(x_k, y_k)

        psi[2, k] = psi_3(x_k, y_k)
        derpsi[2, k] = derpsi_3(x_k, y_k)
    return pts, wght*area_ref, psi, derpsi

if __name__ == '__main__':
    pts, wght, psi, derpsi = base_psiref()

    """ Verification des poids """

    def f(x, y):
        return x**2

    # Valeur exacte de l'integrale de f sur le triangle de ref
    int_f = 1/12

    # Approximation de l'integrale 
    quad_f = 0
    for k in range(7):
        x_k, y_k = coord(pts[k])
        quad_f += wght[k] * f(x_k, y_k)
    
    print("f = x^2")
    print("Valeur exacte de l'integrale:\t", "%.12f"%int_f)
    print("Quadrature de l'integrale:\t", "%.12f"%quad_f)
