import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

coefs = np.random.randn( 4 ) # 다항식 계수

x = np.linspace( -5, 5, 101 )
y = np.zeros( len(x) )

fname = '$y = '

for i,c in enumerate( coefs ):
    y += c*x**i
    fname += '+ '[int(c<0)] +f'{c:.2f}x^{i}'

plt.plot( x, y )
plt.title( fname + '$')
plt.show()
