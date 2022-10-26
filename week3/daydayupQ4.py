def dayup(dayfactor):
    dayup=1
    for i in range(365):
        if i % 7 in [0, 6]:
            dayup *= 1 - 0.01
        else:
            dayup *= 1 + dayfactor
    return dayup
dayfactor=0.01
while dayup(dayfactor)<37.78:
    dayfactor+=0.01
print("工作日参数量{:.2f}".format(dayfactor))


