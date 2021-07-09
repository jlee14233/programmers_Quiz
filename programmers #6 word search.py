"""
words
["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries
["fro??", "????o", "fr???", "fro???", "pro?"]
result
[3, 2, 4, 1, 0]


def solution(words, queries):
    answer = []
    return answer
"""


words=["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries=["fro??", "????o", "fr???", "fro???", "pro?","???ooooa","??oooooa"]

"""
아이디어 개념// 1번 쿼리를 모든 word와 비교해야함.
효율성도 같이 확인하기 때문에, 이진 탐색을 쓸 수 있는 것이 시간 단축에 도움이 될 것.
??를 찾아서 위치를 불러내야한다.
"""

words.sort()
# print(queries[0].index('?'))
# print(len(queries[0]))

"""
위를 통해서 ?첫 위치를 알 수 있다.
끝 위치를 찾는 것이 중요할 것.
접미사, 접두사, 이기 떄문에,

?가 접두 혹은 접미이므로 이진탐색을 통해서 접근한다면 빠르게 처리할 수 있을 것이라고 생각함.
접미일 경우는 위의 탐색으로 바로 해결할 수 있으므로 탐색에서 제외하는 것이 중요할 것,
"""

t=queries[6] #????o T에 대한 이진탐색을 할 것

##이진탐색
# def binary_search(arr, target, low=None, high=None):
#     low, high = low or 0, high or len(arr) - 1
#     if low > high:
#         return -1
#     mid = (low + high) // 2
#     if arr[mid] > target:
#         return binary_search(arr, target, low, mid)
#     if arr[mid] == target:
#         return mid
#     if arr[mid] < target:
#         return binary_search(arr, target, mid + 1, high)
## 접두만 신경쓰면 된다.

left=0
right=len(t)-1

while left<=right:
    mid=(left+right)//2
    if t[mid]=='?':
        print(mid)
        break
    elif t[mid-1]!='?':
        left = mid
        print('\n',left)
    elif t[mid+1]!='?':
        right = mid
        print(right)
    print(mid)

print('\n',mid)