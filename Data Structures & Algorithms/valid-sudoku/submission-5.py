class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row
        for i in range(9):
            s = set()
            
            for j in range(9):
                digit = board[i][j]

                if digit in s:
                    return False
                elif digit != '.':
                    s.add(digit)

        # col
        for i in range(9):
            s = set()
            
            for j in range(9):
                digit = board[j][i]

                if digit in s:
                    return False
                elif digit != '.':
                    s.add(digit)
        # box
        starts = [(0,0), (0,3), (0,6),
                  (3,0), (3,3), (3,6),
                  (6,0), (6,3), (6,6)]

        for i, j in starts:
            s = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    digit = board[row][col]

                    if digit in s:
                        return False
                    elif digit != '.':
                        s.add(digit)
        
        return True


