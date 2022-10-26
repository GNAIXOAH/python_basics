a=input()
b=eval(a)
for i in range(1,b+1,2):
    print("{0:^{1}}".format('*'*i,b))
