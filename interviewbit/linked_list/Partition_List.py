# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        cur=A
        a=[]
        b=[]
        while cur:
            if cur.val>=B:
                b.append(cur.val)
            else:
                a.append(cur.val)
            cur=cur.next
        a=a+b
        cur=A
        i=0
        while cur:
            # print(i)
            cur.val=a[i]
            i+=1
            cur=cur.next
        return A