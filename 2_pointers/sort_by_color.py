class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        l=len(A)
        dic={}
        for i in range(len(A)):
            dic[A[i]]=dic.get(A[i],[]).append(i)
            
        for i in dic.get(0,[])[::-1]:
            n0=i
            try:
                n1=min(dic[1])
            except:
                n1=l+1
            try:
                n2=min(dic[2])
            except:
                n2=l+1
            if n1<n2 and n1<n0:
                A[n0],A[n1]=A[n1],A[n0]
                dic[0].remove(n0)
                dic[1].remove(n1)
                dic[0].append(n1)
                dic[1].append(n0)
            if n2<n1 and n2<n0:
                A[n0],A[n2]=A[n2],A[n0]
                dic[0].remove(n0)
                dic[2].remove(n2)
                dic[0].append(n2)
                dic[2].append(n0)
        
        for i in dic.get(1,[])[::-1]:
            n1=i
            try:
                n2=min(dic[2])
            except:
                n2=l+1
            if n1>n2 :
                A[n1],A[n2]=A[n2],A[n1]
                dic[2].remove(n2)
                dic[1].remove(n1)
                dic[2].append(n1)
                dic[1].append(n2)
        return A