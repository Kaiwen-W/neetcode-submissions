class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # m * n matrix
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m * n - 2

        while l <= r:
            mid = l + (r - l) // 2
            x = mid // m 
            y = mid & m 

            n = matrix[x][y]

            if n == target:
                return True
            elif n < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False