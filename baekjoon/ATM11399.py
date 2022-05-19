# input: 사람의 수 N, 각 사람이 돈을 인출하는데 걸리는 시간 Pi
# output: 시간의 합의 최솟값

N = int(input())
p = list(map(int, input().split()))

p.sort() # 정렬하기
# print(p)
sum = 0
for i in range(N):
    for j in range(N - i):
        sum += p[j]

print(sum)