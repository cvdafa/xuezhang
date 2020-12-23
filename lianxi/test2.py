#冒泡排序
l = [2,1,5,3,56,2,1,0,67,3,9,12]
for i in range(0,len(l)-1):
    for j in range(i+1,len(l) ):
        if l[i] < l[j]:
            l[i],l[j]=l[j],l[i]
print(l)