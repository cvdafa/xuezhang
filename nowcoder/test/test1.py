#python编写函数接受一个字符串分别统计大写字母小写字母数字其他字符的个数并以元组的形式返回结果?
up = []
low = []
def number (a):
    for i in a:
        if i.isupper():
            up.append(i)
        elif i.islower():
            low.append(i)
    return up,low

number(["A","B","a","b","c"])
a=len(up)
b=len(low)
t_a =()


print(t_a,b)


