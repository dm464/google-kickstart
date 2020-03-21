import math
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
t = int(input())  # read a line with a single integer

def mostBeauty(n, scoreList): 
    result = 0
    size = math.ceil(len(scoreList)/2)

    for i in range(size):
        result += scoreList[i]
  
    next_sum = result
    for i in range(size, n):
        next_sum += scoreList[i] - scoreList[i-size] 
        result = max(result, next_sum) 
    return result

for i in range(1, t + 1):
    n = int(input())
    scoreList = [int(v) for v in input()]
    result = mostBeauty(n, scoreList)
    print("Case #{}: {}".format(i, result))
    # check out .format's specification for more formatting options