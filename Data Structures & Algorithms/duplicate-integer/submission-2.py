class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = nums.copy() 
        for i in range(len(nums)):
            store = nums[i]
            new.remove(store)
            if store in new:
                return True
            
        return False