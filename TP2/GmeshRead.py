import numpy as np


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

        line = f.readline()
        while line.find("$EndNodes") < 0:
            splitline = line.split()
            nb = int(splitline[-1])
            dim = int(splitline[1])

            for i in range(nb):
                splitline = f.readline().split()
                tag = int(splitline[0]) - 1
                x = float(splitline[1])
                y = float(splitline[2])
                z = float(splitline[3])

                self.Nodes[tag, 0], self.Nodes[tag, 1] = x, y
                self.label[tag] = dim

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
                    pass
                    # à compléter


            else:
                for i in range(nb): f.readline()

            line = f.readline()


if __name__ == '__main__':
    mesh2d("./maillage/carre.msh")


