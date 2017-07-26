'''
    we can transform finding the median into finding the kth number
    the method is based on dichotomy
    how to find the kth number of two sorted arrays?
    select first q numbers in arrary1 and select first p numbers in array2
    and  q+p is equivalent to k-1 ,so (q+1)th of array1 or (p+1)th of array2 must be the kth number of two sorted arrays
'''
def findmid(nums1,nums2):
    len1=len(nums1)
    len2=len(nums2)
    if(len1+len2)%2==0:
        return (findkth(nums1,len1,nums2,len2,(len1+len2)//2)+findkth(nums1,len1,nums2,len2,(len1+len2)//2+1))/2
    else:
        return findkth(nums1,len1,nums2,len2,(len1+len2+1)//2)

def findkth(nums1,len1,nums2,len2,k):
    p=min(k//2,len1)
    q=k-p-1
    p=p-1
    q=q-1
    if len1>len2:
        return findkth(nums2, len2, nums1, len1,k)
    if len1==0:
        return nums2[k-1]
    if 	k==1:
        return min(nums1[0],nums2[0])
    if  k==2 :
        return findkth(nums1, len1, nums2[1:], len2-1, 1) if nums1[0]>nums2[0] else  findkth(nums1[1:], len1-1, nums2, len2, 1)
    if nums1[p]>nums2[q]:
        return findkth(nums1, len1, nums2[q+1:],len2-q-1, k-q-1)
    elif nums1[p]<nums2[q]:
        return findkth(nums1[p+1:], len1-p-1, nums2, len2, k-p-1)
    elif nums1[p]==nums2[q]:
        return min(nums1[p+1],nums2[q+1])

nums1=[64, 147, 244, 246, 253, 255, 320, 370, 638, 741, 797, 880]
nums2=[]
print(findmid(nums1,nums2))