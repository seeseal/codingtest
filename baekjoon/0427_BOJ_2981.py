import sys
import math
input=sys.stdin.readline

n=int(input())

num = []
result = []
gcd=0
for i in range(n) :
    num.append(int(input()))
    if i == 1 :
        gcd = abs(num[1]-num[0])
    gcd = math.gcd(abs(num[i]-num[i-1]),gcd)


gcd_result = int(gcd ** 0.5)
for i in range(2,gcd_result+1) :
    if gcd%i== 0:
        result.append(i)
        result.append(gcd//i)
result.append(gcd)
result = list(set(result))
result.sort()
for i in result :
    print(i,end=' ')
