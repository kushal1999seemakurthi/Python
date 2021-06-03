class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        if not A or len(A) < 2: return 0
        # A.sort()
        # n=len(A)
        # m=A[1]-A[0]
        # for i in range(1,n):
        #     m=max(m,A[i]-A[i-1])
        # return m
        n=len(A)
        b=[]
        for i in range(n-1):
            b.append([])
        # print(b,n)
        m=min(A)
        ma=max(A)
        p= (max(A)-min(A))/(n-1)
        if p==0 : return 0
        for i in A:
            j=int((i-m)/p)
            if(i==ma):
                b[-1].append(i)
            else:
                b[j].append(i)
        # print(b)
        c=[]
        # print(c)
        for i in b:
            try:
                c.append((min(i),max(i)))
            except:
                continue
        # print(c)
        mi,ma=c[0]
        ma=mi
        q=int(p)
        for i in c:
            imi,ima=i
            q=max(q,imi-ma)
            # print(q,imi,ma)
            ma=ima
        return q