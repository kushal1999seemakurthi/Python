class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        cur=A
        a=[cur.val]
        while cur.next!=None:
            cur=cur.next
            a.append(cur.val)
        a.sort()
        cur=A
        cur.val=a[0]
        i=1
        while cur.next!=None:
            cur=cur.next
            cur.val=a[i]
            i+=1
        return A