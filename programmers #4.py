"""
최적의 행렬 곱.
동적 프로그래밍을 기초로 하고 있다.
https://velog.io/@ruby723/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%8F%99%EC%A0%81%EA%B3%84%ED%9A%8D%EB%B2%95-DP%EC%97%B0%EC%87%84%ED%96%89%EB%A0%AC%EA%B3%B1%EC%85%88
가장 쉽게 설명되어 있는 것 같으니 이걸 바탕으로 다시 해보기.

"""



"""
4 3/ 3 10/ 10 6/ 6 2 /2 10
4 3 / 3 6 / 6 2 / 2 10
4 3 / 3 2/ 2 10
4 3 / 3 10
60
120
180회

24 
4 2 /2 10
80

단순히 생각해서 겹치는 숫자가 가장 큰 것부터 곱셈을 시킨다.
0-0 -1 -1 의 숫자에 가칸 큰 숫자가 존재한다면 가장 마지막에 곱한다.

큰 숫자가 존재하는 넘버를 찾고, 이를 계속 반복한다.
"""
matrix_sizes= [[5,10],[10,8],[8,8],[8,4],[4,3],[3,9],[9,3],[3,2],[2,6],[6,4]]
"""
"#5 10 / 10 8 /8 8/ 8 4/ 4 3 /3 9 /9 3 / 3 2 /2 6 / 6 4
5 8 / 8 8 / 8 4 / 4 3/ 3 9 /9 3 /3 2 / 2 6 /6 4   400
5 8 / 8 8 / 8 4 / 4 3/ 3 3 /3 2 / 2 6 /6 4  481
5 8 / 8 4 / 4 3/ 3 3 /3 2 / 2 6 /6 4    701
5 4 / 4 3 / 3 3 / 3 2 / 2 6 / 6 4   861
5 4 / 4 3 / 3 3 / 3 2 / 2 4       909

3개를 비교하고, 가장 작은 숫자를 남겨둠.
모든 항목에 대해서
분할을 시작할거고.
더했을 때 가장 낮은 숫자를 남겨두는 방식으로 최적값을 구할 수 있다는 것이 포인트.

5 10 10 8 8 8
(5 10 /10 8) 8 8-> 5 8 8 8 400 + 160 
5 10 / (10 8 / 8 8) -> 5 10 10 8  640 + 400 1040
에서 앞 부분을 택한다 라는 느낌인듯

이 둘을 비교하고 가장 작은 수를 계속해서 남겨두는 형식으로 진행

3개짜리 계산 
2x2

"""


sumvalue=0
# a=[i[0] for i in matrix_size if i[0]>0]
# b=[i[1] for i in matrix_size if i[1]>0]
# print(a[1:])
# print(b[:-1])
# print(a,'\n',b)
# t=max(a)
# place=a[1:].index(t)
# print(place)
# a=matrix_size[place][0]
# b=matrix_size[place][1]
# c=matrix_size[place+1][1]
# sumvalue=sumvalue+(a*b*c)
# print(a,b,c)
# print(sumvalue)
# matrix_size.pop(place)
# matrix_size[place]=[a,c]
# print(matrix_size)

# sumvalue=0
# while len(matrix_size)!=1:
#     A=[i[0] for i in matrix_size if i[0]>0]
#     B=[i[1] for i in matrix_size if i[1]>0]
#     t=max(A[1:])
#     place=A[1:].index(t)
#     a=matrix_size[place][0]
#     b=matrix_size[place][1]
#     c=matrix_size[place+1][1]
#     sumvalue=sumvalue+(a*b*c)
#     matrix_size.pop(place)
#     matrix_size[place]=[a,c]

# def solution(matrix_sizes):
#     sumvalue = 0
#     while len(matrix_sizes) != 1:
#         A = [i[0] for i in matrix_sizes if i[0] > 0]
#         B = [i[1] for i in matrix_sizes if i[1] > 0]
#         t = max(A[1:])
#         place = A[1:].index(t)
#         a = matrix_sizes[place][0]
#         b = matrix_sizes[place][1]
#         c = matrix_sizes[place + 1][1]
#         sumvalue = sumvalue + (a * b * c)
#         matrix_sizes.pop(place)
#         matrix_sizes[place] = [a, c]
#
#     return sumvalue
#

import math


def solution(matrix_sizes):
    # table[start][end] = 인덱스 start ~ end 까지의 연산 최솟값.
    table = [[math.inf for _ in range(len(matrix_sizes))] for _ in range(len(matrix_sizes))]
    # start와 end가 동일한 경우는 연산하지 않으므로 0으로 설정.
    for idx in range(len(matrix_sizes)):
        table[idx][idx] = 0

    for gap in range(1, len(matrix_sizes)):
        for start in range(len(matrix_sizes)):
            end = start + gap
            if end >= len(matrix_sizes):
                break
            for sep in range(start, end):
                table[start][end] = min(
                    table[start][end],
                    table[start][sep] + table[sep + 1][end] + (
                                matrix_sizes[start][0] * matrix_sizes[sep][1] * matrix_sizes[end][1])
                )
    print(table)
    return table[0][-1]


print(solution(matrix_sizes))
