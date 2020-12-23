# # 数组中有一个数字出现的次数超过数组长度的一半，
# # 请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
# # 由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
class findNumber ():
    def theNumber(self,list0ne):
        lenth = len(list0ne)
        dic = {}
        for  i  in range(lenth):
            if list0ne[i]  in dic :
                dic[list0ne[i]] += 1
                if dic[list0ne[i]] > lenth%2 :
                   return print( dic[list0ne[i]])
                else:
                    dic[list0ne[i]] = 0
            else:
                return 0
list0ne = [1,2,3,4,2,2,2,2,2]
findNumber().theNumber(list0ne)