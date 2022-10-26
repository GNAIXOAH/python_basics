n=input()
m=""
for i in n:
    if "a"<=i<="z":
        m+=chr(ord("a")+(ord(i)-ord("a")+3)%26)
    elif "A"<=i<="Z":
        m+=chr(ord("A")+(ord(i)-ord("A")+3)%26)
    else: m+=i
print(m)

