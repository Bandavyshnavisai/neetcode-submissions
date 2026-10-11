class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
       if len(s1)>len(s2):
        return False
       mod_count1={}
       mod_count2={}
       for i in range(len(s1)):
        mod_count1[s1[i]]=mod_count1.get(s1[i],0)+1
        mod_count2[s2[i]]=mod_count2.get(s2[i],0)+1
       if mod_count1==mod_count2:
        return True
       l=0
       for i in range(len(s1),len(s2)):
        mod_count2[s2[i]]=mod_count2.get(s2[i],0)+1
        mod_count2[s2[l]]-=1
        if (mod_count2[s2[l]]==0):
            del mod_count2[s2[l]]
        l+=1
        if (mod_count1==mod_count2):
            return True
       return False


            
