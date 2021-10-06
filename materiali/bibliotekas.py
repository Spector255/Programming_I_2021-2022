#pypi.org
#y=x**2
import matplotlib.pyplot as plt
import numpy as np

x = list(range(-10,11))
y = [i**2 for i in x]

fig, ax = plt.subplots()
ax.plot(x, y, color = "green", linewidth = "5")

#ax.set(xlabel = 'X', ylabel = 'X**2', title = 'X**2')
plt.title("X**2")
ax.grid()

#fig.savefig("test.png")
plt.show()