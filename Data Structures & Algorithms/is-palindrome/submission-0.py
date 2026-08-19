class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for ch in s:
            if ch.isalnum() == True:
                clean += ch
        clean = clean.lower()
               
        if clean[::-1] == clean:
            return True
        return False
        