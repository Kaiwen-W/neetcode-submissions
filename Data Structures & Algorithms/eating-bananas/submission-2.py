class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles) # since h >= len(piles)

        while True:
            idx = 0
            copy = piles.copy()
            for _ in range(h):
                copy[idx] -= k

                if copy[idx] <= 0:
                    idx += 1
                if idx > len(copy) - 1:
                    break
            if copy[-1] < 0:
                k -= 1
            else:
                return k + 1     