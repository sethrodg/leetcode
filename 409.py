'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
'''

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        even_sum = 0
        biggest_odd = 0
        
        #counts = collections.Counter(s)
        
        counts = {i: 0 for i in s}
        
        for i in s:
            counts[i] += 1
            
        oddFound = False
        
        print(counts)
        
        for i in counts:
            num = counts[i]
            if num % 2 != 0:
                    oddFound = True
                    even_sum += (num-1)
            else:
                even_sum += num
                
        return even_sum + 1 if oddFound else even_sum
