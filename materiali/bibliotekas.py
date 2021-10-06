#pypi.org
#y=x**2
import matplotlib.pyplot as plt
import numpy as np

x = list(range(0,11))
y = [i**2 for i in x]
# Data for plotting

fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel='X', ylabel='X**2',
       title='X**2')
ax.grid()

#fig.savefig("test.png")
plt.show()