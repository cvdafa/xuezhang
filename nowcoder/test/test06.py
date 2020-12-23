# 如何判断字典a在字典b
# 已知一个dict 比如a = {“a”:1},另一个dict比如为b = {“a”:1,”b”:2},如何判断a是否在与b中。
# 一般在接口测试的时候，返回的参数比较多的情况，如果一个个字段去校验，会比较麻烦，
# 那么如何直接拿一个期望的字典放键值对，判断结果里面是否包含期望的值

a = {"a":2}
b = {"a":1,"b":2}
for key in a.keys() :
    if (key in b.keys()) and (a[key] == b[key]):
        print("在")
    else:
        print("不在")



    # for key_b,value_b in b.items():
    #     if key == key_b:
    #         if a[key] == b[key_b]:
    #             print("在")
    #         else:
    #             print("buzai")



















