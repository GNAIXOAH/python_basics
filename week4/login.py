m = 0
for i in range(1, 4):
    n = input()
    p = input()
    if n == "Kate" and p == "666666":
        print("登录成功！")
        m = 1
        break
if m != 1:
    print("3次用户名或者密码均有误！退出程序。")
