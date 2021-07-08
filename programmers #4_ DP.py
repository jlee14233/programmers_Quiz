"""
d0 = 5
d1 = 10
d2 = 8
d3 = 8
d4 = 4
min 0(1,1 /2 3/ + 640 + 400,  0(3,3) + 400(1,2) + 320 )
[[0, 400, 720,  , inf, inf, inf, inf, inf, inf], 
[inf, 0, 640, 576, inf, inf, inf, inf, inf, inf], 
[inf, inf, 0, 256, inf, inf, inf, inf, inf, inf], 
[inf, inf, inf, 0, inf, inf, inf, inf, inf, inf], 
[inf, inf, inf, inf, 0, inf, inf, inf, inf, inf], 
[inf, inf, inf, inf, inf, 0, inf, inf, inf, inf], 
[inf, inf, inf, inf, inf, inf, 0, inf, inf, inf], 
[inf, inf, inf, inf, inf, inf, inf, 0, inf, inf], 
[inf, inf, inf, inf, inf, inf, inf, inf, 0, inf], 
[inf, inf, inf, inf, inf, inf, inf, inf, inf, 0]]

[[0, 400, inf, inf], 
[inf, 0, 640, inf], 
[inf, inf, 0, 256], 
[inf, inf, inf, 0]]

[[0, 400, 720, inf], 
[inf, 0, 640, 576], 
[inf, inf, 0, 256], 
[inf, inf, inf, 0]]

[[0, 400, 720, 776], 
[inf, 0, 640, 576], 
[inf, inf, 0, 256], 
[inf, inf, inf, 0]]

m[i,j] 
m(ii)= 0
n[i,k] + m[k+1,j] + di-1dkdj (공식에 대한 부분임)

0 inf  inf
inf 0  inf
inf inf 0
생각해야할 것. 
"""

matrix_sizes= [[5,10],[10,8],[8,8],[8,4],[4,3],[3,9],[9,3],[3,2],[2,6],[6,4]]

import math

table=[[math.inf for i in range(len(matrix_sizes))] for i in range(len(matrix_sizes))]

for i in range(len(matrix_sizes)):
    table[i][i] = 0


d=[]
for i in matrix_sizes:
    d.append(i[0])
d.append(matrix_sizes[-1][1])

min_table=[]
ad=1
for j in range(len(matrix_sizes)- 1):
    for i in range(len(matrix_sizes) - 1):
        end = i + ad
        if i+ad+1>len(matrix_sizes):
            break
        for k in range(len(matrix_sizes)-1):
            min_table.append(table[i][k] + table[k + 1][i + ad] + d[i] * d[k + 1] * d[i + ad + 1])
        table[i][i + ad] = min(min_table)
        min_table = []
    ad+=1

print(table[0][-1])

