import numpy as np
import matplotlib.pyplot as plt

interval = (-2, 4)  # Values of r
accuracy = 0.0001  # Dictates the amount of points between given values of r
reps = 1000  # Number of iterations
numtoplot = 500  # Prevents clutter due to excess amount of points, improves diagram detail
xnvals = np.zeros(reps)  # Stores all values of Xn over all iterations

# Iterations of logistic map
fig, ax = plt.subplots()
xnvals[0] = np.random.rand()  # Picks initial amount of population from a Uniform distribution over [0,1)
for r in np.arange(interval[0], interval[1], accuracy):
    for i in range(reps - 1):
        xnvals[i + 1] = r * xnvals[i] * (1 - xnvals[i])
    ax.plot([r] * numtoplot, xnvals[reps - numtoplot:], "k.", markersize=0.01)

# The Bifurcation Diagram constructor
ax.set(xlabel=r'$r$', ylabel=r'$X_{n}$',
       title=r'$Logistic\:map\:Bifurcation\:diagram, \:r \in $' + f'[{interval[0]}; {interval[1]}]')
fig.tight_layout()
ax.set_aspect("equal")
ax.grid(which="major")
ax.minorticks_on()
ax.grid(which="minor", linestyle=":")
ax.set_xlim(interval[0], interval[1])
plt.show()
