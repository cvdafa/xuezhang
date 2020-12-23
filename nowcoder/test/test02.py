# 以字符串的形式读入两个数字，编写一个函数计算它们的和，以字符串形式返回。
# （字符串长度不大于100000，保证字符串仅由'0'~'9'这10种字符组成）

# a_int = int( input('请输入第一个数字:\n'))
# b_int = int(input("请输入第二个数字："))
# print(type(str(a_int+b_int)))
list1 = [2,1,4,2,6,1]
class Ord :
    def order (a):
        for i in range(len(a)-1):
            for j in range(len()-1-i):
                if a[j+1]<a[j]:
                    a[j],a[j+1]=a[j+1],a[j]
        return a
print(Ord().order(list1))


