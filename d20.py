inp = open('input_d20.txt').read().strip()
init = 'abcdefgh'
#init = 'dgfaehcb'
def rotate(st,n=1):
    for _ in range(n):
        st = st[-1] + st[:-1]
    return st

def rotateleft(st,n=1):
    for _ in range(n):
        st = st[1:] + st[0]
    return st

def swap(x,y):
    global init
    c = list(init)
    c[x],c[y]=c[y],c[x]
    init = ''.join(c)

for l in inp.split('\n'):
    print(l)
    print(init)
    if l.startswith('swap position'):
        x = int(l.split('swap position ')[1].split(' with')[0])
        y = int(l.split('with position ')[1])
        swap(x,y)
    elif l.startswith('swap letter'):
        x = l.split('swap letter ')[1].split(' with')[0]
        y = l.split('with letter ')[1]
        xi = init.index(x)
        yi = init.index(y)
        swap(xi,yi)
    elif l.startswith('rotate based'):
        x = l.split('letter ')[1]
        xi = init.index(x)
        init = rotate(init, 1+xi+(0 if xi < 4 else 1))
    elif l.startswith('rotate'):
        if 'left' in l:
            x = int(l.split('left ')[1].split(' step')[0])
            init = rotateleft(init,x)
        else:
            x = int(l.split('right ')[1].split(' step')[0])
            init = rotate(init,x)
    elif l.startswith('reverse '):
        x = int(l.split('positions ')[1].split(' through')[0])
        y = int(l.split('through ')[1])
        init = init[:x] + init[x:y+1][::-1] + init[y+1:]
    elif l.startswith('move '):
        x = int(l.split('position ')[1].split(' to')[0])
        y = int(l.split('to position ')[1])
        tm = init[x]
        init = init[:x] + init[x+1:]
        init = init[:y] + tm + init[y:]
print(init)
