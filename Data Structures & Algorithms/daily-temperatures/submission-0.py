class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        ss=[]
        for i,t in enumerate(temperatures):
            while ss and t>ss[-1][0]:
                stackt,stackind=ss.pop()
                res[stackind]=(i-stackind)
            ss.append([t,i])
        return res


        