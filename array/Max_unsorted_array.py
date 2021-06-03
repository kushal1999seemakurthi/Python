class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        si = 0
        ei = False
        mi=[False,max(A)]
        ma=[False,min(A)]
        for i in range(1,len(A)):
            if A[i]<A[i-1] and mi[1]>A[i]:
                mi=[i,A[i]]
        # print("--1--",mi)
        if mi[0]:
            for j in range(mi[0]):
                
                if A[j]>mi[1]:
                    si=j
                    break
            for k in range(1,len(A)):
                # print(k,A[k],A[k-1],ma[1] )
                if A[k-1]>A[k] and ma[1]<A[k-1]:
                    ma=[k-1,A[k-1]]
            # print("--2--",ma)
            for l in range(ma[0],len(A)):
                if ma[1]>A[l] :
                    ei=l
            return [si, ei]        
            
        else: return [-1]
        
        
