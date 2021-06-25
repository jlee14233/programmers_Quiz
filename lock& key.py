
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


print(key[0][1])
a=[]
b=[]
for i in range(0,5):
    a.append(0)
for j in range(0,5):
    b.append(a)


print(b)
# b[1][1]=key[0][0]
# b[1][2]=key[0][1]
# b[1][3]=key[0][2]
# b[2][1]=key[1][0]

print(key[:][1])
for i in range(0,3):
    for j in range(0,3):
        b[i][j]=int(key[i][j])

print(b)