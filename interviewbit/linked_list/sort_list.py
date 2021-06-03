# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        a=[]
        cur=A
        while cur:
            a.append(cur.val)
            cur=cur.next
        a.sort()
        
        cur=A
        i=0
        while cur:
            cur.val=a[i]
            cur=cur.next
            i+=1
        return A