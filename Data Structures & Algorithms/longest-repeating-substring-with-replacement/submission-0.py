class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq=0
        ans=0
        l=0
        mod_count={}
        for i in range(len(s)):
            mod_count[s[i]]=mod_count.get(s[i],0)+1
            max_freq=max(max_freq,mod_count[s[i]])
            if((i-l+1)-max_freq>k):
                mod_count[s[l]]-=1
                l+=1
            ans=max(ans,i-l+1)
        return ans

        