import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=collections.defaultdict(set)
        columns=collections.defaultdict(set)
        squares=collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                val=board[r][c]
                if val==".":
                    continue
                if (val in rows[r] or
                    val in columns[c] or
                    val in squares[r//3,c//3]):
                    return False
                rows[r].add(val)
                columns[c].add(val)
                squares[r//3,c//3].add(val)
        return True
        