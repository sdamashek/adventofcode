inp = open('input_d6.txt').read()

import collections
c = []
for i in range(8):
    c.append(collections.Counter())

for i in inp.split('\n')[:-1]:
    for d in range(8):
        c[d] += collections.Counter(i[d])

res = ''
for i in range(8):
    res += c[i].most_common()[-1][0]
print(res)
