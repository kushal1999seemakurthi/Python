# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def solve(self, A, B):
        a=[]
        cur=A
        while cur:
            a.append(cur.val)
            cur=cur.next
        b=[]
        c=[]
        for i in range(len(a)):
            c.append(a[i])
            # print(c,b)
            if (i+1)%B==0:
                c=c[::-1]*(((i+1)//B)%2) + c*(((i+1)//B+1)%2)
                b=b+c
                c=[]
        cur=A
        l=0
        while cur:
            cur.val=b[l]
            cur=cur.next
            l+=1
        return A