inp = 'qzyelonm' # original
# inp = 'yjdafjpo'

import hashlib

i = 0

cache = {}
def gen_hash(k):
    r = inp + str(k)

    if k in cache:
        r = cache[k]
        return r
    #for _ in range(2017): # part 2
    for _ in range(1):
        r = hashlib.md5(r).hexdigest().lower()
    cache[k] = r
    return r

def test_thousand(x,c):
    ii = i
    for j in range(ii+1, ii+1001):
        if (c*5) in gen_hash(j):
            return True
    return False

def is_three(j):
    for c in range(len(j)):
        if j[c+1:c+3] == j[c]*2:
            return j[c]
    return False

nth = 0
while nth < 64:
    thing = gen_hash(i)
    c = is_three(thing)
    if c:
        if test_thousand(i,c):
            nth += 1
    i += 1

print(nth)
print(i-1)
