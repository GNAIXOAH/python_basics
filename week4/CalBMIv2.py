height, weight=eval(input())
bmi=weight/pow(height, 2)
print("BMI数值为:{:.2f}".format(bmi))
who=""
who2=""
if bmi<18.5:
    who="偏瘦"
    who2="偏瘦"
elif 18.5<=bmi<24:
    who="正常"
    who2="正常"
elif 24<=bmi<=25:
    who = "正常"
    who2 = "偏胖"
elif 25<=bmi<28:
    who="偏胖"
    who2 = "偏胖"
elif 28<=bmi<30:
    who = "偏胖"
    who2 = "肥胖"
else:
    who="肥胖"
print("BMI指标为:国际'{0}',".format(who), end="")
print("国内'{0}'".format(who2))
