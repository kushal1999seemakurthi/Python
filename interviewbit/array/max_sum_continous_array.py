class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        # su=0
        # m1=min(A)
        # m=m1
        # for i in A:
        #     su+=i
        #     if(su<0):
        #         m=max(m,su)
        #         su=0
        #     else:
        #         m=max(m,su)
        # return m
        s =0
        m=min(A)
        for i in A :
            s+=i
            m=max(s,m)
            if s<0:
                s=0
        return m