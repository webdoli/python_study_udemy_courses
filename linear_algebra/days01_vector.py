import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

v1 = np.array([ 3, -1])
v2 = np.array([ 2, 4 ])

v3 = v1 + v2


plt.plot( [0, v1[0]], [0, v1[1]], 'b', label='v1')
plt.plot( [0, v2[0]] + v1[0], [0, v2[1]]+v1[1], 'r', label='v2')
plt.plot( [0, v3[0]], [0, v3[1]], 'k', label='v1+v2')


# plt.legend()
# plt.axis('square')
# plt.axis((-6, 6, -6, 6))
# plt.grid()
# plt.show()

max1 = np.random.randn( 4, 6 ) # 0행 부터 3행, 0열부터 5열
max2 = np.random.randn( 4, 6 )

dps = np.zeros( 6 )

for i in range( 6 ):
    dps[i] = np.dot( max1[:, i], max2[:, i])

# matrix[0 : 3] > 0행 3열의 값
# matrix[: 2] > 2번째 열 전체
# matrix[ 1:3, : ] > 1행부터 2행까지 전체 
# matrix[ :, 1:4 ] > 모든 행의 1~ 3열 전체
# matrix[ 0, : ] > 0번째 행 전체

print( dps )