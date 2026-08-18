class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 1
        longest = 1
        s = sorted(set(nums))
        leng = len(s) - 1
        for i in range(leng,0,-1):
            if s[i-1] == s[i] - 1:
                count += 1
                
            else:
                count = 1
            longest = max(longest, count)
        return longest




        