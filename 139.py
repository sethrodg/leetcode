'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [0] * (len(s)+1)
        dp[-1] = 1
        
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                temp = s[i: i+len(w)]
                if (len(w) + i) <= len(s) and temp == w:
                    dp[i] =  dp[i+len(w)]
                if dp[i]:
                    break
                        
        return dp[0]
        
