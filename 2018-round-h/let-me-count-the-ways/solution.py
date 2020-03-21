import math
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
t = int(input())  # read a line with a single integer
modAmount = 1000000007

def theWay(totalCouple, newlyCouple): 
    oldCouple = (totalCouple - newlyCouple)
    newCoupleSize = (1 * newlyCouple * 2 + 1)
    oldCoupleSize = (1 * oldCouple * 2 + 1)
    arr = [None] * oldCoupleSize
    for i in range(oldCoupleSize):
        arr[i] = [None] * newCoupleSize
    
    arr[0][0] = 0
    arr[0][1] = 0
    arr[0][2] = 0

    for i in range(3, newCoupleSize):
        arr[0][i] = newCoupleWay(i) % modAmount

    for i in range(1, oldCoupleSize):
        arr[i][0] = math.factorial(i) % modAmount
    
    for i in range(1, oldCoupleSize):
        for j in range(1, newCoupleSize):
            if i == 1 and j == 1:
                arr[i][j] = 2
            else:
                arr[i][j] = (j - j % 2) * arr[i-1][j] + i * arr[i][j-1] % modAmount

    print(arr)

    return arr[oldCouple * 2][newlyCouple * 2] % modAmount

def newCoupleWay(x):
    way = 1
    for i in range(3, x+1):
        if i % 2 == 0:
            way *= i
        else:
            way *= (i-1)
    return way

for i in range(1, t + 1):
    n, m = [int(s) for s in input().split(" ")]
    result = theWay(n, m)
    print("Case #{}: {}".format(i, result))
    # check out .format's specification for more formatting options