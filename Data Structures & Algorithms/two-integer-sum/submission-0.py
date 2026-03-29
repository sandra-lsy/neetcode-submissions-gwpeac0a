class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dict_nums = {}
        for i in range(0, n):
            diff = target - nums[i]
            if diff in dict_nums:
                j = dict_nums[diff]
                return [j, i]
            else:
                dict_nums[nums[i]] = i
        