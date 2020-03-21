t = int(input())

def build(n, x, y, c, d, e1, e2, f):
    arrX = [x]
    arrY = [y]
    for i in range(1, n):
        arrX.append((c*arrX[i-1] + d*arrY[i-1] + e1) % f)
        arrY.append((d*arrX[i-1] + c*arrY[i-1] + e2) % f)
    return [(x+y)%f for x, y in zip(arrX, arrY)]

def allSubArrays(L):
    return [L[i:i+j] for i in range(0,len(L)) for j in range(1,len(L)-i+1)]

    
for case in range(1, t + 1):
    n, k, x, y, c, d, e1, e2, f = [int(i) for i in input().split(" ")]
    a = build(n, x, y, c, d, e1, e2, f)
    subArrList = allSubArrays(a)
    power = 0
    for i in range(1, k+1):
        for j in subArrList:
            for k in range(0, len(j)):
                power += (j[k]*((k+1)**i))
    print("Case #{}: {}".format(case, power%1000000007))