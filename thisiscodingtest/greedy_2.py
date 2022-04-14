# 숫자 카드 게임
# 최소 값이 존재하는 행을 피해서 최소 중 최대의 행을 찾고, 최소값을 출력

N, M = map(int, input().split())


# 2차원 배열의 가로길이 N
arr = [list(map(int, input().split())) for _ in range(N)]
min = [0 for i in range(N)]


for i in range(N):
    min[0] = arr[i][0]
    for j in range(1, M):
        if min[i] > arr[i][j]:
            min[i] = arr[i][j] # 최소값 찾기

tmp = min[0]

for i in range(1, N):
    if tmp < min[i]:
        tmp = min[i]

print(tmp)