class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0]
        for i in range(1, len(height)):
            prefix.append(max(prefix[i - 1], height[i - 1]))
        
        suffix = [0] * len(height)
        for i in range(len(height) - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], height[i + 1])

        total = 0
        for i in range(len(height)):
            water = min(prefix[i], suffix[i]) - height[i]
            if water > 0:
                total += water

        return total