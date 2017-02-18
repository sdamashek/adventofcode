inp = open('input_d22.txt').read().strip().split('\n')[2:]
# inp = """Filesystem            Size  Used  Avail  Use%
# /dev/grid/node-x0-y0   10T    8T     2T   80%
# /dev/grid/node-x0-y1   11T    6T     5T   54%
# /dev/grid/node-x0-y2   32T   28T     4T   87%
# /dev/grid/node-x1-y0    9T    7T     2T   77%
# /dev/grid/node-x1-y1    8T    0T     8T    0%
# /dev/grid/node-x1-y2   11T    7T     4T   63%
# /dev/grid/node-x2-y0   10T    6T     4T   60%
# /dev/grid/node-x2-y1    9T    8T     1T   88%
# /dev/grid/node-x2-y2    9T    6T     3T   66%""".strip().split('\n')[1:]
yn = 35
xn = 30
# yn = 3
# xn = 3

nodes = [[None for __ in range(xn)] for _ in range(yn)]

def get_used_avail(l):
    a = l.replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ')
    used = a.split(' ')[2]
    avail = a.split(' ')[3]
    used = int(used.replace('T',''))
    avail = int(avail.replace('T',''))
    return (used,avail)

for x in range(xn):
    for y in range(yn):
        nodes[y][x] = get_used_avail(inp[x*yn + y])

def is_adjacent(x,y,xp,yp):
    if (x == xp-1 or x == xp+1) and y == yp:
        return True
    if (y == yp-1 or y == yp+1) and x == xp:
        return True
    return False

#print(nodes)
def get_viable(nodel):
    res = []
    for x in range(xn):
        for y in range(yn):
            for (xp,yp) in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                if xp < 0 or xp >= xn or yp < 0 or yp >= yn:
                    continue
                if x == xp and y == yp:
                    continue
                if nodel[y][x][0] == 0:
                    continue
                if nodel[y][x][0] <= nodel[yp][xp][1]:
                    res.append((x,y,xp,yp))
    return res

import copy
def compare(a,b):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] != b[i][j]:
                return False
    return True

def is_complete(swaps):
    loc = (xn-1,0)
    for sw in swaps:
        if loc == (sw[0],sw[1]):
            loc = (sw[2],sw[3])
    return (loc == (0,0))

def distance_to_loc(x,swaps):
    loc = (xn-1,0)
    for sw in swaps:
        if loc == (sw[0],sw[1]):
            loc = (sw[2],sw[3])
    return (abs(x[2]-loc[0]) + abs(x[3]-loc[1]))

def swap(next):
    global nodes
    nodes[next[3]][next[2]] = (nodes[next[1]][next[0]][0]+nodes[next[3]][next[2]][0], -nodes[next[1]][next[0]][0]+nodes[next[3]][next[2]][1])
    nodes[next[1]][next[0]] = (0, nodes[next[1]][next[0]][0]+nodes[next[1]][next[0]][1])

def dobfs():
    global nodes
    queue = [(get_viable(nodes), 0, [])]
    while queue:
        (viable, count, swaps) = queue.pop(0)
        print(swaps)
        bk = copy.deepcopy(nodes)
        for sw in swaps:
            swap(sw)
        for next in sorted(viable, key = lambda x: distance_to_loc(x,swaps)):
            if is_complete(swaps):
                print('done')
                print(len(swaps))
                return
            else:
                if len(swaps) >= 1:
                    if swaps[-1] == (next[2],next[3],next[0],next[1]):
                        continue

                bk1 = nodes[next[1]][next[0]]
                bk2 = nodes[next[3]][next[2]]
                swap(next)

                queue.append((get_viable(nodes), count + 1, swaps + [next]))
                nodes[next[1]][next[0]] = bk1
                nodes[next[3]][next[2]] = bk2

        nodes = bk

dobfs()
