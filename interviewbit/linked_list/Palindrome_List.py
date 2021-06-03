class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        a=[]
        cur=A
        while cur:
            a.append(cur.val)
            cur=cur.next
        b=a[::-1]
        l=len(a)
        for i in range(l):
            if a[i]!=b[i]:
                return 0
        return 1