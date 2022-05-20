# d(n) = n + n//10 + n%10
# n은 d(n)의 생성자이다.

def d(n): # 10 100 1000 자리별로 구별이 필요할 것이다.
  if n < 10: return n + n
  elif n < 100: return n + n//10 + n%10
  elif n < 1000: return n + n//100 + (n//10)%10 + n%10
  else: return n + n//1000 + (n//100)%10 + (n//10)%10 + n%10   
# return n + n//10 + n%10
# n>0 : n%10 => n/10

# 10000보다 작거나 같은 셀프 넘버를 한줄에 하나씩 출력하는 프로그램
a = [i for i in range(1, 10001)]
for i in range(10001):
    if d(i) in a:
        a.remove(d(i))

for j  in range(len(a)):
    print(a[j])

