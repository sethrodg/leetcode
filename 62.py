'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = {}
        
        def recurse(i, j):
            
            if (i,j) in dp:
                return dp[(i,j)]
            elif (j,i) in dp:
                return dp[(j,i)]

            if i == 0 or j == 0:
                return 0
            if i == 1 or j == 1:
                return 1
            
            dp[(i,j)] = recurse(i-1, j) + recurse(i, j-1)
            return dp[(i,j)]
            
        return recurse(m, n)
