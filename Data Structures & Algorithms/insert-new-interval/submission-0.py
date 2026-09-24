class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i, n = 0, len(intervals)
        a, b = newInterval

        while i < n and intervals[i][1] < a:
            res.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= b:
            a = min(a, intervals[i][0])
            b = max(b, intervals[i][1])
            i += 1
        
        res.append([a, b])
        res.extend(intervals[i:])

        return res
            


