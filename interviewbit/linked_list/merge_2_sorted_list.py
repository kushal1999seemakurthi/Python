# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        # while A or B:
        #     if A and B:
        #         if A.val>=B.val:
        #             if Ret==None:
        #                 Ret=ListNode(B.val)
        #                 a=Ret
        #             else:
        #                 a=ListNode(B.val)
        #             B=B.next
        #         else:
        #             if Ret==None:
        #                 Ret=ListNode(B.val)
        #                 a=Ret
        #             else:
        #                 a=ListNode(B.val)
        #             A.next
        #         a=a.next
        #     elif A==None:
        #         a=B
        #         B=None
        #     else:
        #         a=A
        #         A=None
        cur=A
        a=[]
        while cur:
            a.append(cur.val)
            cur=cur.next
        cur=B
        while cur:
            a.append(cur.val)
            cur=cur.next
        a.sort()
        Ret=ListNode(a[0])
        v=Ret
        for i in a[1:]:
            v.next=ListNode(i)
            v=v.next
        return Ret