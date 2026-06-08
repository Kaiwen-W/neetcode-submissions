class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)] # freq[i] = num elements in i 

        count = {} # maps nums to their counts
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for val in count.keys():
            freq[count[val]].append(val)
        
        res = []
        for i in range(len(freq) - 1, 0, -1): 
            for n in freq[i]:
                res.append(n)

                if len(res) == k:
                    return res
        
