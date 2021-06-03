# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        cur=A
        dic={}
        while cur:
            dic[cur.val]=dic.get(cur.val,0)+1
            if dic[cur.val]>1:
                return cur
            cur=cur.next
        return ListNode("NULL")