inp = open('input_d23.txt').read().strip().split('\n')

registers = {x:0 for x in ['a','b','c','d']}
#registers['c'] = 1
registers['a'] = 12
ind = 0
while ind < len(inp):
    i = inp[ind].split(' ')
    print(registers)
    print(i)
    if i[0] == 'cpy':
        if i[1] in registers:
            x = registers[i[1]]
        else:
            x = int(i[1])
        if i[2] in registers:
            registers[i[2]] = x
    if i[0] == 'inc':
        if i[1] in registers:
            registers[i[1]] += 1
    if i[0] == 'dec':
        if i[1] in registers:
            registers[i[1]] -= 1
    if i[0] == 'tgl':
        if i[1] in registers:
            x = registers[i[1]]
        else:
            x = int(i[1])
        if ind+x >= 0 and ind+x < len(inp):
            tomod = inp[ind+x]
            modi = tomod.split(' ')
            if len(modi) == 2:
                if modi[0] == 'inc':
                    modi[0] = 'dec'
                else:
                    modi[0] = 'inc'
            elif len(modi) == 3:
                if modi[0] == 'jnz':
                    modi[0] = 'cpy'
                else:
                    modi[0] = 'jnz'
            inp[ind+x] = ' '.join(modi)
    if i[0] == 'mul':
        registers[i[3]] = registers[i[1]] * registers[i[2]]
    if i[0] == 'jnz':
        #print(i)
        if i[1] in registers:
            x = registers[i[1]]
        else:
            x = int(i[1])
        if x != 0:
            if i[2] in registers:
                ind += registers[i[2]]
            else:
                ind += int(i[2])
        else:
            ind += 1
    else:
        ind += 1

print(registers)
