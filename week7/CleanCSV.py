f = open("data.csv")
s = f.read()
for line in s:
    line = line.strip(" ")
    print(line,end="")