class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_streak = maximum_streak = 0
        for num in nums:
            if num == 1:
                current_streak +=1
            else:
                maximum_streak = max(current_streak, maximum_streak)
                current_streak = 0
        return max(maximum_streak, current_streak)