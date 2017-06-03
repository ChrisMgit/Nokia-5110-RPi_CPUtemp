import numpy as np

a = np.array([10, 24, 94])
b = np.array([23, 5, 21])
c = np.array([1 +1j, 2 - 4j, 3 + 2j])
d = a + (b*c)
dconj = np.conjugate(d)
ddc = (d * dconj)
print(d)
print(dconj)
print(' ')
print("d*dconj = %s " % ddc)