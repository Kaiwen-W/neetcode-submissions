class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use array [0] * 26 to hash 

        anagrams = defaultdict(list)

        for s in strs:
            key = [0] * 26

            for c in s:
                key[ord(c) - ord('a')] += 1
            
            freq = str(key)
            
            anagrams[freq].append(s)
        
        res = []
        for key in anagrams.keys():
            res.append(anagrams[key])
        
        return res