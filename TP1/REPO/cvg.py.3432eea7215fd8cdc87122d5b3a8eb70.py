import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# np.set_printoptions(precision=2)

h = np.array([0.8, 0.4, 0.2, 0.1, 0.05, 0.025, 0.0125])
h1 = np.array([0.924785, 0.269597, 0.0778948, 0.0205284, 0.00520712, 0.00134031, 0.000336841])
l2 = np.array([0.0698802, 0.0105953, 0.00163551, 0.000217006, 2.7499e-05, 3.58227e-06, 4.53486e-07])

pente_h1, ordonne, r_value, p_value, std_err = linregress(np.log10(h), np.log10(h1))
pente_l2, ordonne, r_value, p_value, std_err = linregress(np.log10(h), np.log10(l2))

plt.figure(figsize=(10, 8))
# plt.plot(h, h1, label="H1")
# plt.loglog(h, h1, "o-", label="Pente H1 = "+str(pente_h1))
plt.loglog(h, h1, "o-", label="Pente H1 = "+'%0.2f'%pente_h1)
# plt.plot(h, l2, label="L2")
# plt.loglog(h, l2, "o-", label="Pente L2 = "+str(pente_l2))
plt.loglog(h, l2, "o-", label="Pente L2 = "+'%0.2f'%pente_h1)
# plt.xticks(ticks=h, labels="diametre du maillage")
plt.xlabel("h")
plt.ylabel("Norme")
plt.legend()
plt.show()
