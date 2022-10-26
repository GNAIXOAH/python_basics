CurCon = input()
if CurCon[0:3] in ['USD']:
    R = eval(CurCon[3:])*6.78
    print("RMB{:.2f}".format(R))
elif CurCon [0:3] in ['RMB']:
    U = eval(CurCon[3:])/6.78
    print("USD{:.2f}".format(U))
else:
    print()

