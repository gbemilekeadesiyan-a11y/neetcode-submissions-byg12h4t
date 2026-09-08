class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
         n = 2
         ans = []
         for i in range(n):
            for num in nums:
               ans.append(num)
         return ans
