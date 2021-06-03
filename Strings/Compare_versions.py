class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        A=list(map(int,A.split(".")))
        while 0 in A:
            A.remove(0)
            
        B=list(map(int,B.split(".")))
        while 0 in B:
            B.remove(0)
            
            
        if A>B:
            return 1
        elif A<B:
            return -1
        else:
            return 0