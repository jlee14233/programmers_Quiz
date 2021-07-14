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

#
words=["fr", "front", "frost", "frozen", "frame", "kakao"]
queries=["fr???", "????o",  "fr???","fr???",
         "?????","pro?",
         "?????","pro?","?????","pro?","fr???"]
# words = ["fr", "frozz", "frozz", "frozen", "frame", "kakao"]
# queries = ["fro??"]

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

## 전부가 ? 일 경우에 제대로 찾지 못하는 현상이 있기 때문에 실패로 뜨는듯.
## 밑의 구분은 접두사로 ?가 나왔을 때를 상정한다.
## 모든 문자가 존재할 때도, 쿼리를 찾을 수 없기에 실패로 나옴.
que_pos={}
"""
쿼리에 중복이 있을 경우를 생각을 하지 않았음.
중복된 쿼리가 있을 경우 이를 어떻게 분리할지를 생각해야함.
쿼리에 중복검사가 필요하고, 중복검사되는 첫번째 항목과 두번째 항목, 그 이후의 항목을 모두 저장해야함.
"""

cnt=[i for i in queries if queries.count(i)>=2]
cnt=list(set(cnt))
dup_dic ={ cnt[i]:[] for i in range(0,len(cnt))}
for i in range(0,len(queries)):
    if queries[i] in dup_dic.keys():
        dup_dic[queries[i]].append(i)

"""
cnt 0 번-> 1 2 3 
cnt 1 -> 4,6,8
cnt 2 -> 5,7,9
for i in range(0,len(queries):
    if queries[i]==dup_dic.keys()
        dup_dic[queries[i]].append(i) 
"""

for query in queries:
    left = 0
    right = len(query)-1
    if '?' not in query:
        que_pos[query] = len(query), len(query), len(query)
    elif query.index('?') == 0 and query[-1] != '?':
        while left <= right:
            mid = (left + right) // 2
            if query[mid] == '?' and query[mid + 1] != '?':
                break
            elif query[mid] == '?':
                left = mid
            elif query[mid] != '?':
                right = mid
        que_pos[query] = 0, mid + 1, len(query)
    elif query.index('?') == 0 and query[-1] == '?':
        que_pos[query] = query.index('?'), len(query), len(query)
    else:
        que_pos[query] = query.index('?'), len(query), len(query)

# print(que_pos)
# print(words)

"""
['frame', 'frodo', 'front', 'frost', 'frozen', 'kakao']
question_position 딕셔너리에
첫번째 ? 위치,
두번째 ? 위치,
단어의 총 길이를 모두 입력해두었다.
else 부분이 효율성 테스트에서 떨어지는 탐색방법이라면, 이 부분을 고쳐야할 수도 있다.
"""
print(queries)
result=[]
for key, value in que_pos.items():
    count=0
    t=key[value[0]:value[1]]
    new_key=key.replace(t,"")
    if value[0]!=0:
        for word in words:
            if word[:value[0]]==new_key and len(word)==value[2]:
                count+=1
    else:
        for word in words:
            if word[value[1]:value[2]]==new_key and len(word)==value[2]:
                count+=1
    result.append(count)



print(dup_dic)
"""
위에서 중복처리를 해줘야 할지,
아니면 밑에서 따로 처리를 해야할지 고민해봐야할 문제임
dup_dic으로 해당 중복 items의 이름과, 위치를 모두 담아놓을 수 있었음.

"""
for key, value in dup_dic.items():
    print(value)
print(result)
"""
result
[3, 2, 4, 1, 0]
글자의 길이와 글자의 포지션과의 관계를 모두 정립한다면 쉽게 찾아낼 수 있을거 같음.

접미형일 경우 value[0]!=0:
0:value[0] 까지가 key값과 일치하는 것 and len(word)==value[2]:

접두형일 경우 접두형 ==> value[0]==0:
value[1]:value[2]의 값이 일치하고 len(word)==value[2]와 일치.

"""

def solution(words, queries):
    words.sort()
    que_pos = {}
    for query in queries:
        left = 0
        right = len(query) - 1
        # if '?' not in query:
        #     que_pos[query] = len(query), len(query), len(query)
        if query.index('?') == 0 and query[-1] != '?':
            while left <= right:
                mid = (left + right) // 2
                if query[mid] == '?' and query[mid + 1] != '?':
                    break
                elif query[mid] == '?':
                    left = mid
                elif query[mid] != '?':
                    right = mid
            # print(mid)
            que_pos[query] = 0, mid + 1, len(query)
        elif query.index('?') == 0 and query[-1] == '?':
            que_pos[query] = query.index('?'), len(query), len(query)
        else:
            que_pos[query] = query.index('?'), len(query), len(query)

    result = []
    for key, value in que_pos.items():
        count = 0
        t = key[value[0]:value[1]]
        new_key = key.replace(t, "")
        if value[0] != 0:
            for word in words:
                if word[:value[0]] == new_key and len(word) == value[2]:
                    count += 1
        else:
            for word in words:
                if word[value[1]:value[2]] == new_key and len(word) == value[2]:
                    count += 1

        result.append(count)

    return result

print(solution(words,queries))