class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row[r]:
                    return False
                if board[r][c] in col[c]:
                    return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                sqR = r//3
                sqC = c//3
                if board[r][c] in squares[(sqR,sqC)]:
                    return False
                squares[(sqR,sqC)].add(board[r][c])

        return True

                


        