# 对于一个给定的字符串，我们需要在线性(也就是O(n))的时间里对它做一些变形。
# 首先这个字符串中包含着一些空格，
# 就像"Hello World"一样，然后我们要做的是把着个字符串中由空格隔开的单词反序，
# 同时反转每个字符的大小写。比如"Hello World"变形后就变成了"wORLD hELLO"

str = 'Hello World'
list = str.split(" ")
list[0],list[1] = list[1],list[0]
str_list = " ".join(list)
print(str_list.swapcase())
