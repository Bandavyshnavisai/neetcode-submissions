class Solution:
    def findMin(self, nums: List[int]) -> int:
       res=nums[0]
       l=0
       h=len(nums)-1
       while l<=h:
        if nums[l]<nums[h]:
            res=min(res,nums[l])
            break
        m=(l+h)//2
        res=min(res,nums[m])
        if nums[m]>=nums[h]:
            l=m+1
        else:
            h=m-1
       return res

       
