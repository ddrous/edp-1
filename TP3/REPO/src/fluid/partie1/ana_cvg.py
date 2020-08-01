import numpy as np
import numpy.linalg as nplin
import scipy as sp
import scipy.sparse as spsp
import scipy.sparse.linalg as spsplin
import scipy.stats as spst
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Etude de convergence pour la vitesse
h_gmsh = [0.2, 0.1, 0.05, 0.025]
h = [0.238468, 0.137755, 0.0643246, 0.0309489]        # h_max

#erreur L2 de u
L2_u = [7.8290562145278304e-03, 1.0837582854864012e-03, 1.1335863767546702e-04, 1.3922594656976468e-05]

#norme H1 de u
H1_u = [3.3151543481828438e-01, 9.0118005438627441e-02, 2.1564741653554598e-02, 5.3673278563648209e-03]

# norme L2 de p
L2_p = [8.7986054727024459e-03, 2.2311587624595916e-03, 5.6451710089231127e-04, 1.4074816021665562e-04]

# y = np.array(H1_u) + np.array(L2_p)         # etude numero 1
y = np.array(L2_u)                          # etude numero 2

pentey = spst.linregress(np.log10(h), np.log10(y))
plt.style.use("seaborn")
plt.loglog(h, y, "bo-", label = "Pente = %.3f"%pentey.slope)
plt.xticks([10**(-1.5), 10**(-1), 10**(-0.5)], ["$10^{-1.5}$", "$10^{-1}$", "$10^{-0.5}$"])
plt.xlabel("$h$")
# plt.ylabel("$\Vert u - u_h \Vert_{(H^1)^d} + \Vert p - p_h \Vert_{L^2} $")
plt.ylabel("$Erreur$")
plt.legend(fontsize='xx-large')
plt.show()
