"""
## 어떤 것이 떨어진다고 가정한다.
## 위에서 떨어지는 상황을 어떻게 구현할지 생각해본다.
"""

"""

block count
for문->
zero to a
->
block finder
->
count('a')==2:
board[block] -> 0:
->
a to zero 
count +=1
:for문 끝
-> return count

직사각형의 블록에 요소를 받음
요소에서 a의 갯수가 2개일 경우 모든 요소를 0으로 리턴,
0으로 바뀔 경우 a의 값을 0으로 모두 바꿔줌.

"""
"""
                        {0,0,0,0,0,0,0,0,0,0,0},
                        {0,0,0,0,0,0,0,0,0,0,0},
                        {0,0,0,0,0,0,0,0,0,0,0},
                        {0,0,0,0,0,0,0,0,0,0,0},
                        {0,0,9,0,0,0,4,0,0,0,0},
                        {0,7,9,0,0,0,4,0,0,0,0},
                        {0,7,9,9,3,4,4,0,0,0,0},
                        {7,7,0,2,3,0,0,0,5,5,0},
                        {1,2,2,2,3,3,0,0,0,5,0},
                        {1,1,1,6,0,0,0,0,0,5,0},
                        {0,0,6,6,6,0,0,0,0,0,0}};
"""
# board=[[0, 2, 0, 0], [1, 2, 0, 4], [1, 2, 2, 4], [1, 1, 4, 4]]
board=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 9, 0, 0, 0, 4, 0, 0, 0, 0],
       [0, 7, 9, 0, 0, 0, 4, 0, 0, 0, 0],
       [0, 7, 9, 9, 3, 4, 4, 0, 0, 0, 0],
       [7, 7, 0, 2, 3, 0, 0, 0, 5, 5, 0],
       [1, 2, 2, 2, 3, 3, 0, 0, 0, 5, 0],
       [1, 1, 1, 6, 0, 0, 0, 0, 0, 5, 0],
       [0, 0, 6, 6, 6, 0, 0, 0, 0, 0, 0]]
# """
# block count
# """
# n=list(set(tuple(set(board)) for board in board))
# n=[list(n[i]) for i in range(0,len(n))]
# n=sum(n,[])
# n=list(set(n))
# lists=n.copy()
# lists.remove(0)
# # print(lists)
# # print(n)
# m=len(n)
# """
# zero to a
# """
# turn=[[i,j] for i in range(0,len(board)) for j in range(0,len(board)) if board[i][j]==0]
#
# for i in range(0,len(turn)):
#     x=turn[i][0]
#     y=turn[i][1]
#
#     if [x-1,y] not in turn and turn[i][0]>0:
#         turn.remove([x,y])
#         turn.insert(i,[0,0])
# #중복값제거까지
# turn = list(set(tuple(turn) for turn in turn))
# turn.sort()
#
# for i in turn:
#     board[i[0]][i[1]]='a'
# # print(board)
# # print(turn)
# """
# blockfinder
# """
#
# # print(lists)
# blocks={}
# # print(type(board[0][1]))
# for t in lists:
#     blockfinder=[[i,j] for i in range(0,len(board)) for j in range(0,len(board)) if board[i][j]==t]
#     blocks[t]=blockfinder
#     block=blocks[t]
#     x=[block[0] for block in block]
#     y=[block[1] for block in block]
#     blockpoint=[[i,j] for i in range(min(x),max(x)+1) for j in range(min(y),max(y)+1)]
#     blocks[t]=blockpoint
#
# print(blocks)
# print(min(blocks))
#
# """
# block remover, changer
# """
# countable=[]
# element=[]
# remove=str()
# for i in blocks:
#     for j in range(0,6):
#         case=blocks[i]
#         element.append(board[case[j][0]][case[j][1]])
#     countable.append(element)
#     element=[]
#
# for i in range(0,len(countable)):
#     if countable[i].count('a')==2:
#         remove=i+1## 2번을 찾기
#
# print(type(remove))
# if type(remove)==str():
#     t=blocks[remove]
#     for i in range(0,len(t)):
#         board[t[i][0]][t[i][1]]=0
#
#
# # if type(remove)!=str():
# #     break
#
#
# print(remove)
# ## remove 가 str로 반환된다면 count를 종료 마지막에 리셋 시켜줄 필요가 있음.
# # -> 종료시키고 count를 반환하도록 만들면 될듯.
#
#
# board=[[0 if board[i][j]=='a' else board[i][j] for j in range(0,len(board))] for i in range(0,len(board))]
#
# # print(board)
# print(board)
#
#
# """
#  [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
#  ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
#  ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
#  ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
#  ['a', 'a', 'a', 'a', 'a', 'a', 4, 'a', 'a', 'a'],
#  ['a', 'a', 'a', 'a', 'a', 4, 4, 'a', 'a', 'a'],
#  ['a', 'a', 'a', 'a', 3, 0, 4, 'a', 'a', 'a'],
#  ['a', 0, 0, 0, 3, 0, 0, 'a', 5, 5],
#  [1, 0, 0, 0, 3, 3, 0, 'a', 0, 5],
#  [1, 1, 1, 0, 0, 0, 0, 'a', 0, 5]]
# """
#
# """
# a to zero
# """
#
#


import time

def ea(board):
    n = list(set(tuple(set(board)) for board in board))
    n = [list(n[i]) for i in range(0, len(n))]
    n = sum(n, [])
    n = list(set(n))
    lists= n.copy()
    if lists.index(0)!=True:
        lists.remove(0)

    m=len(n)
    # print(m,'\n',lists)
    return m, lists

def zerotoa(board):
    turn=[[i,j] for i in range(0,len(board)) for j in range(0,len(board)) if board[i][j]==0]
    for i in range(0,len(turn)):
        x=turn[i][0]
        y=turn[i][1]

        if [x-1,y] not in turn and turn[i][0]>0:
            turn.remove([x,y])
            turn.insert(i,[0,0])
    turn = list(set(tuple(turn) for turn in turn))
    turn.sort()
    for i in turn:
        board[i[0]][i[1]] = 'a'

    # print(board)
    return board

def blockfinder(lists,board):
    blocks = {}
    for t in lists:
        blockfinder = [[i, j] for i in range(0, len(board)) for j in range(0, len(board)) if board[i][j] == t]
        blocks[t] = blockfinder
        block = blocks[t]
        x = [block[0] for block in block]
        y = [block[1] for block in block]
        blockpoint = [[i, j] for i in range(min(x), max(x) + 1) for j in range(min(y), max(y) + 1)]
        blocks[t] = blockpoint

    # print(blocks)
    return blocks

def blockremover(board,blocks,lists):
    countable = []
    element = []
    remove = str()

    for i in lists:
        for j in range(0, 6):
            case = blocks[i]
            element.append(board[case[j][0]][case[j][1]])
        countable.append(element)
        element = []
    # print(countable)
    for i in range(0, len(countable)):
        if countable[i].count('a') == 2:
            remove = lists[i]  ## 2번을 찾기
    # print(type(remove))

    if remove=='':
        pass
    elif type(remove)!=str():
        # print(remove)
        t= blocks[remove]
        # print(t)
        for i in range(0, 6):
            board[t[i][0]][t[i][1]] = 0

    # print(remove)
    return board ,remove

def atozero(board):
    T = [[0 if board[i][j] == 'a' else board[i][j] for j in range(0, len(board))] for i in range(0, len(board))]
    # print(T)
    return T


def solution(board):
    count=0
    while True:
        m,lists=ea(board)
        board=zerotoa(board)
        blocks=blockfinder(lists,board)
        board,remove=blockremover(board,blocks,lists)
        if remove=='':
            break
        elif type(remove)!=str():
            count+=1

        board=atozero(board)
        # print(count)
    return count

aa=time.time()
solution(board)
bb=time.time()

print(bb-aa)
