class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        rev_s = ''.join(sorted(s))
        rev_t = ''.join(sorted(t))   
        if rev_s != rev_t:
            return False
        return True     
        

        