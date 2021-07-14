"""
begin	end	          result
1	    10	 [0, 1, 1, 2, 1, 3, 1, 4, 3, 5]
2       10   [1, 1, 2, 1, 3, 1, 4, 3, 5]
3       11   [1, 2, 1, 3, 1, 4, 3, 5, 1]  11-3 (8 -> 9)
    2 3 4 5 6 7 8 9 101112 13
i 0 0 0 0 0 0 0 0 0 0 0 0
1 0 1 1 1 1 1 1 1 1 1 1 1
2 0 0 0 2 0 2 0 2 0 2 0 2
3 0 0 0 0 0 3 0 0 3 0 0 3
4 0 0 0 0 0 0 0 4 0 0 0 4
5 0 0 0 0 0 0 0 0 0 5 0 0
6 0 0 0 0 0 0 0 0 0 0 0 6

12 -> 0 1 1 2 1 3 1 4 3 2 0 6

end의 숫자/2 의 몫까지 n값을 설정하면 된다.

n=end//2 ==> 숫자 블록의 개수

result =[0]
으로 시작한다.
result에 append는 begin로 넣어준다. end의 개수까지 넣어주면 될듯?
begin = 1 -> 0 으로 시작하지만
2일 경우는 1부터 시작하게 된다.

즉 result = []에서 리셋시켜주는 것이 정확함. range (begin,end)

"""

begin=6
end=14


n=[x for x in range(2,int(end//2)+1)]
print(n)
result=[]
for i in range(0,end+1):
    result.append(1)

print(result)
for i in n:
    for k in range(i*2,end+1,i):
        result[k]=i
print(result)
# result.pop(0)
for i in range(0,begin):
    result.pop(0)
if begin == 1:
    result[0] = 0

print(result)



def solution(begin, end):
    n = [x for x in range(2, int(end // 2) + 1)]
    # print(n)
    result = []
    for i in range(0, end + 1):
        result.append(1)

    # print(result)
    for i in n:
        for k in range(i * 2, end + 1, i):
            result[k] = i
    # print(result)
    # result.pop(0)
    for i in range(0, begin):
        result.pop(0)
    if begin == 1:
        result[0] = 0

    return result




k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = list(map(lambda x: x * 2, k))
print(k)