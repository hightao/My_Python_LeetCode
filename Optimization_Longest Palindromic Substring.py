#	This optimization uses Manacher's algorithm which time complexity is O(n)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: strfo
        """
        a='$#'
        mx=0
        id=0
        for i in s:
            a+=i
            a+='#'
        p=[0]*len(a)
        for i in range(1,len(a)):
            if mx>i:
                p[i]=min(p[2*id-i],mx-i)
            else :
                p[i]=1
            while i+p[i]<len(a) and a[i + p[i]] == a[i - p[i]]  :
                p[i]=p[i]+1

            if i+p[i] >mx:
                mx=i+p[i]
                id=i
        mid=p.index(max(p))
        smax=a[mid-p[mid]+1:mid+max(p)].replace('#','')
        return smax


s=Solution()
#s.isPalindrome("babad")
print(s.longestPalindrome("ababc"))
