import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# np.set_printoptions(precision=2)
# 1ere convergence
h = np.array([0.8, 0.4, 0.2, 0.1, 0.05, 0.025, 0.0125])
h1 = np.array([0.924785, 0.269597, 0.0778948, 0.0205284, 0.00520712, 0.00134031, 0.000336841])
l2 = np.array([0.0698802, 0.0105953, 0.00163551, 0.000217006, 2.7499e-05, 3.58227e-06, 4.53486e-07])

# 2eme convergence
# h = np.array([0.8, 0.4, 0.2, 0.1, 0.05, 0.025, 0.0125])
# h1 = np.array([0.0554432, 0.0419687, 0.0299582, 0.0188573, 0.0118874, 0.00745044, 0.00470019])
# l2 = np.array([0.003245, 0.00161767, 0.000694408, 0.000218771, 6.89007e-05, 2.15019e-05, 6.795e-06])

pente_h1, ordonne, r_value, p_value, std_err = linregress(np.log10(h), np.log10(h1))
pente_l2, ordonne, r_value, p_value, std_err = linregress(np.log10(h), np.log10(l2))

plt.figure(figsize=(10, 8))
# plt.loglog(h, h1, "o-", label="Pente H1 = "+str(pente_h1))
# plt.plot(h, h1, "o-", label="Pente H1 = "+'%0.2f'%pente_h1)
plt.loglog(h, h1, "o-", label="Pente H1 = "+'%0.2f'%pente_h1)
# plt.loglog(h, l2, "o-", label="Pente L2 = "+str(pente_l2))
# plt.plot(h, l2, "o-", label="Pente L2 = "+'%0.2f'%pente_l2)
plt.loglog(h, l2, "o-", label="Pente L2 = "+'%0.2f'%pente_l2)
# plt.xticks(ticks=h, labels=h)
plt.xlabel("h")
plt.ylabel("Erreur")
plt.legend()
plt.show()


