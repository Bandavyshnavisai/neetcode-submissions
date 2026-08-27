class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap1={}
        for i in range(len(nums)):
            hashmap1[nums[i]]=hashmap1.get(nums[i],0)+1
        sorted_items=sorted(hashmap1.items(),key=lambda item:item[1],reverse=True)
        ans=[]
        for i in range(k):
            ans.append(sorted_items[i][0])
        return ans
        