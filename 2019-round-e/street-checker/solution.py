import sys
import math

t = int(input())

def getDivisor(n):
    result = []
    i = 1
    while i <= math.sqrt(n): 
        if (n % i == 0) : 
            if (n / i == i) : 
                result.append(i)
            else : 
                result.append(i)
                result.append(n/i)
        i = i + 1
    return result

for case in range(1, t + 1):
    l, r = [int(i) for i in input().split(" ")]
    interesting = 0
    for x in range(l, r+1):
        aliceCnt = 0
        bobCnt = 0
        divisors = getDivisor(x+1)
        for divisor in divisors:
            if divisor % 2 == 0:
                aliceCnt += 1
            else:
                bobCnt += 1
        if abs(aliceCnt - bobCnt) <= 2:
            interesting += 1

    print("Case #{}: {}".format(case, interesting))