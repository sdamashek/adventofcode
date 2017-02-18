#inp = ['R3', 'L5', 'R1', 'R2', 'L5', 'R2', 'R3', 'L2', 'L5', 'R5', 'L4', 'L3', 'R5', 'L1', 'R3', 'R4', 'R1', 'L3', 'R3', 'L2', 'L5', 'L2', 'R4', 'R5', 'R5', 'L4', 'L3', 'L3', 'R4', 'R4', 'R5', 'L5', 'L3', 'R2', 'R2', 'L3', 'L4', 'L5', 'R1', 'R3', 'L3', 'R2', 'L3', 'R5', 'L194', 'L2', 'L5', 'R2', 'R1', 'R1', 'L1', 'L5', 'L4', 'R4', 'R2', 'R2', 'L4', 'L1', 'R2', 'R53', 'R3', 'L5', 'R72', 'R2', 'L5', 'R3', 'L4', 'R187', 'L4', 'L5', 'L2', 'R1', 'R3', 'R5', 'L4', 'L4', 'R2', 'R5', 'L5', 'L4', 'L3', 'R5', 'L2', 'R1', 'R1', 'R4', 'L1', 'R2', 'L3', 'R5', 'L4', 'R2', 'L3', 'R1', 'L4', 'R4', 'L1', 'L2', 'R3', 'L1', 'L1', 'R4', 'R3', 'L4', 'R2', 'R5', 'L2', 'L3', 'L3', 'L1', 'R3', 'R5', 'R2', 'R3', 'R1', 'R2', 'L1', 'L4', 'L5', 'L2', 'R4', 'R5', 'L2', 'R4', 'R4', 'L3', 'R2', 'R1', 'L4', 'R3', 'L3', 'L4', 'L3', 'L1', 'R3', 'L2', 'R2', 'L4', 'L4', 'L5', 'R3', 'R5', 'R3', 'L2', 'R5', 'L2', 'L1', 'L5', 'L1', 'R2', 'R4', 'L5', 'R2', 'L4', 'L5', 'L4', 'L5', 'L2', 'L5', 'L4', 'R5', 'R3', 'R2', 'R2', 'L3', 'R3', 'L2', 'L5']
inp = ['R8', 'R4', 'R4', 'R8']

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

n = 0
e = 0
visited = set()
first = True
f = None

d = NORTH
for i in inp:
    visited.add((n,e))
    dchange = i[0]
    num = int(i[1:])
    if dchange == 'R':
        d += 1
        if d == 4:
            d = NORTH
    if dchange == 'L':
        d -= 1
        if d == -1:
            d = WEST
    if d == NORTH:
        for i in range(num):
            n += 1
            print(n,e)
            if first and (n,e) in visited:
                first = False
                f = (n,e)
            visited.add((n,e))

    elif d == EAST:
        for i in range(num):
            e += 1
            print(n,e)
            if first and (n,e) in visited:
                first = False
                f = (n,e)
            visited.add((n,e))
    elif d == SOUTH:
        for i in range(num):
            n -= 1
            print(n,e)
            if first and (n,e) in visited:
                first = False
                f = (n,e)
            visited.add((n,e))
    elif d == WEST:
        for i in range(num):
            e -= 1
            print(n,e)
            if first and (n,e) in visited:
                print(n,e)
                first = False
                f = (n,e)
            visited.add((n,e))
print(f)
print((n,e))
print(abs(n-f[0])+abs(e-f[1]))

