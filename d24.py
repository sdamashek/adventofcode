inp = open('input_d24.txt').read().strip().split('\n')

graph = dict()
n = 0
yn = len(inp)
xn = len(inp[0])

poss = '01234567'

def find_n(ton):
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            if inp[y][x] == str(ton):
                return (x,y)

def exists(n, found):
    for ele in list(graph[n]):
        if ele[0] == int(found):
            return True
    return False

def find_adj(x,y):
    res = set()
    for (a,b) in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
        if a >= 0 and a < xn and b >= 0 and b < yn:
            if inp[b][a] != '#':
                res.add((a,b))
    return res

for n in range(8):
    x,y = find_n(n)
    if n not in graph:
        graph[n] = set()
    visited = set()
    queue = [((x,y), set([(x,y)]))]
    while queue:
        (vertex, path) = queue.pop(0)
        for nex in find_adj(*vertex) - path:
            if nex in visited:
                continue
            visited.add(nex)
            found = inp[nex[1]][nex[0]]
            if found in poss:
                if not exists(n,found):
                    graph[n].add((int(found), len(path)))
                    if int(found) not in graph:
                        graph[int(found)] = set()
                    graph[int(found)].add((n, len(path)))
            else:
                p = path.copy()
                p.add(nex)
                queue.append((nex, p))

print(graph)
print('bruteforcing TSP (fun times)')
smallest = 10000
queue = [(0, set([0]), 0)]
while queue:
    (current, visited, count) = queue.pop(0)
    if count >= smallest:
        continue
    for pos in graph[current]:
        nv = visited.copy()
        nv.add(pos[0])
        nc = count + pos[1]
        if all([int(p) in nv for p in poss]) and pos[0] == 0 and nc < smallest:
            smallest = nc
            print(smallest)

        elif pos[0] not in visited and nc < smallest:
            queue.append((pos[0], nv, nc))

print(smallest)
