# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        cur=A
        l=0
        while cur:
            l+=1
            cur=cur.next
        p=l//2
        if p-B<0:
            return -1
        if p==B:
            return A.val
        
        cur=A
        l=0
        v=cur.val
        while l<=p-B and cur:
            v=cur.val
            cur=cur.next
            l+=1
        return v