f = open("latex.log")
n = 0
for lines in f:
    lines = lines.strip('\n')
    if len(lines) == 0:
        continue
    n += 1
print("共{}行".format(n))