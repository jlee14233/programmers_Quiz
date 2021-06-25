#
# food_times=[2,2,2,4,0,0]
# k=1
# t=0
# a=[]
# b=[]
# for i in range(0,k):
#     if food_times[t%len(food_times)]>0:
#         food_times[t%len(food_times)]=food_times[t%len(food_times)]-1
#     elif food_times[t%len(food_times)]==0:
#         while food_times[t%len(food_times)]==0:
#             t=t+1
#             if food_times[t%len(food_times)]>0:
#                 food_times[t % len(food_times)] = food_times[t % len(food_times)] - 1
#                 break
#             elif sum(food_times)==0:
#                 break
#     if i>=k-2:
#         a.append(food_times.copy())
#     t+=1
#
#
#
# if k==1:
#     c=a[0]
#     d=[]
#     if sum(c) == 0:
#         pass
#     elif c:
#         for i in range(0,len(c)):
#             if c[i]!=0:
#                 d.append(i+1)
#                 print(d)
# ## 의 경우 d[1]을 표기해주면 된다.
# else:
#     c=a[1]
#     d=[]
#     print(a)
#     for i in range(0, len(a[0])):
#         j = a[0][i] - a[1][i]
#         b.append(j)
#     print(b)
#     if sum(c)==0:
#         pass
#     elif c[b.index(1):]:
#         tm=b.index(1)
#         for i in range(tm,len(c)):
#             if c[i] !=0:
#                 d.append(i+1)
#                 print(d)
#
#     if sum(c)==0:
#         pass
#     elif c[:b.index(1)]:
#         tm=b.index(1)
#         for i in range(0,tm):
#             if c[i]!=0:
#                 d.append(i+1)
#                 print(d)
# if k==1:
#     if sum(c) ==0:
#         print('-1')
#     elif c[0]==0:
#         print(d[0])
#     elif c[0]!=0:
#         print(d[1])
# else:
#     if sum(c) ==0:
#         print('-1')
#     elif c[b.index(1)]==0:
#         print(d[0])
#     elif c[b.index(1)]!=0:
#         print(d[1])
#
#

##풀긴 했지만 먼가 효율성이 떨어짐. 통과하질 못함.
def solution(food_times,k):
    t=0
    a=[]
    b=[]
    for i in range(0,k):
        if food_times[t % len(food_times)] > 0:
            food_times[t % len(food_times)] = food_times[t % len(food_times)] - 1
        elif food_times[t % len(food_times)] == 0:
            while food_times[t % len(food_times)] == 0:
                t = t + 1
                if food_times[t % len(food_times)] > 0:
                    food_times[t % len(food_times)] = food_times[t % len(food_times)] - 1
                    break
                elif sum(food_times) == 0:
                    break
        if i >= k - 2:
            a.append(food_times.copy())
        t += 1

        # print(food_times)
    if k == 1:
        c = a[0]
        d = []
        if sum(c) == 0:
            pass
        elif c:
            for i in range(0, len(c)):
                if c[i] != 0:
                    d.append(i + 1)

        if sum(c) == 0:
            return '-1'
        elif c[0] == 0:
            return d[0]
        elif c[0] != 0:
            return d[1]

    else:
        c = a[1]
        d = []
        for i in range(0, len(a[0])):
            j = a[0][i] - a[1][i]
            b.append(j)
        if sum(c) == 0:
            pass
        elif c[b.index(1):]:
            tm = b.index(1)
            for i in range(tm, len(c)):
                if c[i] != 0:
                    d.append(i + 1)
                continue
        elif c[:b.index(1)]:
            tm = b.index(1)
            for i in range(0, tm):
                if c[i] != 0:
                    d.append(i + 1)

        if sum(c) == 0:
            return '-1'
        elif c[b.index(1)] == 0:
            return d[0]
        elif c[b.index(1)] != 0:
            return d[1]


solution([3,1,25,3,2],2)
