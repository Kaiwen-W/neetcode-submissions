class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # m * n matrix
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m * n - n

        while l <= r:
            mid = l + (r - l) // 2
            x = mid // m 
            y = mid % m 

            print("x =", x)
            print("y =", y)

            n = matrix[x][y]

            if n == target:
                return True
            elif n < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False