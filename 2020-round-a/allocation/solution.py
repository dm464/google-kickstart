import sys
import math

t = int(input())

for case in range(1, t + 1):
    num, budget = [int(i) for i in input().split(" ")]
    houses = [int(i) for i in input().split(" ")]
    total = 0
    houses.sort()
    balance = budget
    for x in range(0, num):
        balance = balance - houses[x]
        if balance < 0:
            break
        total += 1

    print("Case #{}: {}".format(case, total))