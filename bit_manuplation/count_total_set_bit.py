class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        b=bin(A)[2:]
        b=b[::-1]
        n=[]
        for i in range(len(b)):
            if b[i]=="1":
                n.append(i)
        n=n[::-1]
        s=0
        for j in range(len(n)):
            s+=(int(2**(n[j]-1))*n[j] + 1 + j*int(2**n[j]))%1000000007
        return s%1000000007