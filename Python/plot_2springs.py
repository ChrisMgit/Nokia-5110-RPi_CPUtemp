from numpy import loadtxt
from pylab import figure, plot, xlabel, grid, hold, title, savefig

t, x1, xy, x2, y2 = loadtxt('two_springs.dat', unpack=True)

figure(1, figsize=(10, 5.0))
xlabel('t'), grid(True), hold(True)

plot(t, x1, 'b', linewidth=1)
plot(t, x2, 'g', linedwidth=1)
title('Mass Displacement for the \n Couple Spring-Mass System')
