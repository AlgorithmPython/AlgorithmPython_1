# input: 1 ~ 1000 중 N 한수의 범위를 주어지고
# output: 1 ~ N 범위에 해당하는 한수의 개수를 출력
# 숫자가 아닌 등차수열로 보기

def checking(a): # 등차수열임을 확인해준다.
    one = a//100
    two = (a//10)%10
    three = a%10
    return (one - two) == (two - three)


N = int(input())


if N < 100:
    count = N
else: # 1000은 한수가 아니므로 따로 고려할 필요가 없다.
    count = 99
    for i in range(100, N+1): 
        if checking(i):
            count += 1

print(count)
