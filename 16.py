'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        res = 0
        leastDist = sys.maxsize
        
        nums.sort()
        
        for i in range(len(nums)):
            
            if i != 0 and nums[i] == nums[i-1]:
                continue
            
            one = nums[i]
            
            l, r = i+1, len(nums)-1
            
            while l < r:
                
                threesum = one + nums[l] + nums[r]
                
                if threesum == target:
                    return threesum
                
                dist = target - threesum
           
                if (abs(dist)) < leastDist:
                    
                    leastDist = abs(dist)
                    res = threesum
                    
                if threesum < target:
                    l+=1
                elif threesum > target:
                    r-=1
                
        return res
