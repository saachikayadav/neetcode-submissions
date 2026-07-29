class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            letters = tuple(sorted(word))

            if letters not in groups:
                groups[letters] = []

            groups[letters].append(word)

        return list(groups.values())
        
        
        