s=""
for i in range(100, 1000):
    t=str(i)
    if eval(t[0]) ** 3 + eval(t[1]) ** 3 + eval(t[2]) ** 3 == i:
        s += "{},".format(i)
print(s[:-1])
