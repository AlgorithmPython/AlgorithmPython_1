# 1이 될때까지

# 1. N에서 1을 뺀다. 2. N을 K로 나눈다.
# 다음 과정을 통해서 1이 되는 최소 횟수를 구한다.

N, K = map(int, input().split())
count = 0

if N == 1:
    print(0)

else:
    while(N != 1):
        if N % K == 0:
            N //= K
            count += 1
        else:
            N -= 1
            count += 1

print(count)

