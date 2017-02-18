inp = '01000100010010111'

def dragon_step(a):
    b = a[::-1]
    b = b.replace('0','a').replace('1','0').replace('a','1')
    return a+'0'+b

def chk(a):
    c = ''
    for i in range(0,len(a),2):
        if len(list(set(a[i:i+2]))) == 1:
            c += '1'
        else:
            c += '0'
    while len(c) % 2 == 0:
        c = chk(c)
    return c

l = 35651584
res = inp
while len(res) < l:
    res = dragon_step(res)

res = res[:l]
c = chk(res)
print(c)
