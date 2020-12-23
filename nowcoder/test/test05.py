#输入m1={'a':1,'b':2,'c':1} 输出{1:['a','c'],2:['b']}


dict_new = {}
m1 = {'a':1,'b':2,'c':1}

for key,value in m1.items():
    print(key,value)
    if value not in dict_new:
        dict_new[value] = [key]
    else :
        dict_new[value].append(key)
print(dict_new)
