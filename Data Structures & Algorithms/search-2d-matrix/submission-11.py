class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # m * n matrix
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m * n - 1 

        while l <= r:
            mid = l + (r - l) // 2
            x = mid // n
            y = mid % n

            print("x =", x)
            print("y =", y)

            num = matrix[x][y]

            if num == target:
                return True
            elif num < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False