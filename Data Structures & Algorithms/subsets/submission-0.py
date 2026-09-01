class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(index,curr_path):
            if index==len(nums):
                res.append(curr_path.copy())
                return
            curr_path.append(nums[index])
            backtrack(index+1,curr_path)
            curr_path.pop()
            backtrack(index+1,curr_path)
        backtrack(0,[])
        return res


        