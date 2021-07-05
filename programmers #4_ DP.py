
"""
모든 창을 계산해야한다.
10 by 10의 창을 만들어야 하나?
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
"""


matrix_sizes= [[5,10],[10,8],[8,8],[8,4],[4,3],[3,9],[9,3],[3,2],[2,6],[6,4]]

import math
print(len(matrix_sizes))

table=[[math.inf for i in range(len(matrix_sizes))] for i in range(len(matrix_sizes))]
##table에 infinite 를 모두 넣는 함수

for i in range(len(matrix_sizes)):
    table[i][i] = 0
## 행과 열이 동일한 곳에 0으로 리셋을 넣는다.

"""
d0 = 5
d1 = 10
d2 = 8
d3 = 8

min 0(1,1 /2 3/ + 640 + 400,  0(3,3) + 400(1,2) + 320 )
[[0, 400, inf, inf, inf, inf, inf, inf, inf, inf], 
[inf, 0, 640, inf, inf, inf, inf, inf, inf, inf], 
[inf, inf, 0, inf, inf, inf, inf, inf, inf, inf], 
[inf, inf, inf, 0, inf, inf, inf, inf, inf, inf], 
[inf, inf, inf, inf, 0, inf, inf, inf, inf, inf], 
[inf, inf, inf, inf, inf, 0, inf, inf, inf, inf], 
[inf, inf, inf, inf, inf, inf, 0, inf, inf, inf], 
[inf, inf, inf, inf, inf, inf, inf, 0, inf, inf], 
[inf, inf, inf, inf, inf, inf, inf, inf, 0, inf], 
[inf, inf, inf, inf, inf, inf, inf, inf, inf, 0]]
"""
min_number= min(matrix_sizes[0][0] * matrix_sizes[2][0]*(matrix_sizes[0][1]+matrix_sizes[2][1]),
                matrix_sizes[1][0] * matrix_sizes[2][1]*(matrix_sizes[0][0]+matrix_sizes[1][1]))
"""
5 10/ 10 8 /8 8 -> 
5 * 10 * 8 + 5* 8 *8  = 5 * 8 (10 + 8)
10* 8 * 8 + 5* 10 * 8 = 10 * 8 (5 + 8)

/8 4 /4 3/ 3 9 

8 * 4 * 3 + 8 * 3 * 9   = 8 * 3 ( 4 + 9) 
4 * 3 * 9 + 8 * 4 * 9   = 4 * 9 ( 8 + 3)

a[0][0] * a[2][0] * ( a[0][1] + a[2][1] )
a[1][0] * a[2][1] * ( a[0][0] + a[1][1] )

a[0][0] * a[1][1] * ( a[0][1] + a[2][1])
a[1][0] * a[2][1] * ( a[0][0] + a[1][1])
"""
print(min_number)

"""
0,1,2에서 이렇게 된다. ( 1 2 3 ) 

"""
