class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mod_count={}
        for i in nums:
            mod_count[i]=mod_count.get(i,0)+1
        for j in mod_count.values():
            if (j>1):
                return True
        return False
        