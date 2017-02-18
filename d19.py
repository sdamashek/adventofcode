inp = open('input_d19.txt').read().strip()

inp = 3018458

import sys
inp = int(sys.argv[1])
class Ele:
    def __init__(self, ind, n):
        self.ind = ind
        self.n = n
        self.val = 1

#m = []
base = Ele(0, None)
prev = base
for i in range(1,inp):
    e = Ele(i, None)
    prev.n = e
    #print('Set ',prev.ind,' to ',e.ind)
    prev = e
    if i == inp-1:
        e.n = base
#    m.append(e)

#n = [(_,1) for _ in range(inp)]

def get_prev(i):
    return i.n

def is_all():
    for i in range(inp):
        if n[i][1] == inp:
            return n[i][0]
    return False

cur = base
count = inp
while cur.n.ind != cur.ind:
    left = count / 2
    right = count - left
    to_steal_p = cur
    to_steal = cur.n
    for i in range(left-1):
        to_steal_p = to_steal
        to_steal = to_steal.n
    #cur.val += to_steal.val
    to_steal_p.n = to_steal.n
    cur = cur.n
    count -= 1
    # while i < len(n):
    #     if n[i]:
    #         n[i] = (n[i][0], get_prev(i)[1])
    #         n.pop(get_prev_i(i))
    #     print(len(n))
    #     i += 1
    # print(len(n))
    # if len(n) <= 1:
    #     print(n)
    #     break
print(cur.ind+1)
