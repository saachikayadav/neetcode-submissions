class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i!=j:
            for i in range(len(nums)):
                if nums[i] + nums [j] == target:
                    return sorted([i,j])
            j-=1
        return False
            


          