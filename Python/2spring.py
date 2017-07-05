def vectorfield(w, t, p):
    x1, y1, x2, y2 = w
    m1, m2, k1, k2, L1, L2, b1, b2 = p
    f = [y1, (-b1 * y1 - k1 * (x1 - L1) + k2 * (x2 - x1 - L2))/m1, y2, (-b2 * y2 - k2 * (x2 - x1 - L2))/m2]
    return f

from scipy.integrate import odeint

m1 = 1.0
m2 = 1.5
k1 = 8.0
k2 = 40.0
L1 = 0.5
L2 = 1.0
b1 = 0.8
b2 = 0.5
x1 = 0.5
y1 = 0.0
x2 = 2.25
y2 = 0.0

abserr = 1.0e-8
relerr = 1.0e-6
stoptime = 30.0
numpoints = 200

t = [stoptime * float(i) / (numpoints - 1) for i in range(numpoints)]
p = [m1, m2, k1, k2, L1, L2, b1, b2]
w0 = [x1, y1, x2, y2]
wsol = odeint(vectorfield, w0, t, args=(p,), atol = abserr, rtol = relerr)

with open ('two_springs.dat', 'w') as f:
    for t1, w1, in zip(t, wsol):
        print >> f, t1, w1[0], w1[1], w1[2], w1[3]
