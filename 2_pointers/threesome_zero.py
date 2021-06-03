class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        a=set(A)
        dic={}
        for i in A:
            dic[i]=dic.get(i,0)+1
        a=list(a)
        a.sort()
        # print(a)
        l=len(a)
        o=[]
        for i in range(l-1):
            for j in range(i+1,l):
                req=-a[i]-a[j]
                if req not in dic:
                    continue
                # print("i= ",i,"j=",j,"a[i]=",a[i],"a[j]=",a[j],"req=",req ,dic.get(req,0))
                if req == a[i] and dic[a[i]]>1:
                    # print(a[i],a[j],req,i,j,"i")
                    o.append([a[i],req,a[j]])
                elif req == a[j] and dic[a[j]]>1:
                    # print(a[i],a[j],req,i,j,"j")
                    o.append([a[i],a[j],req])
                elif req > a[i] and req >a[j]:
                    # print(a[i],a[j],req,i,j,"req")
                    o.append([a[i],a[j],req])
                elif req > a[i] and req <a[j] :
                    o.append([a[i],req,a[j]])
                elif req < a[i] and req <a[j] :
                    o.append([req,a[i],a[j]])
                    
            if a[i]==0:
                if dic[0]>2:
                    o.append([0,0,0])
        o.sort()
        out=[]
        temp=[]
        for i in o:
            if i!=temp:
                out.append(i)
                temp=i
        
        return out