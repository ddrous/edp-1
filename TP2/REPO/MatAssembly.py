from GmeshRead import *
from BaseP1 import *
import numpy as np
import numpy.linalg as nplin
import scipy as sp
import scipy.sparse as spsp
import scipy.sparse.linalg as spsplin
import scipy.stats as spst
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Poisson:

    def __init__(self, mesh, f):
        self.Mh = mesh
        self.f = f
        self.Ndof = self.Mh.Nnodes
        self.A = spsp.dok_matrix((self.Ndof, self.Ndof), dtype=np.float64)
        self.rhs = np.zeros(self.Ndof, dtype=np.float64)
        self.u = np.zeros(self.Ndof, dtype=np.float64)

        self.uexact = u_exact
        self.grad_uexact = grad_u_exact


    def compute_nabla(self, el):
        # nabla_TK_transposee = B tel que TK(x_hat) = B@x_hat + b

        # Deux vecteurs de la base de ref K_hat
        u_1 = a_2 - a_1         # a_1, a_2, a_3 definis dans le fichier BaseP1.py
        u_2 = a_3 - a_1
        B_ref = np.stack((u_1, u_2), axis=1)  

        # 3 points et 2 vecteurs de la base locale K
        A = self.Mh.connect[el, 0]
        B = self.Mh.connect[el, 1]
        C = self.Mh.connect[el, 2]
        v_1 = self.Mh.Nodes[B] - self.Mh.Nodes[A]
        v_2 = self.Mh.Nodes[C] - self.Mh.Nodes[A]
        B_local = np.stack((v_1, v_2), axis=1) 

        # B = B_local @ B_ref_moins_1
        B = B_local @ nplin.inv(B_ref)

        return abs(nplin.det(B)), nplin.inv(B.T)


    def assemble_matrix(self):
        pts, wght, psi, derpsi = base_psiref()
        # Boucle sur les elements
        for el in range(self.Mh.Nel):
            # B telle que x = T_K(x_hat) = B @ x_hat + b, voir masterpde.pdf page 32
            detTK, B_moins_T = self.compute_nabla(el)
            # Boucle sur les points de quadrature
            for q in range(len(wght)):
                # Boucle sur les fonctions de forme
                for ni in range(3):
                    i = self.Mh.connect[el, ni]                         # i -> inode
                    for nj in range(3):
                        j = self.Mh.connect[el, nj]                     # j -> jnode
                        derpsi_i = B_moins_T @ derpsi[ni, q]
                        derpsi_j = B_moins_T @ derpsi[nj, q]
                        self.A[i, j] += detTK * wght[q] * derpsi_i @ derpsi_j
                        # Noeud du bord -> Dirchlet
                        if self.Mh.label[i] < 2:        # dim = 0, 1 sur les bords
                            self.A[i, :] = 0 
                            self.A[i, i] = 1
        

    def assemble_rhs(self):
        pts, wght, psi, derpsi = base_psiref()
        # Boucle sur les elements
        for el in range(self.Mh.Nel):
            detTK, B_moins_T = self.compute_nabla(el)
            # Boucle sur les points de quadrature
            for q in range(len(wght)):
                # Boucle sur les fonctions d'interpolation
                for ni in range(3):
                    i = self.Mh.connect[el, ni]                     # i -> inode
                    x_q, y_q = coord(pts[q])
                    
                    f_i = self.f(x_q, y_q)
                    psi_i = psi[ni, q]
                    self.rhs[i] += detTK * wght[q] * f_i * psi_i
                    # Noeud du bord -> Dirchlet
                    if self.Mh.label[i] < 2: 
                        self.rhs[i] = 0 


    def plot_sol(self):
        x = self.Mh.Nodes[:, 0]
        y = self.Mh.Nodes[:, 1]
        fig = plt.figure()
        ax=fig.add_subplot(1,1,1, projection='3d')
        surf = ax.plot_trisurf(x, y, self.u, linewidth=0.2, antialiased=True, cmap=plt.cm.CMRmap)
        fig.colorbar(surf, shrink=0.5, aspect=5)
        plt.show()

    # Pour faire le graphe de la solution exacte
    def plot_sol_exact(self):
        x = np.linspace(-1, 1, 1000)
        y = np.linspace(-1, 1, 1000)
        xx, yy = np.meshgrid(x, y)

        xx = xx.flatten()
        yy = yy.flatten()

        xx_2 = xx[xx**2 + yy**2 <= 1]
        yy_2 = yy[xx**2 + yy**2 <= 1]
        xx = xx_2
        yy = yy_2

        fig = plt.figure()
        ax=fig.add_subplot(1,1,1, projection='3d')
        surf = ax.plot_trisurf(xx, yy, self.uexact(xx, yy), linewidth=0.2, antialiased=True, cmap=plt.cm.CMRmap)
        fig.colorbar(surf, shrink=0.5, aspect=5)
        plt.show()

    def solve(self, plot = False):
        self.u = nplin.solve(self.A.todense(), self.rhs)
        # self.u = spsplin.cg(self.A, self.rhs)
        if(plot): 
            self.plot_sol()


    def compute(self):
        self.normeL2 = 0
        semi_normeH1 = 0
        pts, wght, psi, derpsi = base_psiref()

        for el in range(self.Mh.Nel):
            detTK, B_moins_T = self.compute_nabla(el)
            ## B = nplin.inv(B_moins_T.T)          # Il nous faut b en plus
            for q in range(len(wght)):
                for ni in range(3):
                    """ 1ere methode: On connait le gradient de u_exaxt ==> NE MARCHE PAS! """
                    # i = self.Mh.connect[el, ni]                     # i -> inode
                    # x_q, y_q = coord(pts[q])                    # Coord x_K,q
                    # # Norme L2
                    # uexact_i = self.uexact(x_q, y_q)        # _i ==> contribution pour le noeud i
                    # uh_i = self.u[i] * psi[ni, q]
                    # self.normeL2 += detTK * wght[q] * (uexact_i-uh_i)**2
                    # # Semi-norme H1
                    # grad_uexact_i = B_moins_T @ self.grad_uexact(x_q, y_q)
                    # grad_uh_i = B_moins_T @ (self.u[i] * derpsi[ni, q])
                    # semi_normeH1 += detTK * wght[q] * nplin.norm(grad_uexact_i-grad_uh_i)**2

                    # # print("ue[i] =", self.uexact(x_q, y_q), "\tuh[i] =", self.u[i] * psi[ni, q])
                    # # print("gradue[i] =", np.array(self.grad_uexact(x_q, y_q)), "\tgraduh[i] =", self.u[i] * derpsi[ni, q])

                    """ 2eme methode: On interpole tout ==> MARCHE ! """
                    i = self.Mh.connect[el, ni] 
                    # x_i, y_i = B @ coord(pts[ni]) + b                  # Il faut calculer le b
                    x_i, y_i = self.Mh.Nodes[i, 0], self.Mh.Nodes[i, 1]
                    # Norme L2
                    uexact_i = self.uexact(x_i, y_i) * psi[ni, q]
                    uh_i = self.u[i] * psi[ni, q]
                    self.normeL2 += detTK * wght[q] * (uexact_i-uh_i)**2
                    # Semi-norme H1
                    grad_uexact_i = B_moins_T @ (self.uexact(x_i, y_i) * derpsi[ni, q])
                    grad_uh_i = B_moins_T @ (self.u[i] * derpsi[ni, q])
                    semi_normeH1 += detTK * wght[q] * nplin.norm(grad_uexact_i-grad_uh_i)**2

                    # print("ue[i] =", self.uexact(x_i, y_i), "\tuh[i] =", self.u[i])
                    # print("gradue[i] =", self.uexact(x_i, y_i) * derpsi[ni, q], "\tgraduh[i] =", self.u[i] * derpsi[ni, q])

        self.normeH1 = np.sqrt(self.normeL2 + semi_normeH1)
        self.normeL2 = np.sqrt(self.normeL2)

def f(x, y):
    return 1;

def u_exact(x, y):
    return (1 - x**2 - y**2)/4

def grad_u_exact(x, y):
    return -x/2, -y/2


if __name__ == '__main__':

    # mesh = mesh2d("./maillage/triangle.msh")
    mesh = mesh2d("./maillage/new_disque.msh")
    probleme = Poisson(mesh, f)

    probleme.assemble_matrix()
    # print(probleme.A)

    probleme.assemble_rhs()
    # print(probleme.rhs)

    probleme.solve(plot=False)
    # print(probleme.u)

    # probleme.plot_sol_exact()

    probleme.compute()
    print("diametre h = %.6f"%probleme.Mh.h)
    print("norme L2 = %.6f"%probleme.normeL2)
    print("norme H1 = %.6f"%probleme.normeH1)

    # Etude de convergence
    h_gmsh = [0.4, 0.2, 0.1, 0.05, 0.025]
    h = [0.514280, 0.250224, 0.131696, 0.070653, 0.036613]
    L2 = [0.003339, 0.000889, 0.000212, 0.000057, 0.000014]
    H1 = [0.030875, 0.015594, 0.007267, 0.003686, 0.001825]
    penteL2 = spst.linregress(np.log10(h), np.log10(L2))
    penteH1 = spst.linregress(np.log10(h), np.log10(H1))
    plt.style.use("seaborn")
    plt.loglog(h, L2, "bo-", label = "Pente L2 = %.3f"%penteL2.slope)
    plt.loglog(h, H1, "ro-", label = "Pente H1 = %.3f"%penteH1.slope)
    plt.xticks([10**(-1.5), 10**(-1), 10**(-0.5)], ["$10^{-1.5}$", "$10^{-1}$", "$10^{-0.5}$"])
    plt.xlabel("h")
    plt.ylabel("$\Vert u - u_h \Vert$")
    plt.legend()
    plt.show()
