class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        dic={}
        for i in A:
            dic[i]=dic.get(i,0)+1
        for i,j in dic.items():
            if B!=0:            
                if dic.get(i+B,0)+dic.get(i-B,0)>0:
                    return 1
            else:
                if dic.get(i,0)>1:
                    return 1
        return 0
