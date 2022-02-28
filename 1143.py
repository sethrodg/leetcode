'''
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        
        dp = [[0] *(len(text1)+1) for n in range(len(text2)+1)]
        
        for i in range(len(text2)):
            for j in range(len(text1)):
                if text2[i] == text1[j]:
             
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                 
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
                    
        return dp[-1][-1]
        

