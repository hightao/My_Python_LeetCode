# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.next = None
                
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        fin=result=ListNode(0)
        carry=0
        while l1 or l2 or carry:
            val=0
            if l1:
                val+=l1.val
                l1=l1.next
            if l2:
                val+=l2.val
                l2=l2.next
            val+=carry
            carry,val = divmod(val,10)
            result.next=ListNode(val)
            result=result.next
        return fin.next
    
"""
:type l1: ListNode
:type l2: ListNode
:rtype: ListNode
"""
        