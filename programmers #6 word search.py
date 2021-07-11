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
## 밑의 구분은 접두사로 ?가 나왔을 때를 상정한다.
que_pos={}
for query in queries:
    left=0
    right=len(query)-1
    if query.index('?')==0:
        while left <= right:
            mid = (left + right) // 2
            if query[mid] == '?' and query[mid + 1] != '?':
                break
            elif query[mid] == '?':
                left = mid
            elif query[mid] != '?':
                right = mid
        que_pos[query]=0,mid+1,len(query)
    else:
        que_pos[query]=query.index('?') , len(query) ,len(query)

print(que_pos)
print(words)
"""
['frame', 'frodo', 'front', 'frost', 'frozen', 'kakao']
question_position 딕셔너리에
첫번째 ? 위치,
두번째 ? 위치,
단어의 총 길이를 모두 입력해두었다.
else 부분이 효율성 테스트에서 떨어지는 탐색방법이라면, 이 부분을 고쳐야할 수도 있다.
"""
result=[]
for key, value in que_pos.items():
    t=key[value[0]:value[1]]
    key=key.replace(t,"")
    result.append(key)

print(result)

# for word in words:

"""
result
[3, 2, 4, 1, 0]
글자의 길이와 글자의 포지션과의 관계를 모두 정립한다면 쉽게 찾아낼 수 있을거 같음.

접미형일 경우 value[0]!=0:
0:value[0] 까지가 key값과 일치하는 것 and len(word)==value[2]:

접두형일 경우 접두형 ==> value[0]==0:
value[1]:value[2]의 값이 일치하고 len(word)==value[2]와 일치.

"""


