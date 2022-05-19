
N = int(input())
m = [int(input()) for i in range(N)]

m.sort(reverse=False)
for i in range(N):
    print(m[i])