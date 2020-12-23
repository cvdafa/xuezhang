# 给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。
#
# 换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。
#
# 以数组形式返回答案。
# 输入：nums = [8,1,2,2,3]
# 输出：[4,0,1,1,3]
# list_test = [1,8,2,0,4]
# dict = {}
# count = 0
# nume = len(list_test)
# print(nume*[0])
# for  i in range(0,nume):
#     for j in range(0,nume-i):
#         if list_test[i] > list_test[j]:
#             count += 1
#             dict[list_test[i]] = count
# print(dict)

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        num_size = len(nums)
        smaller_nums = num_size * [0]
        for i in range(num_size):
            for j in range(num_size):
                if nums[j] < nums[i]:
                    smaller_nums[i] = smaller_nums[i] + 1
        return smaller_nums
print(Solution().smallerNumbersThanCurrent([1,2,0,9,1,4]))



