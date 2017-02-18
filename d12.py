inp = open('input_d12.txt').read().split('\n')[:-1]

registers = {x:0 for x in ['a','b','c','d']}
registers['c'] = 1
ind = 0
while ind < len(inp):
    #print(ind)
    i = inp[ind].split(' ')
    if i[0] == 'cpy':
        if i[1] in registers:
            x = registers[i[1]]
        else:
            x = int(i[1])
        registers[i[2]] = x
    if i[0] == 'inc':
        registers[i[1]] += 1
    if i[0] == 'dec':
        registers[i[1]] -= 1
    if i[0] == 'jnz':
        #print(i)
        if i[1] in registers:
            x = registers[i[1]]
        else:
            x = int(i[1])
        if x != 0:
            ind += int(i[2])
        else:
            ind += 1
    else:
        ind += 1
print(registers)
