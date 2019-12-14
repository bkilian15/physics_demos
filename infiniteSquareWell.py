import numpy
import matplotlib.pyplot as plt

# This is the first script

nPoints = 100
x = numpy.linspace(0, 7, num=nPoints)
y = numpy.sin(x)


plt.plot(x, y)
plt.show()
