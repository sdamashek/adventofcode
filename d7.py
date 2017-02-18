inp = open('input_d7.txt').read()

i = inp.split('\n')[:-1]

import re

ins = set()
t = True
def check_aba(s):
    for k in range(len(s)-2):
        print(s[k:k+2], s[k+1:k+3])

        if s[k:k+2] == s[k+1:k+3][::-1] and s[k] != s[k+1]:
            if t:
                ins.add(s[k:k+2][::-1] + s[k+1])
                print(ins)
            elif s[k:k+3] in ins:
                print("True")
                return True
            else:
                print(ins)
                print("Fail " + s[k:k+3])
    return False

count = 0
for j in i:
    ins = set()
    hyp = re.findall(r'\[([^\]]+)\]', j)
    st = []
    st.append(j.split('[',1)[0])
    st += re.findall(r'\]([^\[]*)',j)
    print(j)
    print(st)
    print(hyp)
    t = True
    map(check_aba, hyp)
    t = False
    print("Checking")
    if any(map(check_aba,st)):
        count += 1
print(count)
