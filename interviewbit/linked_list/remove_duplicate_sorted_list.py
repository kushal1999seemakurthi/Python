# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        dic={}
        cur=A
        while cur:
            dic[cur.val]=dic.get(cur.val,0)+1
            cur=cur.next
        
        cur=A
        prev=None
        while cur:
            while dic[cur.val]>1:
                cur=cur.next
                if cur==None:
                    break
            # if cur: print("1---",cur.val)
            if prev==None:
                if cur:
                    # print("2---",cur.val)
                    prev=ListNode(cur.val)
                    p=prev
                else:
                    # print("4---",cur.val)
                    prev=cur
                    p=prev
            elif cur:
                if dic[cur.val]==1:
                    # print("3---",cur.val)
                    p.next=ListNode(cur.val)
                    p=p.next
            if cur:
                cur=cur.next
        return prev