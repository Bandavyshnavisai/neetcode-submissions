class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap1={}
        for i in nums:
            hashmap1[i]=hashmap1.get(i,0)+1
            if(hashmap1[i]>=2):
                return i
        