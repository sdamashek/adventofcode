inp1 = open('input_d9.txt').read().strip()

def repeat_stuff(inp):
    if not inp:
        return 0
    c = inp[0]
    r = 0
    if c == '(':
        char_count = int(inp[1:].split('x',1)[0])
        repeat_count = int(inp[1:].split('x',1)[1].split(')')[0])
        i = inp.index(')')
        to_rep = repeat_stuff(inp[i+1:i+1+char_count])
        r += to_rep * repeat_count
        return r + repeat_stuff(inp[i+1+char_count:])
    else:
        return 1 + repeat_stuff(inp[1:])

r = repeat_stuff(inp1)
print(r)
