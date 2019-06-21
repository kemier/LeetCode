'''
51. N-Queens
Hard

https://leetcode.com/problems/n-queens/
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
'''
class Solution:
    def solveNQueens(self, n: int) -> int:
        self.col = [False] * n
        self.diag = [False] * (2 * n)
        self.anti_diag = [False] * (2 * n)
        self.result = []
        self.recursive(0, n, [])
        return self.result


    def recursive(self, row, n, column):
        if row == n:
            self.result.append(list(map(lambda x: '.' * x + 'Q' + '.' * (n - 1 - x), column)))
        else:
            for i in range(n):
                if not self.col[i] and not self.diag[row + i] and not self.anti_diag[n - i + row]:
                    self.col[i] = self.diag[row + i] = self.anti_diag[n - i + row] = True
                    self.recursive(row + 1, n, column + [i])
                    self.col[i] = self.diag[row + i] = self.anti_diag[n - i + row] = False


sol = Solution()
print(sol.solveNQueens(4))