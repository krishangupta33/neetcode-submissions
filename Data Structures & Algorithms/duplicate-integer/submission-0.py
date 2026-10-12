class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n=len(nums)-1
        for i in range(n):
            diff=nums[i+1]-nums[i]
            if diff==0:
                return True
        
        return False
        

        