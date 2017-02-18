import hashlib
inp = 'ffykfhsq'

res = [0]*8

n = 0
while 0 in res:
    r = hashlib.md5(inp + str(n)).hexdigest()
    if r.startswith('00000'):
        if ord(r[5]) >= ord('0') and ord(r[5]) <= ord('7'):
            if res[int(r[5])] == 0:
                print(r[5])
                res[int(r[5])] = r[6]

    n += 1

print(''.join(res))
