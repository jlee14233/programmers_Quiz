
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


matrix_sizes= [[5,10],[10,8],[8,8],[8,4]] #,[4,3],[3,9],[9,3],[3,2],[2,6],[6,4]

import math
# print(len(matrix_sizes))

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
x=[1,2,3,4]
d=[]
for i in matrix_sizes:
    d.append(i[0])
d.append(matrix_sizes[-1][1])
print(d) # 값의 모음을 저장했음
"""
순서가 들어갈 때 1,2 -> 2,3 -> 1,3 이렇게 진행되어야 정상적으로 구동된다.
즉, 4개가 된다면
1,2 2,3 3,4 -> 1,3, 2,4 -> 1,4
12 23 34 -> 13 24 -> 14
i i+1
j 4 일 경우
for i in range(1,3):
    j=4
    end=i+1
    ad=1
    if end==j:
         ad+=1
    for k in range(1,j):
        table[i][i+ad]=min(table[i][k]+m[k+1][i+ad]+d[i-1]*d[k]*d[i+ad])

"""
min_table=[]
for i in range(len(matrix_sizes)-1):
    print(i)
    j=len(matrix_sizes)
    end=i+1
    ad=1
    for k in range(0,3):
        min_table.append(table[i][k]+table[k+1][i+ad]+d[i-1]*d[k]*d[i+ad])
        print(min_table)
    table[i][i+ad]=min(min_table)
    min_table = []
    if end==j:
        ad+=1
        break
print(ad)

    # print(table)
print(min_table)
print(table)

# [[0, 200, inf, inf],
#  [inf, 0, 400, inf],
#  [inf, inf, 0, 640],
#  [inf, inf, inf, 0]]
