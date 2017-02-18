inp = open('input_d18.txt').read()

xl = len(inp)-1
yl = 400000
tiles = [[False for _ in range(xl)] for _ in range(yl)] # True if trap

def get_tile(x,y):
    if x < 0 or x >= xl or y < 0 or y >= yl:
        return False
    return tiles[y][x]

def is_trap(x,y):
    left,center,right = get_tile(x-1,y-1),get_tile(x,y-1),get_tile(x+1,y-1)
    if left and center and not right:
        return True
    if center and right and not left:
        return True
    if left and not right and not center:
        return True
    if right and not left and not center:
        return True
    return False

count = 0
for x in range(xl):
    tiles[0][x] = (True if inp[x] == '^' else False)
    if inp[x] == '.':
        count += 1

for y in range(1,yl):
    for x in range(xl):
        tiles[y][x] = is_trap(x,y)
        if not tiles[y][x]:
            count += 1

# for y in range(yl):
#     for x in range(xl):
#         if not tiles[y][x]:
#             count += 1
print(count)
