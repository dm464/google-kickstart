# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
t = int(input())  # read a line with a single integer

def bigNumber(n, blackList):
    memory = {}
    blackList.sort(key=len)
    result = 2**n
    for prefix in blackList:
        exist = False
        for i in range(1, len(prefix)):
            parent = prefix[:i]
            if parent in memory:
                exist = True
                break
        if(exist):
            continue
        memory[prefix] = True
        result -= 2**(n-len(prefix))
    return result

for i in range(1, t + 1):
    n, p = [int(i) for i in input().split(" ")]
    blackList = []
    for line in range(0, p):
        blackList.append(input())
    result = bigNumber(n, blackList)
    print("Case #{}: {}".format(i, result))
    # check out .format's specification for more formatting options