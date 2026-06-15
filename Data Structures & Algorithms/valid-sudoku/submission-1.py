class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check that each row only contains 1-9 once or .
        valid = set(["1", "2", "3", "4", "5", "6", "7", "8", "9", "."])

        # declare hashmap which maps column index (0 -> 8) to elements in that column
        col_board = {}

        # declare hashmap which maps square index to elements in that square
        squares = {}

        for i, row in enumerate(board):
            nums = set()

            for j, entry in enumerate(row):
                if entry == ".":
                    continue

                if entry not in valid:
                    return False
                
                # entry is already in row
                if entry in nums:
                    return False
                nums.add(entry)

                col_board.setdefault(j, []).append(entry)

                square_idx = (i // 3) * 3 + (j // 3)
                squares.setdefault(square_idx, []).append(entry)


        for key in col_board.keys():
            nums = set()

            for entry in col_board[key]:
                if entry in nums:
                    return False
                nums.add(entry)
        
        for key in squares.keys():
            nums = set()

            for entry in squares[key]:
                if entry in nums:
                    return False
                nums.add(entry)

        return True
