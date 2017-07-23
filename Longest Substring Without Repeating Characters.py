class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start=lmax=0
        cur_str={}        
        for i in range(len(s)):
            if s[i] in cur_str and start <= cur_str[s[i]]: # right judgement avoids example like "tmmzuxt",  't' needs modifying its index
                start=cur_str[s[i]]+1
            else:
                lmax=max(lmax,i-start+1)
            cur_str[s[i]]=i
        return lmax