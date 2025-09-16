import numpy as np
import matplotlib.pyplot as plt

#non-linear graph
xDomain = [ -2, 2 ]

# opt1
resolution = .1
x = np.arange( xDomain[0], xDomain[1]+resolution, resolution )

# opt2
# [ -2, 2 )
x = np.linspace( xDomain[0], xDomain[1], 41 )

# function
y = x**2 + 3*x**3 - x**4

# plot
# plt.plot( x, y )
# plt.grid()
# plt.legend()
# plt.xlim( xDomain[0], xDomain[1] )
# plt.xlabel('x')
# plt.ylabel('y=f(x)')
# plt.show()