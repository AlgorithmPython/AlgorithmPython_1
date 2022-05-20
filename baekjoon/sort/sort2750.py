# input: 줄의 개수 N, 값들
# output: 오름차순된 결과
def bubble_sort(n):
    for i in range(len(n)):
        for j in range(len(n)-i-1):
            if n[j] < n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]


N = int(input())
m = [int(input()) for i in range(N)]
# print(m)
bubble_sort(m)
m.reverse()
# print(m) 
for i in range(N):
    print(m[i])