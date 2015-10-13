import math
import pylab
from matplotlib import mlab

tmin = -20.0
tmax = 20.0

dt = 0.01
tlist = mlab.frange (tmin, tmax, dt)

pylab.ion()

for a in range (50):
        ylist = [math.cos(2 * t) for t in tlist]
        xlist = [math.sin(t + a) for t in tlist]
        pylab.clf()
        pylab.plot (xlist, ylist)
        pylab.draw()

pylab.close()
