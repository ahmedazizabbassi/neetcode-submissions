class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        prevsRow = collections.defaultdict(set)
        prevsCol = collections.defaultdict(set)
        prevsSquare = collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if (board[i][j] in prevsRow[i] or
                    board[i][j] in prevsCol[j] or
                    board[i][j] in prevsSquare[(i // 3, j // 3)]):
                    return False
                
                prevsRow[i].add(board[i][j])
                prevsCol[j].add(board[i][j])
                prevsSquare[(i // 3, j // 3)].add(board[i][j])

        return True