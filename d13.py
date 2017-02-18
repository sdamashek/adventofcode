inp = 1350

from collections import Counter
def is_open(x,y):
    a = x*x + 3*x + 2*x*y + y + y*y
    a += inp
    return (Counter(bin(a)[2:])['1'] % 2 == 0)

def find_adjacent(vertex):
    res = set()
    for i,j in ((vertex[0]-1,vertex[1]),(vertex[0]+1,vertex[1]),(vertex[0],vertex[1]-1),(vertex[0],vertex[1]+1)):
            if is_open(i,j) and (i>=0) and (j>=0):
                res.add((i,j))
    return res

def print_stuff(x,y):
    for j in range(y):
        line = ''
        for i in range(x):
            line += ('a' if is_open(i,j) else '#')
        print(line)

def bfs_paths(start):
    queue = [(start, [start])]
    visited = set()
    count = 0
    while queue:
        (vertex, path) = queue.pop(0)
        if vertex not in visited and len(path) <= 51:
            count += 1
        if len(path) > 51:
            continue
        visited.add(vertex)
        for next in find_adjacent(vertex) - set(path):
            queue.append((next, path + [next]))
    print(visited)
    return count

print_stuff(30,30)
print(bfs_paths((1,1)))
