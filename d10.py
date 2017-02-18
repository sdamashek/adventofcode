inp = open('input_d10.txt').read().split('\n')[:-1]
done = set()
al = set(range(len(inp)))

import collections
bots = collections.defaultdict(list)
outputs = collections.defaultdict(list)

while al != done:
    for ind,i in enumerate(inp):
        #print(ind,i)
        #print(bots)
        if ind in done:
            continue
        if i.startswith('value '):
            num = int(i.split(' ', 1)[1].split(' ',1)[0])
            destbot = int(i.rsplit(' ', 1)[1])
            bots[destbot].append(num)
            done.add(ind)
        else:
            sourcebot = int(i.split(' ',1)[1].split(' ',1)[0])
            if len(bots[sourcebot]) != 2:
                continue
            done.add(ind)
            low = sorted(bots[sourcebot])[0]
            high = sorted(bots[sourcebot])[1]
            if low == 17 and high == 61:
                print(sourcebot)
            if 'low to output' in i:
                o = int(i.split('low to output ')[1].split(' ',1)[0])
                outputs[o].append(low)
            else:
                #print('bot')
                o = int(i.split('low to bot ')[1].split(' ',1)[0])
                bots[o].append(low)
                #print(bots)
            if 'high to output' in i:
                o = int(i.split('high to output ')[1])
                outputs[o].append(high)
            else:
                o = int(i.split('high to bot ')[1])
                bots[o].append(high)
            bots[sourcebot].remove(low)
            bots[sourcebot].remove(high)

print(outputs[0],outputs[1],outputs[2])
