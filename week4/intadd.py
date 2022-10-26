s=0
for i in range(1, 967):
    if i % 2 != 0:
        s += i
    else:
        s -= i
print(s)
