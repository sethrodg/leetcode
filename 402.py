'''
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.
'''
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []
        res = ""
        
        for i in num:
            
            while stack and int(stack[-1]) > int(i) and k > 0:
                stack.pop()
                k-=1
                
            stack.append(i)
            
        print(stack)
        while stack:
            l = stack.pop()
            res = res + l
            
        res = res[::-1]
        while res and res[0] == "0":
            res = res[1:]
        
        if k > 0:
            res = res[: len(res)-k]
            
        return res if res else "0"
            
