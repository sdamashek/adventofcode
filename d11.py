inp = """The first floor contains a thulium generator, a thulium-compatible microchip, a plutonium generator, and a strontium generator.
The second floor contains a plutonium-compatible microchip and a strontium-compatible microchip.
The third floor contains a promethium generator, a promethium-compatible microchip, a ruthenium generator, and a ruthenium-compatible microchip.
The fourth floor contains nothing relevant."""

from copy import deepcopy
class Generator:
    def __init__(self,t):
        self.t = t

    def __repr__(self):
        return 'Gen ' + self.t

    def __hash__(self):
        return hash('G'+self.t)

    def __eq__(self, x):
        return type(x) is Generator and self.t == x.t

class Microchip:
    def __init__(self,t):
        self.t = t

    def __repr__(self):
        return 'Mic ' + self.t

    def __hash__(self):
        return hash('M'+self.t)
    def __eq__(self, x):
        return type(x) is Microchip and self.t == x.t

class Floor:
    contents = set()
    def __init__(self,n,contents=None):
        self.n = n
        if contents is not None:
            self.contents = contents

    def is_valid(self):
        for ele in self.contents:
            if isinstance(ele, Microchip):
                if not self.check_microchip(ele):
                    return False
        return True

    def check_microchip(self, m):
        t = m.t
        for ele in self.contents:
            if isinstance(ele, Generator) and ele.t != t:
                return self.has_generator_t(t)
        return True

    def has_generator_t(self, t):
        for ele in self.contents:
            if isinstance(ele, Generator) and ele.t == t:
                return True
        return False

    def __deepcopy__(self, memo):
        return Floor(self.n, set(self.contents))

    def __str__(self):
        return str(self.contents)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, x):
        return len(self.contents) == len(x.contents) and self.contents == x.contents

class Floors:

    def __init__(self):
        self.floors = [Floor(0), Floor(1), Floor(2), Floor(3)]
    def __getitem__(self, n):
        return self.floors[n]
    def __repr__(self):
        return ' '.join([repr(fl) for fl in self.floors])
    def __str__(self):
        return self.__repr__()
import sys
sys.setrecursionlimit(10000)
floors = Floors()
floors[0].contents = set([Generator('thulium'), Microchip('thulium'), Generator('plutonium'), Generator('strontium')])
floors[1].contents = set([Microchip('plutonium'), Microchip('strontium')])
floors[2].contents = set([Generator('promethium'), Microchip('promethium'), Generator('ruthenium'), Microchip('ruthenium')])
#floors[0].contents = set([Microchip('hydrogen'), Microchip('lithium')])
#floors[1].contents = set([Generator('hydrogen')])
#floors[2].contents = set([Generator('lithium')])

elevator_n = 0

import itertools
UP = 5
DOWN = 4

def poss_is_valid(p):
    for ele in p:
        if isinstance(ele, Microchip):
            if not poss_check_microchip(p, ele):
                return False
    return True

def poss_check_microchip(p, el):
    t = el.t
    for ele in p:
        if isinstance(ele, Generator) and ele.t != t:
            return poss_has_generator_t(p,t)
    return True

def poss_has_generator_t(p, t):
    for ele in p:
        if isinstance(ele, Generator) and ele.t == t:
            return True
    return False

def determine_new_fl(n,d):
    if d == UP:
        return n+1
    return n-1

def attempt_solution(fl_o, n, tm, d):
    new_n = determine_new_fl(n,d)
    if (new_n < 0) or (new_n > 3):
        return (False, None, None)

    fl = Floors()
    for i in range(4):
        fl[i].contents = fl_o[i].contents.copy()
    for i in tm:
        fl[new_n].contents.add(i)
        fl[n].contents.remove(i)


    return ((fl[n].is_valid() and fl[new_n].is_valid()), fl, new_n)

def is_complete(fl):
    print(sum([len(fl[x].contents) for x in range(3)]))
    return all([len(fl[x].contents) == 0 for x in range(3)])

def is_dup(res, sol, n, already):
    for i in list(res):
        if already >= i[2] and i[1] == n and all([i[0][floor]==sol[floor] for floor in range(4)]):
            return True
    return False

done = []
res = set()
def get_min():
    if done:
        return min(done)
    return 100000000

def determine_steps(fl, n, already=0):
    if already >= get_min() or already >= 50:
        return
    if is_complete(fl):
        print("Got solution")
        print(fl,n,already)
        done.append(already)
    poss = []
    for z in range(1,min(len(fl[n].contents)+1,3)):
        poss.extend(itertools.combinations(fl[n].contents, z))


    for p in poss:
        if not poss_is_valid(p):
            continue
        for d in (UP, DOWN):
            r = attempt_solution(fl, n, p, d)
            if r[0]:
                if is_complete(fl):
                    print(fl,n,already)
                if is_dup(res, r[1], r[2], already+1):
                    continue
                res.add((r[1],r[2], already+1))
                determine_steps(r[1], r[2], already+1)
determine_steps(floors, 0)
print(done)
print(min(done))
