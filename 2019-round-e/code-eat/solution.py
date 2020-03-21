import sys

t = int(input())

def canReach(slots, codeTarget, eatTarget):
    totalCode = sum(item['code'] for item in slots)
    totalEat = sum(item['eat'] for item in slots)
    if codeTarget/totalCode > 1:
        return 'N'
    if eatTarget/totalEat > 1:
        return 'N'
    if codeTarget/totalCode + eatTarget/totalEat > 1:
        return 'N'
    return 'Y'


for case in range(1, t + 1):
    d, s = [int(i) for i in input().split(" ")]
    slots = []
    days = []
    for slot in range(s):
        c, e = [int(i) for i in input().split(" ")]
        slots.append({
            "code": c,
            "eat": e,
        })

    for day in range(d):
        a, b = [int(i) for i in input().split(" ")]
        days.append(canReach(slots, a, b))

    print("Case #{}: {}".format(case, ''.join(days)))