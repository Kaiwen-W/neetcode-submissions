class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # formula = min(heights[l], heights[r]) x (r - l)

        # only move pointer if increases height components by 
        # at least 2 as 1 is removed by moving closer

        l = 0 
        r = len(heights) - 1 

        most = 0
        while l < r:
            min_height = min(heights[l], heights[r])
            width = r - l 

            area = min_height * width 
            most = max(most, area)

            if heights[l + 1] > heights[l] + 1:
                l += 1 
            elif heights[r - 1] > heights[r] + 1:
                r -= 1
            else:
                l += 1 
                r -= 1
        


