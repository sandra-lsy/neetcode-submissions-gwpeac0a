class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_nums = {}
        for num in nums:
            if num in dict_nums:
                return True
            else:
                dict_nums[num] = 1
        
        return False

        