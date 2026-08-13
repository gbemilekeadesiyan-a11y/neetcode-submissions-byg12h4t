class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # initialise an empty Hash set
        for num in nums: 
            if num in seen:# check if an item is in seen 
                return True
            seen.add(num) # since it is not seen then we add it to seen
        return False # If after adding to seen we still do not see it again