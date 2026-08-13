class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}   # value:index 
        for i, n in enumerate(nums):           # This basically iterate through both value and index
            diff = target - n                  # Finding the number to add to n to get to target
            if diff in prevMap:                # Check if this difference is in prevMap
                return [prevMap[diff],i]       # if it is, we return the index of that number or difference and the index(i) of the first number(n)
            prevMap[n] = i                     # if not found, we just move on to the next number
        return                                 # Since we are guaranteed that we have a sloution, we just return nothing (No edge cases) 