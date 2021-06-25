# def key_lock(a,b):
#     import numpy as np
#     import random
#     import warnings
#     warnings.filterwarnings(action='ignore')
#
#     a=int()
#     b=int()
#
#     lock = np.zeros([a,a])
#
#     for i in range(0,a):
#         for j in range(0,a):
#             lock[i,j]=random.randint(0,1)
#
#     key = np.zeros([b,b])
#
#     for i in range(0,b):
#         for j in range(0,b):
#             key[i,j]=random.randint(0,1)
#
#
#     if a>=3 and b>=3:
#         key0 = np.zeros([a+2*b-2, a+2*b-2])
#         key0[a-1:a+b-1, a-1:a+b-1] = key
#         key90 = np.rot90(key0)
#         key180 = np.rot90(key0, 2)
#         key270 = np.rot90(key0, 3)
#
#     print(key)
#     print(lock)
#
#
#     list=[]
#     for i in range(0,a):
#         for j in range(0,a):
#             list.append(key0[i:i + 3, j:j + 3])  ##모든 경우의 수를 다 하기 위함.
#             list.append(key90[i:i + 3, j: j + 3])
#             list.append(key180[i:i + 3, j:j + 3])
#             list.append(key270[i:i + 3, j:j + 3])
#
#     for i in range(0,len(list)):
#         solve=list[i]+lock
#
#         if np.sum(solve)==9 and solve.all()==1:
#         # print('true')
#         # print(a[i])
#             list.append('true')
#
#     if list[-1]=='true':
#         print('true')
#     else:
#         print('false')
#
#
# key_lock(3,3)
#

# def check_match(lock, key):
#     for i in range(len(lock)):
#         for j in range(len(lock)):
#             if lock[i][j] + key[i][j] != 1:
#                 return False
#     return True
#
#
# def solution(key, lock):
#     answer = True
#     m = len(key[0])
#     n = len(lock[0])
#
#     new_key_0 = [[0] * n for _ in range(n)]
#     new_key_1 = [[0] * n for _ in range(n)]
#     new_key_2 = [[0] * n for _ in range(n)]
#     new_key_3 = [[0] * n for _ in range(n)]
#     for i in range(m):
#         for j in range(m):
#             new_key_0[i][j] = key[i][j]
#             new_key_1[j][m-i-1] = key[i][j]
#             new_key_2[m-i-1][m-j-1] = key[i][j]
#             new_key_3[m-j-1][i] = key[i][j]
#
#     for key in [new_key_0, new_key_1, new_key_2, new_key_3]:
#         for i in range(n):
#             for j in range(n):
#                 left_up_key = [row[i:] + [0]*i for row in key[j:]] + [[0]*n]*j
#                 if check_match(lock, left_up_key):
#                     return True
#                 left_down_key = [[0]*n]*(n-j-1) + [row[i:] + [0]*i for row in key[:j+1]]
#                 if check_match(lock, left_down_key):
#                     return True
#                 right_up_key = [[0]*i + row[:n-i] for row in key[j:]] + [[0]*n]*j
#                 if check_match(lock, right_up_key):
#                     return True
#                 right_down_key = [[0]*n]*(n-j-1) + [[0]*i + row[:n-i] for row in key[:j+1]]
#                 if check_match(lock, right_down_key):
#                     return True
#     return False
#


# def solution(key, lock):

#
#
# key = np.zeros([3,3])
#
# for i in range(0,3):
#     for j in range(0,3):
#         key[i,j]=random.randint(0,1)
#
#
# lock = np.zeros([3,3])
#
# for i in range(0,3):
#     for j in range(0,3):
#         lock[i,j]=random.randint(0,1)
#
# # data test code
# # key=np.array([[0,0,0],[1,0,0],[0,1,1]])
# # lock=np.array([[1,1,1],[1,1,0],[1,0,1]])
#
# key0 = np.zeros([7,7])
# key0[2:5,2:5]=key
# key90=np.rot90(key0)
# key180=np.rot90(key0,2)
# key270=np.rot90(key0,3)
#
# a=[]
# for i in range(0,5):
#     for j in range(0,5):
#         a.append(key0[i:i + 3, j:j + 3])##모든 경우의 수를 다 하기 위함.
#         a.append(key90[i:i + 3, j: j + 3])
#         a.append(key180[i:i + 3, j:j + 3])
#         a.append(key270[i:i + 3, j:j + 3])
#
# # print(a)
# # print(len(a))
#
#
# for i in range(0,len(a)):
#     solve=a[i]+lock
#
#     if np.sum(solve)==9 and solve.all()==1:
#         # print('true')
#         # print(a[i])
#         a.append('true')
#
# # print(a)
#
# if a[-1]=='true':
#     print('true')
# else:
#     print('false')
#