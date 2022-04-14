# 배열의 크기 N, 숫자가 더해지는 횟수 M, 연속할 수 있는 횟수 K

# 연속할 수 있도록 하는 횟수에서 가장 큰 수를 출력할 수 있는 방법 => 큰 수의 법칙

N, M, K = map(int, input().split())

# 어떻게 배열의 갯수를 N으로 제한받지?
arr = list(map(int, input().split()))
# arr = list(int(x) for x in input().split())
sum = 0

arr.sort() # 오름차순 정렬
print(arr)
first = arr[N-1]
second = arr[N-2]
print(first, second)
count = 0

if first == second:
    sum += (first * M)
    print(sum)
else: # k만큼씩 더하는 프로세스
    while M >= K:
        if count % 2 == 0:
            sum += (first * K)
            count += 1
            M -= K
        else:
            sum += second
            count += 1
            M -= 1

    if M == 0:
        print(sum)
    else:
        while(M != 0):
            if count % 2 == 0:
                sum += first
                M -= 1
            else:
                sum += second
                M -= 1
                count += 1
    print(sum)
    