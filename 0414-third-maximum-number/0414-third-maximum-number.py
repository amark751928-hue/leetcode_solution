class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        unique_nums = sorted(set(nums), reverse=True)
        
        if len(unique_nums) >= 3:
            return unique_nums[2]
        return unique_nums[0]