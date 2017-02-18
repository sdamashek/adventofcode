f = open('input_d17.txt').read()
inp = 'edjrjqaa'

def is_open(char):
    return char in 'bcdef'

cache = dict()
import hashlib
def hash_path(p):
    if p in cache:
        return cache[p]
    h = hashlib.md5(inp+p).hexdigest()
    cache[p] = h
    return h

max_len = 0
def bfs_paths(start, goal):
    global max_len
    queue = [(start, [start], '')]
    while queue:
        (vertex, path, lpath) = queue.pop(0)
        c = get_avail(lpath, vertex)
        for next in c:
            if next[:2] == goal:
                if len(lpath + next[2]) > max_len:
                    max_len = len(lpath + next[2])
                    print(max_len)
            else:
                print(lpath)
                queue.insert(0,(next[:2], path + [next[:2]], lpath + next[2]))

def get_avail(path, pos):
    x,y = pos
    h = hash_path(''.join(path))
    r = []
    if is_open(h[0]):
         r.append((x,y+1,'U'))
    if is_open(h[1]):
        r.append((x,y-1,'D'))
    if is_open(h[2]):
        r.append((x-1,y,'L'))
    if is_open(h[3]):
        r.append((x+1,y,'R'))
    print(r)
    for i in r:
        if i[0] < 0 or i[1] < 0 or i[0] > 3 or i[1] > 3:
            r.remove(i)
    return set(r)

bfs_paths((0,3),(3,0))
print(max_len)
#print(sorted(list(bfs_paths((0,3),(3,0))), key=lambda x:len(x)))
