f = open("latex.log")
n = 0
d = {}
for i in range(26):
    d[chr(ord('a')+i)] = 0
for line in f:
    for c in line:
        d[c] = d.get(c,0) + 1
        n+=1
print("共{}字符".format(n),end="")
for i in range(26):
    if d[chr(ord('a')+i)] != 0:
         print(",{}:{}".format(chr(ord('a')+i), d[chr(ord('a')+i)]),end="")

