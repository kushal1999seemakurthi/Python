# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        a=""
        b=""
        cur=A
        while cur:
            a+=str(cur.val)
            cur=cur.next
        
        cur=B
        while cur:
            b+=str(cur.val)
            cur=cur.next
        
        a=int(a[::-1])
        b=int(b[::-1])
        c=a+b
        c=list(map(int,list(str(c))[::-1]))
        a=ListNode(c[0])
        cur=a
        for i in c[1:]:
            cur.next=ListNode(i)
            cur=cur.next
        return a