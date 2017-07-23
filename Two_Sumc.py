class Solution:
    def twoSum(self, nums, target):
        d={}
        i=0
        for x in nums:
            if target-x in d:
                return (d[target-x],i)
            else:
                d.update({x:i})
            i=i+1