import sys

t = int(input())

for case in range(1, t + 1):
    n, p = [int(i) for i in input().split(" ")]
    arr = [int(i) for i in input().split(" ")]
    arr.sort()
    minHour = sys.maxsize
    for highest in range(p-1, n):
        players = arr[highest-p+1:highest][::-1]
        reference = arr[highest]
        hour = 0
        for restPlayer in players:
            hour += (reference - restPlayer)
        if hour <= minHour:
            minHour = hour
        if minHour == 0:
            break
    print("Case #{}: {}".format(case, minHour))