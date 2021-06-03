class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        a=list(A)
        d={}
        for i in a:
            d[i]=d.get(i,0)
            d[i]+=1
            if(d[i]>1):
                return i