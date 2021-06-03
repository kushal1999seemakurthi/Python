class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        p=map(str,A)
        p="".join(p)
        p=int(p)+1
        return p