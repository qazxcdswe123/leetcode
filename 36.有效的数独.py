#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, diag = defaultdict(set), defaultdict(set), defaultdict(set)
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                if num in row[i] or num in col[j] or num in diag[(i//3, j//3)]:
                    return False
                row[i].add(num)
                col[j].add(num)
                diag[(i//3, j//3)].add(num)
        
        return True
# @lc code=end

