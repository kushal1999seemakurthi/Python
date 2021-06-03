class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        i=0
        p=0
        s=A
        if A==1:
            return 1
        if A==2:
            return 3
        while s>=2**(i//2):
            p+=2**(i//2)
            s-=2**(i//2)
            i+=1
        if s!=0:
            i+=1
            b=bin(s-1)[2:]
        else:
            # print(i)
            s=0
            for i in range(6):
                s+=2**i
            return s
        
        # i gives length of string
        # s gives the order of the dstring in that length
        #   and also the half of the symetrical string
        q=i%2
        l1=i//2+q-len(b)
        st="1"+"0"*(l1-1)+b
        # print(st,s)
        st=st+(st[:-q])[::-1]+(1-q)*(st)[::-1]
        v=[i for i in range(len(st)) if st[i]=="1"]
        # print(i,s,l1,st,v)
        s=0
        for i in v:
            s+=2**i
        return s