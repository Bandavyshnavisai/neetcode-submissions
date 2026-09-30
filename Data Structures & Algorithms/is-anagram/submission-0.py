class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mod_count1={}
        mod_count2={}
        for i in s:
            mod_count1[i]=mod_count1.get(i,0)+1
        for j in t:
            mod_count2[j]=mod_count2.get(j,0)+1
        if mod_count1==mod_count2:
            return True
        else:
            return False
        