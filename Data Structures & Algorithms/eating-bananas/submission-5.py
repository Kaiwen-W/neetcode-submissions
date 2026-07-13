class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower_k = 1
        upper_k = max(piles) # upper bound, since h >= len(piles)

        # split upper_k in half
        # if k too high, lower 
        # if k too lower, upper

        while lower_k <= upper_k:
            k = lower_k + (upper_k - lower_k) // 2

            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / k)

            if total_time <= h:
                upper_k = k - 1
            else:
                lower_k = k + 1
        
        if h - total_time < 0:
            return k + 1
        return k 
