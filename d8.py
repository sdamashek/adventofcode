inp = open('input_d8.txt').read()

arr = [[0 for i in range(50)] for j in range(6)]

def rect(x,y):
    global arr
    for i in range(x):
        for j in range(y):
            print(i,j)
            arr[j][i] = 1

def rotatecol(x,n):
    global arr
    for _ in range(n):
        first = arr[5][x]
        for i in range(5,0,-1):
            arr[i][x] = arr[i-1][x]
        arr[0][x] = first
        print(arr)

def rotaterow(y,n):
    global arr
    for _ in range(n):
        first = arr[y][49]
        for i in range(49,0,-1):
            arr[y][i] = arr[y][i-1]
        arr[y][0] = first
        print(arr)

def countpixels():
    c = 0
    for i in range(50):
        for j in range(6):
            if arr[j][i] == 1:
                c += 1
    return c

for i in inp.split('\n')[:-1]:
    if i.startswith('rotate row'):
        rotaterow(int(i.split('y=')[1].split(' ')[0]), int(i.split('by ')[1]))

    elif i.startswith('rotate column'):
        print(i)
        rotatecol(int(i.split('x=')[1].split(' ')[0]), int(i.split('by ')[1]))
    else:
        rect(int(i.split(' ')[1].split('x')[0]), int(i.split('x')[1]))

print(arr)
print(countpixels())
for i in arr:
    print(' '.join(map(str,i)))
