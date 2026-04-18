class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - 97] += 1 
            
            freq = str(freq)

            if anagrams.get(freq, None) is None:
                anagrams[freq] = [s]
            else:
                anagrams[freq].append(s)
        
        ans = []
        for _, value in anagrams.items():
            ans.append(value)
        return ans

