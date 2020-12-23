#判断一个字符串是否是回文
s = input('请输入一段字符串：')
if not s :
    print("请不要输入空字符串")

for i in range(0,int(len(s)/2)):
    if s[i] == s[len(s)-i-1]:
        print("是回文")
    else:
        print('不是回文')

