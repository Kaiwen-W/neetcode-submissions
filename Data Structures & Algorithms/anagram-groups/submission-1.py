class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # naive sorting solution

        # seen = {}

        # for s in strs:
        #     sorted_s = ''.join(sorted(s))

        #     if seen.get(sorted_s, None):
        #         seen[sorted_s].append(s)
        #     else:
        #         seen[sorted_s] = [s]

        seen = {}

        for s in strs:
            freq = [0] * 26

            for c in s:
                freq[ord(c) - ord("a")] += 1
            
            freq = str(freq)

            if seen.get(freq, None) is None:
                seen[freq] = [s]
            else:
                seen[freq].append(s)
        
        result = []

        for lst in seen.values():
            result.append(lst)

        return result