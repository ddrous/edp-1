import numpy as np
import numpy.linalg as nplin


class mesh2d:

    def __init__(self, filename):

        f = open(filename, "r")

        #--- Lecture des noeuds du maillage ---#
        line = f.readline()
        while line.find("$Nodes") < 0: line = f.readline()
        splitline = f.readline().split()

        self.Nnodes = int(splitline[1])
        self.Nodes = np.empty((self.Nnodes, 2), dtype=float)
        self.label = np.zeros( self.Nnodes, dtype=int)

        firstNode = True        # Souvent le 1er noeud est de tag 2, le disque par exemple

        line = f.readline()
        while line.find("$EndNodes") < 0:
            splitline = line.split()
            nb = int(splitline[-1])
            dim = int(splitline[1])

            for i in range(nb):
                splitline = f.readline().split()
                
                if firstNode == True:                   # Pour detecter le tag du tout 1er noeud
                    tag_0 = int(splitline[0])
                    firstNode = False 

                tag = int(splitline[0]) - tag_0         # on commence la numerotation des noeuds a 0
                x = float(splitline[1])
                y = float(splitline[2])
                z = float(splitline[3])

                self.Nodes[tag, 0], self.Nodes[tag, 1] = x, y
                self.label[tag] = dim               # 0 ou 1 sur le bord, 2 a l'interieur

            line = f.readline()

        # --- Lecture des éléments du maillage ---#
        while line.find("$Elements") < 0: line = f.readline()
        f.readline()

        line = f.readline()
        while line.find("$EndElements") < 0:
            splitline = line.split()
            nb = int(splitline[-1])
            dim = int(splitline[1])

            # Lecture des éléments 2D (triangle) uniquement
            if dim == 2:
                self.Nel = nb
                self.connect = np.empty((nb, 3), dtype=int)
                self.area = np.zeros(nb, dtype=float)
                self.diam = np.zeros(nb, dtype=float)

                for i in range(nb):
                    line = f.readline()
                    splitline = line.split()
                    # Remplissons le tableau connect
                    a_1 = self.connect[i, 0] = int(splitline[1]) - tag_0
                    a_2 = self.connect[i, 1] = int(splitline[2]) - tag_0
                    a_3 = self.connect[i, 2] = int(splitline[3]) - tag_0
                    # calcul du diametre
                    u = self.Nodes[a_1] - self.Nodes[a_2]       # 1er vecteur du triangle
                    v = self.Nodes[a_1] - self.Nodes[a_3]       # 2eme
                    w = self.Nodes[a_2] - self.Nodes[a_3]       # 3eme
                    self.diam[i] = max(nplin.norm(u), nplin.norm(v), nplin.norm(w))
                    # Calcul de l'aire
                    self.area[i] = abs(u[0]*v[1] - u[1]*v[0]) / 2

            else:
                for i in range(nb): f.readline()

            line = f.readline()
        self.h = np.max(self.diam)      # Diametre du maillage


if __name__ == '__main__':
   
    """ Verification avec un triangle"""
    def verification_triangle(mesh):
        u = mesh.Nodes[0] - mesh.Nodes[1]
        v = mesh.Nodes[0] - mesh.Nodes[2]
        total_area = abs(u[0]*v[1] - u[1]*v[0]) / 2
        aggregated_area = np.sum(mesh.area)
        return total_area, aggregated_area

    mesh1 = mesh2d("./maillage/triangle.msh")
    total_area, aggregated_area =  verification_triangle(mesh1)
    print("Aire du triangle:\t\t", total_area)
    print("Somme des aires des elements:\t", aggregated_area)


    """ Verification avec un disque """
    def verification_disque(mesh):
        # Le premier point est sans doute le centre
        rayon = nplin.norm(mesh.Nodes[0] - mesh.Nodes[1])/2
        total_area = np.pi*(rayon**2)
        aggregated_area = np.sum(mesh.area)
        return total_area, aggregated_area

    mesh2 = mesh2d("./maillage/new_disque.msh")
    total_area, aggregated_area =  verification_disque(mesh2)
    print("\nAire du disque:\t\t\t", total_area)          # Puisque qu'il s'agit des 3/4 du disque
    print("Somme des aires des elements:\t", aggregated_area)




