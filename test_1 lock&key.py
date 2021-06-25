## idea 컨셉
## 모든 방면의 것을 다 더해서 전체의 합이 9일 경우와 모든 값이 1이 되는 경우만 추려냄.
import array

# import numpy as np
# import warnings
# import random
#
# warnings.filterwarnings(action='ignore')
# ## 자물쇠와 열쇠를 생산하는 코드
# a=int(input())
# b=int(input())
# key = np.zeros([a,a])
#
# for i in range(0,a):
#     for j in range(0,a):
#         key[i,j]=random.randint(0,1)
#
# lock = np.zeros([b,b])
#
# for i in range(0,b):
#     for j in range(0,b):
#         lock[i,j]=random.randint(0,1)


#
# key0 = np.zeros([a + 2 * b - 2, a + 2 * b - 2])
# key0[b-1: b+a-1,b-1: b+a-1] = key
# key90 = np.rot90(key0)
# key180 = np.rot90(key0, 2)
# key270 = np.rot90(key0, 3)
#
# # print(key0)
# ###
# a=[]
# for i in range(0,b):
#     for j in range(0,b):
#         a.append(key0[i:i + b, j:j + b])##모든 경우의 수를 다 하기 위함.
#         a.append(key90[i:i + b, j: j + b])
#         a.append(key180[i:i + b, j:j + b])
#         a.append(key270[i:i + b, j:j + b])
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
#
#
# print(key)
# #
# print(lock)
### 총 합이 9이상이 될 경우 clear의 가능성이 보임
##

# T=key+lock


# print(key0)
# print(key90)
# print(key180)
# print(key270)
#
#
# def lock(a,b):
#     import numpy as np
#     import random
#
#     a=int(a)
#     b=int(b)
#
#     lock = np.zeros([a, b])
#
#     for i in range(0, a):
#         for j in range(0, b):
#             lock[i, j] = random.randint(0, 1)
#
#     print(lock)
#
#
# lock(3,4)
#
