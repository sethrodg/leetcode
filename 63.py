'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        dp = {}
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
  
        if obstacleGrid[m-1][n-1] == 1:
            return 0
        
        def recurse(i, j):
            
            if i == m or j == n:
                return 0
            
            if obstacleGrid[i][j] == 1:
                return 0
            
            if (i,j) in dp:
                print("cache word")
                return dp[(i,j)]
            
            if i == m-1 and j == n-1:
                return 1
            
            dp[(i,j)] = recurse(i+1, j) + recurse(i, j+1)
            return dp[(i,j)]
            
        return recurse(0, 0)

