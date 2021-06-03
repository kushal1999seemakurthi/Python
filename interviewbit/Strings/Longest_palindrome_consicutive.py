class Solution:
    # @param A : string
    # @return a strings
    def palin(self, A, start, end):
        left = start
        right = end
        while left >=0 and right <len(A) and A[left] == A[right]:
            left -=1
            right +=1
        return right - left -1
    
    def longestPalindrome(self, A):
        l=len(A)
        ll=len(set(A))
        if l==ll:
            return A[0]
        a=[]
        Start=0
        End = 0
        for i in range(l):
            l1=self.palin(A,i,i)
            l2=self.palin(A,i,i+1)
            length= max(l1,l2)
            # print(i,l1,l2,length)
            if length >End-Start+1:
                Start = i - (length-1)//2
                End = i + length//2
            # print("---",Start,End)
        return A[Start:End+1]