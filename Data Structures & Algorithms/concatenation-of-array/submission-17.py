class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
         n = len(nums)-1
         for i in range(len(nums)):
            nums.append(nums[i])
         return nums