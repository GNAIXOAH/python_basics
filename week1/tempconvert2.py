#tempconvert.py
TempStr = input()
if TempStr[-1] in ['F', 'f']:
    C = (eval(TempStr[0:-1]) - 32)/1.8
    print("{:.2f}C".format(C))
elif TempStr [-1] in ['C', "c"]:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("{:.2f}F".format(F))
else:
    print("输入格式错误")

