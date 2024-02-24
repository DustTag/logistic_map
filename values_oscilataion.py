import numpy as np
import matplotlib.pyplot as plt

reps = 80
r = 2.8  # The reproduction parameter
lims = np.zeros(reps)  # The Values of Xn

fig, ax = plt.subplots()
lims[0] = np.random.rand()
for i in range(reps - 1):
    lims[i + 1] = r * lims[i] * (1 - lims[i])
x = np.arange(reps)
ax.plot(x, lims, "k", markersize=0.1)

ax.set(xlabel=r'$N$', ylabel=r'$X[N]$', title=r'$Amplitude\:of\:the\:Logistic\:map$')
ax.grid(which="major")
ax.minorticks_on()
ax.grid(which="minor", linestyle=":")
ax.set_xlim(0, reps)
ax.set_ylim(0, 1)
plt.show()
