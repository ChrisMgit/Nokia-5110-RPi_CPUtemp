import numpy as np

a = np.array([1+2j, 3-8j, 23+2j])
print('The original array is: %s' % a)
print(' ')
aangle = np.angle(a)
print('Convert to angle (radians): %s' % aangle)
print(' ')
adeg = np.angle(a, deg=True)
print('Conver to angle (degrees): %s' % adeg)
