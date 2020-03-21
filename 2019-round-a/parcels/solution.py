import sys

t = int(input())

def manhattan(r1, c1, r2, c2):
    return abs(r1- r2) + abs(c1 - c2)

def hasOffice(r, c, grid, distance):
    row = len(grid)
    col = len(grid[0])
    if distance == 0:
        return grid[r][c]
    elif distance >= (row + col - 2):
        return False
    else:
        quads = [[-1, -1], [-1, +1], [+1,+1], [+1, -1]]
        for quad in quads:
            for d in range(distance):
                x = d * quad[0]
                y = (distance - d) * quad[1]
                if r+x >= row or r+x < 0 or c+y >= col or c+y <= 0:
                    continue
                if grid[r+x][c+y]:
                    return True
        return False

    if grid[r][c]:
        return True

def nearestOffice(r, c, grid):
    row = len(grid)
    col = len(grid[0])
    if grid[r][c] == '1':
        return 0
    else:
        distance = 1
        while distance < (row + col - 2):
            # print("distance: {}".format(distance))
            quads = [[1, 1], [1, -1], [-1,-1], [-1, 1]]
            for quad in quads:
                # print("quad: {}".format(quad))
                for d in range(0, distance+1):
                    x = r + (d * quad[0])
                    y = c + ((distance - d) * quad[1])
                    # print("[{}, {}] checking [{}, {}]".format(r, c, x, y))
                    if x >= row or x < 0 or y >= col or y < 0:
                        continue
                    if grid[x][y] == '1':
                        return distance
            distance += 1
        return -1

for case in range(1, t + 1):
    r, c = [int(i) for i in input().split(" ")]
    grid = []
    gridDis = []
    for row in range(r):
        grid.append(list(input()))

    for row in range(r):
        dis = []
        for col in range(c):
            dis.append(nearestOffice(row, col, grid))
        gridDis.append(dis)

    largest = 0
    largestCell = [0, 0]
    for row in range(r):
        for col in range(c):
            if gridDis[row][col] > largest:
                largest = gridDis[row][col]
                largestCell = [row, col]
    
    # for x in gridDis:
    #     print(*x, sep=" ")
    # print('===')
    
    if largest == 0:
        print("Case #{}: {}".format(case, 0))
        continue

    grid[largestCell[0]][largestCell[1]] = '1'

    newGridDis = []
    for row in range(r):
        dis = []
        for col in range(c):
            dis.append(nearestOffice(row, col, grid))
        newGridDis.append(dis)

    largest = 0
    for row in range(r):
        for col in range(c):
            if newGridDis[row][col] > largest:
                largest = newGridDis[row][col]
        
    # for x in newGridDis:
    #     print(*x, sep=" ")
    
    print("Case #{}: {}".format(case, largest))